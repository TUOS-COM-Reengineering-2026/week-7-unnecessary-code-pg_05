import unittest
from tests.resources import program2, program1


class MyTestCase(unittest.TestCase):
    def test_programs1(self):
        s = 'hello world'
        self.assertEqual(program1.is_palindrome(s), program2.is_palindrome(s))  # add assertion here

    def test_programs2(self):
        s = '11111'
        self.assertEqual(program1.is_palindrome(s), program2.is_palindrome(s))  # add assertion here

    def test_programs3(self):
        s = '01111'
        self.assertEqual(program1.is_palindrome(s), program2.is_palindrome(s))  # add assertion here

    def test_programs4(self):
        s = ''
        self.assertEqual(program1.is_palindrome(s), program2.is_palindrome(s))  # add assertion here

if __name__ == '__main__':
    unittest.main()
