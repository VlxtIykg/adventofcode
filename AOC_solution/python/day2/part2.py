# This is my Python solution for part 2 of day 2 of AOC.
import os
import re
from icecream import ic
from functools import reduce
import operator

# If you don't have a conda environment or didn't set up the .env file,
# you can just replace this with the path to the text file.
file_path = os.getenv("day2textfile")
if file_path is None:
    # Example, replace ... with actual path, check using pwd
    file_path = "/home/.../adventofcode/resources/day1.txt"


def separate_objects(games: list[str]) -> int:
    total = 0
    for game in games:
        biggest_set = {"red": 0, "green": 0, "blue": 0}

        for sets in game.split(":"):
            if sets.startswith("Game"):
                continue
            # Convert semicolon to comma so that we can split on comma to have
            # 1 string to loop through
            sets = re.sub(";", ",", sets)
            # Remove trailing white spaces
            sets = sets.strip()
            # Loop through each color and count the number of cubes
            sets = sets.split(",")
            for color in sets:
                color = color.strip()
                (number, color) = color.split()
                number = int(number)
                if color == "blue" and biggest_set["blue"] < number:
                    biggest_set["blue"] = number
                    pass
                elif color == "green" and biggest_set["green"] < number:
                    biggest_set["green"] = number
                    pass
                elif color == "red" and biggest_set["red"] < number:
                    biggest_set["red"] = number
                    pass
                elif color == "blue" and biggest_set["blue"] == 0:
                    biggest_set["blue"] = number
                    pass
                elif color == "green" and biggest_set["green"] == 0:
                    biggest_set["green"] = number
                    pass
                elif color == "red" and biggest_set["red"] == 0:
                    biggest_set["red"] = number
                    pass
                pass

        # Add the biggest set to the total, separate stmt for readability
        result = reduce(operator.mul, biggest_set.values(), 1)
        total += result
    return total


def get_data() -> list[str]:
    with open(file_path, "r") as f:
        games = f.readlines()
        temp_ = []
        for i in range(len(games)):
            temp_.append(games[i].rstrip("\n"))
        games = temp_
        del temp_
    return games


def main():
    data = get_data()
    mnm_set = separate_objects(data)
    ic(mnm_set)


if __name__ == "__main__":
    main()
