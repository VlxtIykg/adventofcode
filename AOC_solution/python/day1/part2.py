# This is my Python solution for part 2 of day 1 of AOC.
import os
from enum import Enum
from typing import LiteralString
from icecream import ic

file_path = os.getenv("day1textfile")

class Numbers(Enum):
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
    string (str): The input string.

  Returns:
    LiteralString: A string representation of the numbers associated with the input string.
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

def get_required_number(string: str | int | None):
  """
  Calculates the sum of the first and last characters of the given string.

  Args:
    string (str | int | None): The input string.

  Returns:
    The concatenation of the first and last characters of the string.
  """
  total = string[0] + string[-1]
  return total

def calculate_total():
  """
  Calculates the total by reading numbers from a file and applying number parsing logic.

  Returns:
    The calculated total.
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
