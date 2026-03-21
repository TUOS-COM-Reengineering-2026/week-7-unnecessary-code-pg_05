import unittest
import os

class MyTestCase(unittest.TestCase):
    def test_dead_code(self):
        base_dir = os.path.dirname(__file__)
        with open(os.path.join(base_dir, '..', 'dead_code.py'), 'r') as f:
            code = f.read()
        self.assertEqual(code.strip(),
"""def example_function():
    x = 5
    return x""")
