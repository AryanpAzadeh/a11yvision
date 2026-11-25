import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/rules.py'


class RuleToolTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'references/rules', self.root / 'references/rules')
        shutil.copytree(ROOT / 'schemas', self.root / 'schemas')

    def tearDown(self):
        self.temp.cleanup()

    def run_tool(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), '--root', str(self.root), *args],
                              text=True, capture_output=True)

    def rule(self):
        return self.root / 'references/rules/images-media/AV-IMG-001.md'

    def test_valid_and_deterministic_manifest(self):
        self.assertEqual(self.run_tool('validate').returncode, 0)
        first = self.run_tool('manifest')
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, self.run_tool('manifest').stdout)
        self.assertEqual(len(json.loads(first.stdout)['rules']), 43)
        target = self.root / 'manifest.json'
        target.write_text(first.stdout)
        self.assertEqual(self.run_tool('manifest', '--check', str(target)).returncode, 0)
        target.write_text('{}')
        self.assertNotEqual(self.run_tool('manifest', '--check', str(target)).returncode, 0)

    def test_schema_and_section_errors(self):
        p = self.rule()
        text = p.read_text().replace('scope: "conformance"', 'scope: "incorrect"')
        p.write_text(text.replace('## User impact', '## Impact'))
        result = self.run_tool('validate')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('scope', result.stderr)
        self.assertIn('required sections', result.stderr)

    def test_missing_rule_and_duplicate_yaml_key(self):
        p = self.rule()
        p.write_text(p.read_text().replace('status: "active"', 'status: "active"\nstatus: "draft"'))
        result = self.run_tool('manifest')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')
        self.assertIn('duplicate YAML key', result.stderr)
        self.assertIn('missing rule: AV-IMG-001', result.stderr)

    def test_duplicate_id_and_unexpected_file(self):
        source = self.rule()
        (source.parent / 'duplicate.md').write_text(source.read_text())
        result = self.run_tool('validate')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('duplicate ID', result.stderr)
        self.assertIn('filename must match', result.stderr)


if __name__ == '__main__':
    unittest.main()
