# This is my Python solution for part 1 of day 2 of AOC.
import os
from typing import Dict
from icecream import ic

# If you don't have a conda environment or didn't set up the .env file,
# you can just replace this with the path to the text file.
file_path = os.getenv("day2textfile")
if file_path is None:
    # Example, replace ... with actual path, check using pwd
    file_path = "/home/.../adventofcode/resources/day1.txt"


def separate_objects(games: list[str]) -> int:
    outer_temp_: dict[str, int] = {
        "total_games": 0
    }
    for game in games:
        temp_ = {

        }
        temp_["game"] = game.split(":")[0]
        temp_["cubes"] = game.split(":")[1]
        result = [n for n in temp_["cubes"].split(";")]
        add_game = True

        for item in result:
            colors = item.split(", ")
            red_count = 0
            green_count = 0
            blue_count = 0
            for color in colors:
                if "red" in color:
                    red_count += int(color.split()[0])
                    if red_count > 12:
                        add_game = False
                        continue
                elif "green" in color:
                    green_count += int(color.split()[0])
                    if green_count > 13:
                        add_game = False
                        continue
                elif "blue" in color:
                    blue_count += int(color.split()[0])
                    if blue_count > 14:
                        add_game = False
                        continue
        if add_game:
            gameID = int(temp_["game"].split(" ")[1])
            outer_temp_["total_games"] += gameID
    return outer_temp_["total_games"]


def get_data() -> list[str]:
    with open(file_path, "r") as f:
        games = f.readlines()
        temp_ = []
        for i in range(len(games)):
            temp_.append(games[i].rstrip('\n'))
        games = temp_
        del temp_
    return games


def main():
    data = get_data()
    separate_objects(data)


if __name__ == "__main__":
    main()
