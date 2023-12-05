from AOC_solution.python.day1.part1 import get_first_and_last_numbers
import unittest

class TestGetFirstAndLastNumbers(unittest.TestCase):
    def test_get_first_and_last_numbers(self):
        """ Test case 1: string with single digit numbers """
        input_string = "1 2 3 4 5"
        expected_output = 15
        self.assertEqual(
            get_first_and_last_numbers(input_string),
            expected_output)

        """ Test case 2: string with multi-digit numbers """
        input_string = "10 20 30 40 50"
        expected_output = 10
        self.assertEqual(
            get_first_and_last_numbers(input_string),
            expected_output)

        """ Test case 3: string with no numbers """
        input_string = "abc def ghi"
        expected_output = 0
        self.assertEqual(
            get_first_and_last_numbers(input_string),
            expected_output)

        """ Test case 4: string with special characters """
        input_string = "!@#$%^&*()_+"
        expected_output = 0
        self.assertEqual(
            get_first_and_last_numbers(input_string),
            expected_output)


if __name__ == '__main__':
    unittest.main()
