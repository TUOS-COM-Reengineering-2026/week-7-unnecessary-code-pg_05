import unittest
import os
from code_clones import visualise_dot_plot

class MyTestCase(unittest.TestCase):
    def test_visualise_dot_plot_simples(self):
        base_dir = os.path.dirname(__file__)
        a = os.path.join(base_dir, 'resources', 'simple1.py')
        b = os.path.join(base_dir, 'resources', 'simple2.py')
        plot = '''--------------------------------------------------------------------------------
x0: def calculate_total(values: list):
x1:     total = 0
x2:     for value in values:
x3:         if value < 0:
x4:             continue
x5:         total += value
x6:     return total
--------------------------------------------------------------------------------
y0: def calculate_total(values: list):
y1:     total = 0
y2:     for value in values:
y3:         if value < 0:
y4:             print("Negative value!")
y5:             continue
y6:         total += value
y7:     return total
--------------------------------------------------------------------------------
	x0	x1	x2	x3	x4	x5	x6	
y0	*	 	 	 	 	 	 	
y1	 	*	 	 	 	 	 	
y2	 	 	*	 	 	 	 	
y3	 	 	 	*	 	 	 	
y4	 	 	 	 	 	 	 	
y5	 	 	 	 	*	 	 	
y6	 	 	 	 	 	*	 	
y7	 	 	 	 	 	 	*	
--------------------------------------------------------------------------------'''
        self.assertEqual(visualise_dot_plot(a, b), plot)


    def test_visualise_dot_plot_programs(self):
        base_dir = os.path.dirname(__file__)
        a = os.path.join(base_dir, 'resources', 'program1.py')
        b = os.path.join(base_dir, 'resources', 'program2.py')
        plot = '''--------------------------------------------------------------------------------
x0: def is_palindrome(s):
x1:     if len(s) == 0:
x2:         return True
x3:     elif s[0] != s[-1]:
x4:         return False
x5:     elif len(s) <= 1:
x6:         return True
x7:     else:
x8:         return is_palindrome(s[1:-1])
--------------------------------------------------------------------------------
y0: def is_palindrome(s):
y1:     if len(s) <= 1:
y2:         return True
y3:     elif s[0] != s[-1]:
y4:         return False
y5:     else:
y6:         return is_palindrome(s[1:-1])
--------------------------------------------------------------------------------
	x0	x1	x2	x3	x4	x5	x6	x7	x8	
y0	*	 	 	 	 	 	 	 	 	
y1	 	 	 	 	 	 	 	 	 	
y2	 	 	*	 	 	 	*	 	 	
y3	 	 	 	*	 	 	 	 	 	
y4	 	 	 	 	*	 	 	 	 	
y5	 	 	 	 	 	 	 	*	 	
y6	 	 	 	 	 	 	 	 	*	
--------------------------------------------------------------------------------'''

        self.assertEqual(visualise_dot_plot(a, b), plot)