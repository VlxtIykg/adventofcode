import unittest
import sys
sys.path.append('./AOC_solution/python/day1/')
from part2 import number_parsing_logic, get_number_from_enum  # noqa: E402


class TestNumberParsingLogic(unittest.TestCase):
    def test_number_parsing_logic(self):
        # Test case 1: string with no characters to replace
        input_string = "12345"
        expected_output = "12345"
        self.assertEqual(number_parsing_logic(input_string), expected_output)

        # Test case 2: string with characters to replace
        input_string = "a1b2c3"
        expected_output = "123"
        self.assertEqual(number_parsing_logic(input_string), expected_output)

        # Test case 3: string with characters to replace
        input_string = "tmoneightzstdjqjncnkpkknzoneonethreefive7"
        expected_output = "1811357"
        self.assertEqual(number_parsing_logic(input_string), expected_output)

        # Test case 4: string with characters to replace
        input_string = "9vnxqtjjrsg"
        expected_output = "9"
        self.assertEqual(number_parsing_logic(input_string), expected_output)

    def test_number_from_enum(self):
        # Test case 5: string with characters to replace
        input_string = "7five2134"
        expected_output = ""
        self.assertEqual(get_number_from_enum(input_string), expected_output)

        # Test case 6: string with characters to replace
        input_string = "five2134"
        expected_output = "5"
        self.assertEqual(get_number_from_enum(input_string), expected_output)


if __name__ == '__main__':
    unittest.main()
