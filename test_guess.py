import unittest
import random
import sys
import os

class TestGuessGame(unittest.TestCase):
    def setUp(self):
        self.original_stdin = sys.stdin
        sys.stdin = open('test_input.txt', 'r')
        self.original_stdout = sys.stdout
        sys.stdout = open('test_output.txt', 'w')

    def tearDown(self):
        sys.stdin = self.original_stdin
        sys.stdout = self.original_stdout
        os.remove('test_input.txt')
        os.remove('test_output.txt')

    def test_valid_guess(self):
        # Test when the user guesses the correct number on the first try
        with open('test_input.txt', 'w') as f:
            f.write('50\n')
        with open('test_input.txt', 'r') as f:
            random.seed(42)
            from guess import number
            self.assertEqual(number, 50)

    def test_too_low_guess(self):
        # Test when the user guesses too low
        with open('test_input.txt', 'w') as f:
            f.write('40\n45\n50\n')
        with open('test_input.txt', 'r') as f:
            random.seed(42)
            from guess import number
            self.assertEqual(number, 50)

    def test_too_high_guess(self):
        # Test when the user guesses too high
        with open('test_input.txt', 'w') as f:
            f.write('60\n55\n50\n')
        with open('test_input.txt', 'r') as f:
            random.seed(42)
            from guess import number
            self.assertEqual(number, 50)

    def test_invalid_input(self):
        # Test when the user enters non-integer input
        with open('test_input.txt', 'w') as f:
            f.write('abc\n10\n')
        with open('test_input.txt', 'r') as f:
            random.seed(42)
            from guess import number
            self.assertEqual(number, 50)

    def test_exhausted_attempts(self):
        # Test when the user runs out of attempts
        with open('test_input.txt', 'w') as f:
            f.write('1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n')
        with open('test_input.txt', 'r') as f:
            random.seed(42)
            from guess import number
            self.assertEqual(number, 50)

if __name__ == '__main__':
    unittest.main()