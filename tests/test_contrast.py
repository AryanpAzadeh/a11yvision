import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/contrast.py'
spec = importlib.util.spec_from_file_location('contrast', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ContrastTests(unittest.TestCase):
    def test_known_ratios_and_symmetry(self):
        black, white = module.color('#000'), module.color('#ffffff')
        self.assertAlmostEqual(module.contrast(black, white), 21)
        self.assertEqual(module.contrast(white, black), module.contrast(black, white))
        self.assertAlmostEqual(module.contrast(white, white), 1)
        self.assertAlmostEqual(module.contrast(module.color('#aaa'), white), 2.323123, places=5)

    def test_near_threshold_never_rounds_up(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '#777', '#fff'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('normal text (4.5:1): below', result.stdout)
        self.assertIn('large text (3:1): meets', result.stdout)
        self.assertLess(module.contrast(module.color('#777'), module.color('#fff')), 4.5)

    def test_invalid_or_unresolved_colors_are_rejected(self):
        for value in ('#abcd', '#12345678', 'red', 'var(--text)', '#zzzzzz', '#12'):
            with self.subTest(value=value):
                result = subprocess.run([sys.executable, str(SCRIPT), value, '#fff'], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn('Contrast ratio:', result.stdout)


if __name__ == '__main__':
    unittest.main()
