import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/check_html.py'


class HtmlChecks(unittest.TestCase):
    def inspect(self, content):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'test.html'
            path.write_text(content, encoding='utf-8')
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)['files'][0]['findings']

    def test_candidates_have_bounded_outcomes_and_lines(self):
        findings = self.inspect('<html><head><title></title></head><body>\n<img src="x">\n<button aria-hidden="true">Save</button></body></html>')
        self.assertEqual({x['rule'] for x in findings}, {'AV-LNG-001', 'AV-IMG-001', 'AV-HID-001', 'AV-TIT-001'})
        self.assertTrue(all(x['outcome'] == 'NEEDS_REVIEW' for x in findings))
        self.assertEqual(next(x for x in findings if x['rule'] == 'AV-IMG-001')['line'], 2)

    def test_fragment_and_valid_alternatives_not_invented_as_failures(self):
        self.assertEqual(self.inspect('<img alt="" src="divider.svg"><button disabled aria-hidden="true">Save</button>'), [])
        self.assertEqual(self.inspect('<html lang="en"><head><title>Account</title></head><body><img alt="Profile" src="x"></body></html>'), [])

    def test_unreadable_input_exits_with_error(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '/not/a/real/file.html'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, '')


if __name__ == '__main__':
    unittest.main()
