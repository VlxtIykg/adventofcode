# This is my Python solution for part 2 of day 1 of AOC.
import os
from enum import Enum
from typing import LiteralString
from icecream import ic

file_path = os.getenv("day1textfile") # If you don't have a conda environment or didn't set up the .env file, you can just replace this with the path to the text file.
if file_path is None:
    file_path = "/home/.../adventofcode/resources/day1.txt" # Example, replace ... with actual path, check using pwd

class Numbers(Enum):
    """
    An enumeration of numbers for indexing purposes.

    Accessible as follows:

    - attribute access:

      >>> Numbers.one
      <Numbers.one: '1'>

    - value lookup:

      >>> Numbers("1")
      <Numbers.one: '1'>

    - inheritance:
      
      >>> Numbers.mro()
      [<enum 'Numbers'>, <enum 'Enum'>, <class 'object'>] # Idk why u need this but it's cool

    Indexing:

    Most efficient:
      >>> for i in Numbers:
      >>>   print(i.name)
      "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
      >>>        print(i.value)
      1, 2, 3, 4, 5, 6, 7, 8, 9
    Managable:
      >>> for i in list(Numbers):
      >>>   print(i.name) 
      "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
      >>>        print(i.value)
      1, 2, 3, 4, 5, 6, 7, 8, 9
    Brute force from length of enumeration:
      >>> for i in range(1, len(Numbers) + 1):
      >>>   print(Numbers(str(i)).name) # one, two, three, four, five, six, seven, eight, nine
      # 
      # or            
      # 
      >>> for i in range(len(Numbers)):
      >>>   if i == 4 and "four" == Numbers.four.name and "4" == Numbers.four.value:
      >>>     print(Numbers.four.name)
      "four"
      >>>     print(Numbers.four.value)
      4


    """
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"


def get_number_from_enum(string: str) -> LiteralString:
    """
    Returns a string representation of the numbers associated with the given string.

    Args:
      string (str): The string form of the numeric number.

    Returns:
      LiteralString: A string representation of the numbers associated with the input string.

    Example:
      
    >>> number = get_number_from_enum("nine")
    >>> print(number)
    9
    """
    temp = []
    for key in Numbers:
        if string.startswith(key.name):
            temp.append(key.value)
    return "".join(temp)


def number_parsing_logic(string: str) -> LiteralString:
    """
    Parses a string and replaces characters with corresponding numbers based on an enumeration.

    Args:
      string (str): The input string to be parsed.

    Returns:
      LiteralString: A list of numbers joined as a string.
    
    >>> number = number_parsing_logic("one two three four five six seven eight nine")
    >>> print(number)
    123456789
    """
    temp = []
    tempchar = ""
    for idx, item in enumerate(string):
        if item.isdigit():
            temp.append(item)
        else:
            tempchar = tempchar + item
            number = get_number_from_enum(string[idx:])
            temp.append(number)
    return "".join(temp)


def get_required_number(string: str):
    """
    Calculates the sum of the first and last characters of the given string.

    Args:
      string (str | int | None): The input string.

    Returns:
      The concatenation of the first and last characters of the string.

    >>> number = get_required_number("123456789")
    >>> print(number)
    19
    """
    total = string[0] + string[-1]
    return total


def calculate_total():
    """
    Calculates the total by reading numbers from a file and applying number parsing logic.

    Returns:
      The calculated total.

    >>> total = calculate_total()
    >>> print(total)
    56324
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            text = number_parsing_logic(line)
            total += int(get_required_number(text))
        ic(total)


if __name__ == "__main__":
    calculate_total()
