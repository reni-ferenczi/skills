#!/usr/bin/env python3
"""Test suite for the gplates-code skill.

    python scripts/test_gpq.py            # everything
    python scripts/test_gpq.py -v         # verbose
    python scripts/test_gpq.py Extractors # one TestCase

Unit tests for the extractors and the source-tree validation run without an
index. The query tests need a built index and are skipped (loudly) without one.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from gplates_index import build  # noqa: E402
from gplates_index.common import DB_PATH, SkillError, check_source_root, open_db  # noqa: E402

GPQ = SCRIPTS / "gpq.py"
HAVE_INDEX = DB_PATH.exists()
needs_index = unittest.skipUnless(HAVE_INDEX, "no index - run scripts/setup_index.py first")


def gpq(*argv):
    """Run gpq and return (returncode, stdout, stderr)."""
    proc = subprocess.run([sys.executable, str(GPQ), *argv],
                          capture_output=True, text=True, encoding="utf-8", errors="replace")
    return proc.returncode, proc.stdout, proc.stderr


def hits(stdout):
    """Result lines only: drop the `#` summary lines and blanks."""
    return [ln for ln in stdout.splitlines() if ln and not ln.startswith("#")]


# ---------------------------------------------------------------------------
# Extractors (no index required)
# ---------------------------------------------------------------------------

class Extractors(unittest.TestCase):

    def test_includes(self):
        text = '#include <boost/optional.hpp>\n#include "app-logic/Foo.h"\n// #include "x.h"\n'
        got = list(build.extract_includes(text))
        self.assertEqual(got, [(1, "boost/optional.hpp", 1), (2, "app-logic/Foo.h", 0)])

    def test_connection_single_line(self):
        text = ('QObject::connect(button, SIGNAL(clicked()), this, SLOT(handle_click()));\n')
        (line, sender, signal, receiver, slot), = build.extract_connections(text)
        self.assertEqual((line, sender, signal, receiver, slot),
                         (1, "button", "clicked()", "this", "handle_click()"))

    def test_connection_multiline_with_nested_parens(self):
        text = (
            "void wire()\n"
            "{\n"
            "\tQObject::connect(\n"
            "\t\t\t&controller,\n"
            "\t\t\tSIGNAL(time_changed(const double &)),\n"
            "\t\t\tthis,\n"
            "\t\t\tSLOT(react_time_changed(const double &)));\n"
            "}\n")
        (line, sender, signal, receiver, slot), = build.extract_connections(text)
        self.assertEqual(line, 3)
        self.assertEqual(sender, "&controller")
        self.assertEqual(signal, "time_changed(const double &)")
        self.assertEqual(receiver, "this")
        self.assertEqual(slot, "react_time_changed(const double &)")

    def test_connection_without_signal_macro_is_ignored(self):
        self.assertEqual(list(build.extract_connections("connect(a, &A::b, c, &C::d);\n")), [])

    def test_py_api_class_chain(self):
        text = (
            'void export_thing()\n'
            '{\n'
            '\tbp::class_<GPlatesApi::Thing>("Thing", bp::no_init)\n'
            '\t\t.def("do_it", &GPlatesApi::Thing::do_it)\n'
            '\t\t.def_readonly("size", &GPlatesApi::Thing::size)\n'
            '\t\t;\n'
            '\tbp::def("standalone", &standalone);\n'
            '}\n')
        got = list(build.extract_py_api(text))
        self.assertEqual([(g[1], g[2], g[3]) for g in got], [
            ("", "Thing", "class"),
            ("Thing", "do_it", "method"),
            ("Thing", "size", "attribute"),
            ("", "standalone", "function"),
        ])
        self.assertEqual(got[0][0], 3)
        self.assertEqual(got[3][0], 7)

    def test_py_api_owner_resets_after_statement(self):
        """A module-level def() after a class_ chain must not be attributed to the class."""
        text = ('class_<A>("A").def("m", &A::m);\ndef("free_fn", &free_fn);\n')
        got = list(build.extract_py_api(text))
        self.assertEqual([(g[1], g[2], g[3]) for g in got],
                         [("", "A", "class"), ("A", "m", "method"), ("", "free_fn", "function")])

    def test_classify(self):
        cases = {
            ("src/app-logic/Foo.cc", ".cc", "Foo.cc"): "cpp",
            ("src/qt-widgets/FooUi.ui", ".ui", "FooUi.ui"): "ui",
            ("src/qt-resources/opengl/x.glsl", ".glsl", "x.glsl"): "shader",
            ("src/qt-resources/gpgim/gpgim.xml", ".xml", "gpgim.xml"): "gpgim",
            ("sample-data/gpml/a.gpml", ".gpml", "a.gpml"): "data",
            ("src/CMakeLists.txt", ".txt", "CMakeLists.txt"): "build",
            ("CHANGELOG", "", "CHANGELOG"): "doc",
            ("scripts/reconstruct.py", ".py", "reconstruct.py"): "python",
        }
        for (rel, ext, name), expected in cases.items():
            self.assertEqual(build.classify(rel, ext, name), expected, rel)

    def test_ui_parsing(self):
        xml = (
            '<?xml version="1.0"?>\n<ui version="4.0">\n'
            ' <class>SampleDialog</class>\n'
            ' <widget class="QDialog" name="SampleDialog">\n'
            '  <property name="windowTitle"><string>Sample</string></property>\n'
            '  <widget class="QPushButton" name="button_ok">\n'
            '   <property name="text"><string>OK</string></property>\n'
            '  </widget>\n'
            ' </widget>\n'
            ' <action name="action_Quit">\n'
            '  <property name="text"><string>Quit</string></property>\n'
            ' </action>\n'
            '</ui>\n')
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SampleDialogUi.ui"
            path.write_text(xml, encoding="utf-8")
            form, widgets = build.extract_ui(path)
        self.assertEqual(form, ("SampleDialog", "QDialog", "Sample"))
        self.assertIn(("QPushButton", "button_ok", "OK"), widgets)
        self.assertIn(("QAction", "action_Quit", "Quit"), widgets)

    def test_ui_parsing_survives_broken_xml(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "Broken.ui"
            path.write_text("<ui><class>Nope", encoding="utf-8")
            self.assertEqual(build.extract_ui(path), (None, []))


# ---------------------------------------------------------------------------
# Source tree validation (no index required)
# ---------------------------------------------------------------------------

class SourceValidation(unittest.TestCase):

    def test_missing_directory_is_rejected(self):
        with self.assertRaises(SkillError) as ctx:
            check_source_root(Path(tempfile.gettempdir()) / "definitely-not-here-12345")
        self.assertIn("not found", str(ctx.exception))

    def test_unrelated_directory_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "src").mkdir()
            with self.assertRaises(SkillError) as ctx:
                check_source_root(tmp)
        self.assertIn("does not look like a GPlates source tree", str(ctx.exception))

    def test_old_version_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for marker in ("CMakeLists.txt", "CHANGELOG", "cmake/modules/Version.cmake",
                           "src/CMakeLists.txt", "src/gplates_main.cc",
                           "src/qt-resources/gpgim/gpgim.xml"):
                path = root / marker
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("", encoding="utf-8")
            for d in ("src/app-logic", "src/qt-widgets", "src/maths", "src/model"):
                (root / d).mkdir(parents=True, exist_ok=True)
            (root / "cmake/modules/Version.cmake").write_text(
                "set(GPLATES_VERSION_MAJOR 2)\n"
                "set(GPLATES_VERSION_MINOR 4)\n"
                "set(GPLATES_VERSION_PATCH 0)\n", encoding="utf-8")
            with self.assertRaises(SkillError) as ctx:
                check_source_root(root)
        self.assertIn("requires 2.5.0", str(ctx.exception))

    @needs_index
    def test_configured_source_still_valid(self):
        con = open_db()
        root = dict(con.execute("SELECT key, value FROM meta"))["source_root"]
        con.close()
        _, version = check_source_root(root)
        self.assertGreaterEqual(version, (2, 5, 0))


# ---------------------------------------------------------------------------
# Index integrity
# ---------------------------------------------------------------------------

@needs_index
class IndexIntegrity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.con = open_db()

    @classmethod
    def tearDownClass(cls):
        cls.con.close()

    def count(self, sql, *params):
        return self.con.execute(sql, params).fetchone()[0]

    def test_sanity_minimums(self):
        from gplates_index import indexer
        problems = indexer.verify_stats(indexer.collect_stats(self.con))
        self.assertEqual(problems, [])

    def test_no_orphan_rows(self):
        for table in ("symbols", "includes", "lines", "ui_forms", "ui_widgets",
                      "qt_connections", "py_api"):
            orphans = self.count(
                "SELECT COUNT(*) FROM %s t LEFT JOIN files f ON f.id = t.file_id "
                "WHERE f.id IS NULL" % table)
            self.assertEqual(orphans, 0, table)

    def test_no_duplicate_qualified_symbols(self):
        """ctags' `qualified` extra used to emit a second tag whose name repeats its scope."""
        doubled = self.count(
            "SELECT COUNT(*) FROM symbols WHERE scope IS NOT NULL AND name LIKE scope || '::%'")
        self.assertEqual(doubled, 0)

    def test_line_counts_match_files(self):
        bad = self.count(
            "SELECT COUNT(*) FROM files f WHERE f.has_text = 1 AND f.lines <> "
            "(SELECT COUNT(*) FROM lines l WHERE l.file_id = f.id)")
        self.assertEqual(bad, 0)

    def test_fts_agrees_with_lines(self):
        self.assertEqual(self.count("SELECT COUNT(*) FROM lines_fts"),
                         self.count("SELECT COUNT(*) FROM lines"))

    def test_known_landmarks_present(self):
        landmarks = [
            ("SELECT COUNT(*) FROM files WHERE path = 'src/gplates_main.cc'", 1),
            ("SELECT COUNT(*) FROM symbols WHERE name = 'ReconstructionTree' "
             "AND kind = 'class'", 1),
            ("SELECT COUNT(*) FROM symbols WHERE scope LIKE 'GPlatesMaths%'", 100),
            ("SELECT COUNT(*) FROM ui_forms WHERE class_name = 'ViewportWindow'", 1),
            ("SELECT COUNT(*) FROM gpgim_features WHERE name = 'gpml:Isochron'", 1),
        ]
        for sql, minimum in landmarks:
            self.assertGreaterEqual(self.count(sql), minimum, sql)

    def test_include_resolution(self):
        resolved = self.count("SELECT COUNT(*) FROM includes WHERE target_id IS NOT NULL")
        local = self.count("SELECT COUNT(*) FROM includes WHERE is_system = 0")
        self.assertGreater(resolved, local * 0.8,
                           "most quoted includes should resolve to in-tree headers")

    def test_gpgim_links_reference_known_names(self):
        unknown = self.count(
            "SELECT COUNT(*) FROM gpgim_feature_properties fp "
            "WHERE NOT EXISTS (SELECT 1 FROM gpgim_properties p WHERE p.name = fp.property)")
        self.assertEqual(unknown, 0)


# ---------------------------------------------------------------------------
# gpq command-line behaviour
# ---------------------------------------------------------------------------

@needs_index
class Queries(unittest.TestCase):

    def test_info(self):
        rc, out, err = gpq("info")
        self.assertEqual(rc, 0, err)
        self.assertIn("GPlates 2.", out)
        self.assertIn("src/app-logic", out)

    def test_sym_exact(self):
        rc, out, _ = gpq("sym", "ReconstructionTree", "--kind", "class")
        self.assertEqual(rc, 0)
        self.assertIn("[exact]", out)
        self.assertTrue(any("src/app-logic/ReconstructionTree.h" in h for h in hits(out)))

    def test_sym_widens_to_prefix(self):
        """No class is called exactly `ReconstructLayer`, so auto mode widens to prefix."""
        rc, out, _ = gpq("sym", "ReconstructLayer", "--kind", "class", "--limit", "60")
        self.assertEqual(rc, 0)
        self.assertIn("[prefix]", out)
        self.assertTrue(any("ReconstructLayerProxy" in h for h in hits(out)))

    def test_sym_widens_to_substring(self):
        """`olygonMesh` matches neither exactly nor as a prefix."""
        rc, out, _ = gpq("sym", "olygonMesh", "--kind", "class", "--limit", "60")
        self.assertEqual(rc, 0)
        self.assertIn("[sub]", out)
        self.assertTrue(any("PolygonMesh" in h for h in hits(out)))

    def test_sym_auto_prefers_exact(self):
        rc, out, _ = gpq("sym", "LayerProxy", "--kind", "class", "--limit", "60")
        self.assertEqual(rc, 0)
        self.assertIn("[exact]", out)
        for h in hits(out):
            self.assertRegex(h, r"(^|::)LayerProxy  ")

    def test_sym_regex_mode(self):
        rc, out, _ = gpq("sym", "^Reconstruct.*LayerProxy$", "--mode", "regex",
                         "--kind", "class")
        self.assertEqual(rc, 0)
        self.assertTrue(hits(out))
        for h in hits(out):
            self.assertIn("LayerProxy", h)

    def test_sym_unknown_name_exits_nonzero(self):
        rc, out, _ = gpq("sym", "ZzNotARealSymbolZz")
        self.assertEqual(rc, 1)
        self.assertIn("no symbol matches", out)

    def test_sym_limit_is_respected(self):
        rc, out, _ = gpq("sym", "Reconstruct", "--mode", "sub", "--limit", "7")
        self.assertEqual(rc, 0)
        self.assertLessEqual(len(hits(out)), 7)

    def test_global_and_subcommand_option_positions_agree(self):
        _, a, _ = gpq("--limit", "5", "sym", "Reconstruct", "--mode", "sub")
        _, b, _ = gpq("sym", "Reconstruct", "--mode", "sub", "--limit", "5")
        self.assertEqual(a, b)

    def test_def_body(self):
        rc, out, _ = gpq("def", "ReconstructionTree", "--kind", "class", "--body",
                         "--limit", "1")
        self.assertEqual(rc, 0)
        body = [h for h in hits(out) if h.startswith("src/app-logic/ReconstructionTree.h:")]
        self.assertGreater(len(body), 10)

    def test_grep_fts(self):
        rc, out, _ = gpq("grep", "anchor plate", "--path", "src/app-logic")
        self.assertEqual(rc, 0)
        self.assertTrue(hits(out))
        for h in hits(out):
            self.assertTrue(h.startswith("src/app-logic/"), h)

    def test_grep_regex(self):
        rc, out, _ = gpq("grep", r"class\s+ReconstructionTree\b", "--regex")
        self.assertEqual(rc, 0)
        self.assertTrue(any("ReconstructionTree" in h for h in hits(out)))

    def test_grep_bad_regex_reports_cleanly(self):
        rc, out, _ = gpq("grep", "([unclosed", "--regex")
        self.assertEqual(rc, 2)
        self.assertIn("bad regex", out)

    def test_grep_ranks_code_above_prose(self):
        rc, out, _ = gpq("grep", "anchored plate", "--limit", "5")
        self.assertEqual(rc, 0)
        self.assertFalse(hits(out)[0].startswith("CHANGELOG"))

    def test_grep_category_filter(self):
        rc, out, _ = gpq("grep", "isosurface", "--category", "shader")
        self.assertEqual(rc, 0)
        for h in hits(out):
            self.assertIn(".glsl", h)

    def test_refs(self):
        rc, out, _ = gpq("refs", "reconstruct_feature_geometries", "--limit", "30")
        self.assertEqual(rc, 0)
        self.assertTrue(any("[def " in h for h in hits(out)))
        self.assertTrue(any("[def " not in h for h in hits(out)))

    def test_file_outline(self):
        rc, out, _ = gpq("file", "src/app-logic/ReconstructUtils.h", "--limit", "80")
        self.assertEqual(rc, 0)
        self.assertIn("namespace", out)
        for h in hits(out):
            self.assertTrue(h.startswith("src/app-logic/ReconstructUtils.h:"), h)

    def test_file_range(self):
        rc, out, _ = gpq("file", "src/app-logic/ReconstructUtils.h", "--range", "60-64")
        self.assertEqual(rc, 0)
        self.assertEqual(len(hits(out)), 5)

    def test_file_ambiguous_lists_candidates(self):
        rc, out, _ = gpq("file", "ReconstructUtils")
        self.assertEqual(rc, 0)
        self.assertGreaterEqual(len(hits(out)), 2)

    def test_file_unknown_exits_nonzero(self):
        rc, out, _ = gpq("file", "no/such/file/at/all.cc")
        self.assertEqual(rc, 1)

    def test_tree(self):
        rc, out, _ = gpq("tree", "src", "--limit", "40")
        self.assertEqual(rc, 0)
        self.assertTrue(any(h.startswith("src/app-logic") for h in hits(out)))

    def test_includes_forward_and_reverse(self):
        rc, out, _ = gpq("includes", "src/app-logic/ReconstructUtils.h")
        self.assertEqual(rc, 0)
        self.assertTrue(hits(out))
        rc, out, _ = gpq("includes", "src/app-logic/ReconstructionTree.h", "--by")
        self.assertEqual(rc, 0)
        self.assertTrue(hits(out))

    def test_hier_ctags_fallback(self):
        rc, out, _ = gpq("hier-ctags", "LayerProxy", "--limit", "40")
        self.assertEqual(rc, 0)
        self.assertTrue(any("sub: " in h for h in hits(out)))
        for h in hits(out):
            self.assertNotIn("::GPlatesAppLogic::GPlatesAppLogic", h)

    def test_ui_form_lists_its_widgets(self):
        rc, out, _ = gpq("ui", "TotalReconstructionPoles", "--limit", "40")
        self.assertEqual(rc, 0)
        self.assertIn("TotalReconstructionPolesDialog", out)
        self.assertTrue(any("QTableWidget" in h for h in hits(out)))

    def test_signals(self):
        rc, out, _ = gpq("signals", "reconstruction_time_changed")
        self.assertEqual(rc, 0)
        self.assertTrue(any(" -> " in h for h in hits(out)))

    def test_pyapi(self):
        rc, out, _ = gpq("pyapi", "Feature", "--limit", "40")
        self.assertEqual(rc, 0)
        self.assertTrue(any("src/api/" in h for h in hits(out)))

    def test_gpgim_detail(self):
        rc, out, _ = gpq("gpgim", "Isochron", "--detail")
        self.assertEqual(rc, 0)
        self.assertIn("gpml:Isochron", out)
        self.assertIn("properties:", out)

    def test_gpgim_property_lookup(self):
        rc, out, _ = gpq("gpgim", "reconstructionPlateId", "--detail")
        self.assertEqual(rc, 0)
        self.assertTrue(any(h.startswith("property ") for h in hits(out)))

    def test_json_output_is_parseable(self):
        rc, out, _ = gpq("sym", "ReconstructionTree", "--kind", "class", "--json")
        self.assertEqual(rc, 0)
        rows = json.loads(out)
        self.assertTrue(rows)
        self.assertIn("path", rows[0])

    def test_sql_escape_hatch(self):
        rc, out, _ = gpq("sql", "SELECT COUNT(*) FROM symbols WHERE kind = 'class'")
        self.assertEqual(rc, 0)
        self.assertGreater(int(hits(out)[0]), 1000)

    def test_sql_write_is_refused(self):
        rc, _, err = gpq("sql", "DELETE FROM symbols")
        self.assertNotEqual(rc, 0)
        self.assertIn("readonly", err.lower())



# ---------------------------------------------------------------------------
# Deep C++ parsing (no index required)
# ---------------------------------------------------------------------------

try:
    from gplates_index import cpp_parse, cpp_extract
    from gplates_index.resolve import base_key
    cpp_parse.ensure_parser()
    HAVE_TS = True
except Exception:  # noqa: BLE001 - tree-sitter is optional until setup runs
    HAVE_TS = False

needs_ts = unittest.skipUnless(HAVE_TS, "tree-sitter not installed - run setup_index.py")

SAMPLE = b"""#define MAX_PLATES 512
#define SQR(x) ((x)*(x))
namespace GPlatesAppLogic {
    template<typename T, int N>
    class Cache : public Base<T>, private boost::noncopyable {
    public:
        typedef std::vector<T> seq_type;
        enum Mode { FAST, SLOW };
        explicit Cache(int n);
        int size() const;
    private:
        seq_type d_items;
    };
    int Cache::size() const {
        int local_n = d_items.size();
        d_ratio = local_n * SQR(2);
        return compute(local_n, MAX_PLATES);
    }
}
"""


def parse_sample(src=SAMPLE):
    data = cpp_parse.prepare(src)
    tree = cpp_parse.parse(data)
    sink = cpp_extract.Sink()
    cpp_extract.extract_entities(data, tree, sink)
    return data, tree, sink


@needs_ts
class Preprocessing(unittest.TestCase):
    """The Qt/preprocessor transforms must never move a byte or a line."""

    QT = b"""class Foo : public QObject {
    Q_OBJECT
public slots:
    void handle();
signals:
    void changed(const double &t);
private:
    int d_x;
};
void wire() {
    QObject::connect(a, SIGNAL(changed(const double &)), b, SLOT(handle()));
}
"""

    def test_length_and_lines_preserved(self):
        for src in (SAMPLE, self.QT):
            out = cpp_parse.prepare(src)
            self.assertEqual(len(out), len(src))
            self.assertEqual(out.count(b"\n"), src.count(b"\n"))

    def test_qt_macros_removed(self):
        out = cpp_parse.neutralise_qt(self.QT)
        self.assertNotIn(b"Q_OBJECT", out)
        self.assertNotIn(b"signals:", out)
        self.assertIn(b"public:", out)

    def test_qt_class_parses_cleanly(self):
        raw_err = cpp_parse.error_extent(cpp_parse.parse(self.QT))
        fixed_err = cpp_parse.error_extent(cpp_parse.parse(cpp_parse.prepare(self.QT)))
        self.assertGreater(raw_err, 0, "the raw Qt sample should confuse the parser")
        self.assertEqual(fixed_err, 0, "preparation should make it parse cleanly")

    def test_if_else_branch_selected(self):
        src = b"""int f()
{
#if defined(USE_A)
    return 1;
#else
    return 2;
#endif
}
"""
        out = cpp_parse.select_branches(src)
        self.assertIn(b"return 1;", out)
        self.assertNotIn(b"return 2;", out)
        self.assertEqual(len(out), len(src))

    def test_if_zero_body_removed(self):
        src = b'#if 0\nbroken ( syntax\n#else\nint ok = 1;\n#endif\n'
        out = cpp_parse.select_branches(src)
        self.assertNotIn(b"broken", out)
        self.assertIn(b"int ok = 1;", out)

    def test_include_guard_survives(self):
        src = b'#ifndef GUARD_H\n#define GUARD_H\nint kept = 1;\n#endif\n'
        out = cpp_parse.select_branches(src)
        self.assertIn(b"int kept = 1;", out)


@needs_ts
class DeepExtraction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data, cls.tree, cls.sink = parse_sample()
        cls.by_qname = {e["qname"]: e for e in cls.sink.entities}

    def test_no_parse_errors_in_sample(self):
        self.assertEqual(cpp_parse.error_extent(self.tree), 0)

    def test_macros(self):
        self.assertEqual(self.by_qname["MAX_PLATES"]["kind"], "macro")
        sqr = self.by_qname["SQR"]
        self.assertEqual(sqr["kind"], "macro_function")
        self.assertEqual(sqr["signature"], "(x)")
        self.assertIn("(x)*(x)", sqr["type_text"])

    def test_class_and_template(self):
        cache = self.by_qname["GPlatesAppLogic::Cache"]
        self.assertEqual(cache["kind"], "class")
        self.assertEqual(cache["is_template"], 1)
        self.assertIn("typename T", cache["template_params"])

    def test_bases_recorded_with_access(self):
        got = {name: access for _, name, access, _ in self.sink.bases}
        self.assertEqual(got.get("Base<T>"), "public")
        self.assertEqual(got.get("boost::noncopyable"), "private")

    def test_declaration_and_definition_are_distinct(self):
        sizes = [e for e in self.sink.entities
                 if e["qname"] == "GPlatesAppLogic::Cache::size"]
        self.assertEqual(len(sizes), 2)
        self.assertEqual({e["is_def"] for e in sizes}, {0, 1})

    def test_member_field_has_type_and_access(self):
        field = self.by_qname["GPlatesAppLogic::Cache::d_items"]
        self.assertEqual(field["kind"], "field")
        self.assertEqual(field["type_text"], "seq_type")
        self.assertEqual(field["access"], "private")

    def test_no_phantom_entity_named_after_its_own_type(self):
        """A tree-sitter identity-comparison bug used to emit `Cache::int`."""
        for e in self.sink.entities:
            if e["type_text"]:
                self.assertNotEqual(e["name"], e["type_text"], e["qname"])

    def test_typedef_enum_and_enumerators(self):
        self.assertEqual(self.by_qname["GPlatesAppLogic::Cache::seq_type"]["kind"], "typedef")
        self.assertEqual(self.by_qname["GPlatesAppLogic::Cache::Mode"]["kind"], "enum")
        self.assertIn("GPlatesAppLogic::Cache::Mode::FAST", self.by_qname)

    def test_parameters_and_locals(self):
        kinds = {e["kind"] for e in self.sink.entities}
        self.assertIn("parameter", kinds)
        self.assertIn("local", kinds)

    def test_occurrence_roles(self):
        known = {e["name"] for e in self.sink.entities}
        sink = cpp_extract.Sink()
        cpp_extract.extract_occurrences(self.data, self.tree, sink, known)
        roles = {(name, role) for _, _, name, role in sink.occurrences}
        self.assertIn(("SQR", "call"), roles)
        self.assertIn(("MAX_PLATES", "read"), roles)
        self.assertIn(("d_items", "read"), roles)
        self.assertIn(("size", "call"), roles)

    def test_base_key_normalisation(self):
        self.assertEqual(base_key("GPlatesUtils::ReferenceCount<Foo>"), "ReferenceCount")
        self.assertEqual(base_key("boost::noncopyable"), "noncopyable")
        self.assertEqual(base_key("Base<T>"), "Base")


# ---------------------------------------------------------------------------
# Deep index integrity
# ---------------------------------------------------------------------------

@needs_index
class DeepIndexIntegrity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.con = open_db()

    @classmethod
    def tearDownClass(cls):
        cls.con.close()

    def count(self, sql, *params):
        return self.con.execute(sql, params).fetchone()[0]

    def test_entities_cover_every_kind_asked_for(self):
        kinds = {r[0] for r in self.con.execute("SELECT DISTINCT kind FROM entities")}
        for required in ("class", "struct", "enum", "enumerator", "typedef", "method",
                         "function", "constructor", "destructor", "field", "variable",
                         "parameter", "local", "macro", "macro_function", "namespace"):
            self.assertIn(required, kinds)

    def test_no_orphan_deep_rows(self):
        self.assertEqual(self.count(
            "SELECT COUNT(*) FROM entities e LEFT JOIN files f ON f.id = e.file_id "
            "WHERE f.id IS NULL"), 0)
        self.assertEqual(self.count(
            "SELECT COUNT(*) FROM occurrences o LEFT JOIN files f ON f.id = o.file_id "
            "WHERE f.id IS NULL"), 0)
        self.assertEqual(self.count(
            "SELECT COUNT(*) FROM entities c LEFT JOIN entities p ON p.id = c.parent_id "
            "WHERE c.parent_id IS NOT NULL AND p.id IS NULL"), 0)

    def test_occurrence_targets_exist(self):
        self.assertEqual(self.count(
            "SELECT COUNT(*) FROM occurrences o LEFT JOIN entities e ON e.id = o.entity_id "
            "WHERE o.entity_id IS NOT NULL AND e.id IS NULL"), 0)

    def test_resolution_rate(self):
        total = self.count("SELECT COUNT(*) FROM occurrences")
        resolved = self.count("SELECT COUNT(*) FROM occurrences WHERE entity_id IS NOT NULL")
        self.assertGreater(resolved / total, 0.80,
                           "expected most occurrences to bind to an entity")

    def test_every_occurrence_has_a_confidence(self):
        self.assertEqual(self.count(
            "SELECT COUNT(*) FROM occurrences WHERE confidence IS NULL"), 0)

    def test_closure_is_sane(self):
        self.assertEqual(self.count(
            "SELECT COUNT(*) FROM inherit_closure WHERE ancestor_id = descendant_id"), 0,
            "inheritance closure must not contain cycles through self")
        self.assertEqual(self.count(
            "SELECT COUNT(*) FROM inherit_closure WHERE depth < 1"), 0)

    def test_closure_contains_direct_edges(self):
        direct = self.count(
            "SELECT COUNT(*) FROM bases WHERE base_entity_id IS NOT NULL "
            "AND entity_id <> base_entity_id")
        depth1 = self.count("SELECT COUNT(*) FROM inherit_closure WHERE depth = 1")
        self.assertGreaterEqual(depth1, direct * 0.9)

    def test_known_hierarchy(self):
        """ReconstructLayerProxy -> LayerProxy -> LayerProxyHandle -> ReferenceCount."""
        chain = self.con.execute(
            "SELECT a.qname, c.depth FROM inherit_closure c "
            "JOIN entities a ON a.id = c.ancestor_id "
            "JOIN entities d ON d.id = c.descendant_id "
            "WHERE d.qname = 'GPlatesAppLogic::ReconstructLayerProxy' ORDER BY c.depth"
        ).fetchall()
        names = [r[0] for r in chain]
        self.assertIn("GPlatesAppLogic::LayerProxy", names)
        self.assertIn("GPlatesUtils::ReferenceCount", names)

    def test_unresolved_bases_are_external(self):
        """Anything left unresolved should be a Qt/Boost/std type, not GPlates code."""
        rows = self.con.execute(
            "SELECT base_key, COUNT(*) c FROM bases WHERE base_entity_id IS NULL "
            "GROUP BY base_key ORDER BY c DESC LIMIT 10").fetchall()
        for key, _ in rows:
            self.assertFalse(key.startswith("GPlates"),
                             "in-tree base %r should have resolved" % key)


# ---------------------------------------------------------------------------
# Deep index queries
# ---------------------------------------------------------------------------

@needs_index
class DeepQueries(unittest.TestCase):

    def test_decl_separates_declaration_from_definition(self):
        rc, out, _ = gpq("decl", "ReconstructionTree", "--kind", "class", "--limit", "30")
        self.assertEqual(rc, 0)
        self.assertTrue(any(h.endswith("(def)") for h in hits(out)))
        self.assertTrue(any(h.endswith("(decl)") for h in hits(out)))

    def test_decl_finds_a_macro(self):
        rc, out, _ = gpq("decl", "GPLATES_ASSERTION_SOURCE")
        self.assertEqual(rc, 0)
        self.assertIn("macro", out)

    def test_decl_unknown_exits_nonzero(self):
        rc, _, _ = gpq("decl", "ZzNoSuchEntityZz")
        self.assertEqual(rc, 1)

    def test_uses_reports_roles(self):
        rc, out, _ = gpq("uses", "d_anchor_plate_id", "--limit", "40")
        self.assertEqual(rc, 0)
        self.assertIn("usages by role:", out)
        self.assertTrue(any(" read " in h or " member " in h for h in hits(out)))

    def test_uses_role_filter(self):
        rc, out, _ = gpq("uses", "get_anchor_plate_id", "--role", "call", "--limit", "20")
        self.assertEqual(rc, 0)
        for h in hits(out):
            self.assertIn("call", h)

    def test_uses_of_a_type(self):
        rc, out, _ = gpq("uses", "ReconstructionTree", "--kind", "class",
                         "--role", "type", "--limit", "20")
        self.assertEqual(rc, 0)
        self.assertTrue(hits(out))

    def test_hier_is_transitive_both_ways(self):
        rc, up, _ = gpq("hier", "ReconstructLayerProxy", "--up")
        self.assertEqual(rc, 0)
        self.assertTrue(any("base d2" in h or "base d3" in h for h in hits(up)),
                        "expected an indirect base class")
        rc, down, _ = gpq("hier", "ReferenceCount", "--down", "--limit", "200")
        self.assertEqual(rc, 0)
        self.assertTrue(any("sub  d2" in h for h in hits(down)),
                        "expected an indirect subclass")

    def test_hier_depth_limit(self):
        rc, out, _ = gpq("hier", "ReferenceCount", "--down", "--depth", "1", "--limit", "200")
        self.assertEqual(rc, 0)
        for h in hits(out):
            if h.strip().startswith("sub"):
                self.assertIn("sub  d1", h)

    def test_members_filters_members_not_the_container(self):
        """`--kind field` must narrow the members, not the class lookup."""
        rc, out, _ = gpq("members", "ReconstructionTree", "--kind", "field", "--limit", "40")
        self.assertEqual(rc, 0)
        body = [h for h in hits(out) if h.strip()]
        self.assertTrue(body)
        for h in body:
            self.assertIn("field", h)

    def test_members_access_filter(self):
        rc, out, _ = gpq("members", "ReconstructionTree", "--kind", "method",
                         "--access", "public", "--limit", "40")
        self.assertEqual(rc, 0)
        for h in hits(out):
            self.assertIn("[public]", h)

    def test_members_of_a_namespace(self):
        rc, out, _ = gpq("members", "GPlatesMaths", "--kind", "class", "--limit", "20")
        self.assertEqual(rc, 0)
        self.assertTrue(hits(out))

    def test_macro_lists_uses(self):
        rc, out, _ = gpq("macro", "GPLATES_ASSERTION_SOURCE", "--uses", "--limit", "10")
        self.assertEqual(rc, 0)
        self.assertTrue(any(".cc:" in h or ".h:" in h for h in hits(out)))

    def test_deep_json_output(self):
        rc, out, _ = gpq("decl", "ReconstructionTree", "--kind", "class", "--json")
        self.assertEqual(rc, 0)
        rows = json.loads(out)
        self.assertTrue(rows)
        self.assertIn("qname", rows[0])

if __name__ == "__main__":
    if not HAVE_INDEX:
        print("warning: no index at %s - only unit tests will run\n"
              "         build one with: python scripts/setup_index.py --source <DIR>\n"
              % DB_PATH, file=sys.stderr)
    unittest.main(verbosity=2)
