# This is my Python solution for part 1 of day 1 of AOC.
from icecream import ic
import re
import os

file_path = os.getenv("day1textfile") # If you don't have a conda environment or didn't set up the .env file, you can just replace this with the path to the text file.
if file_path is None:
    file_path = "/home/.../adventofcode/resources/day1.txt" # Example, replace ... with actual path, check using pwd

def get_first_and_last_numbers(string) -> tuple[int, int] | int:
    numbers = re.findall(pattern=r'\d+', string=string)
    compacted_numbers = "".join(numbers)
    if not compacted_numbers:
        return 0
    first_number = int(compacted_numbers[0])
    last_number = int(compacted_numbers[-1])
    concatenation = str(first_number) + str(last_number)
    return int(concatenation)


def read_file() -> None:
    with open(file_path, "r") as file:
        lines = file.readlines()
        temp_ = []
        for line in lines:
            temp_.append(get_first_and_last_numbers(line))

        lines = temp_
        print(lines)
        ic(sum(lines))


if __name__ == "__main__":
    read_file()
