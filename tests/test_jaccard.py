##### DO NOT MODIFY THIS FILE #####

import unittest
import os
from code_clones import compute_jaccard_similarity

class MyTestCase(unittest.TestCase):
    def test_jaccard_simples(self):
        base_dir = os.path.dirname(__file__)
        a = os.path.join(base_dir, 'resources', 'simple1.py')
        b = os.path.join(base_dir, 'resources', 'simple2.py')
        self.assertEqual(compute_jaccard_similarity(a, b), 7/8)

    def test_jaccard_programs(self):
        base_dir = os.path.dirname(__file__)
        a = os.path.join(base_dir, 'resources', 'program1.py')
        b = os.path.join(base_dir, 'resources', 'program2.py')
        self.assertEqual(compute_jaccard_similarity(a, b), 6/9)
