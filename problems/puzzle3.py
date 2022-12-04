from helpers import time_it, load_text_file
from pathlib import Path
from rich import print
import os
import click

def puzzle1(data):
    """
    Given a list of priorities where the first half
    is of one elf and the other half is another, find
    the common priority and its score.
    """
    score_cum = 0
    for i in data:
        # transform string to list of chrs
        letter_list = list(i)
        # store middle position
        middle_pos = int(len(i)/2)
        # get intersection element of 2 lists
        distinct_element = set(i[:middle_pos]) & set(i[middle_pos:])
        distinct_element = distinct_element.pop()
        # get element value
        match distinct_element.islower():
            case True:
                score_cum += ord(distinct_element) - 96
            case False:
                score_cum += ord(distinct_element) - 38

    print(f"   * Total priorities score is {score_cum}\n")

def puzzle2(data):
    """
    The list of priorities now is 3-elf wise, find the
    common element.
    """
    score_cum = 0
    for i in range(0, len(data), 3):
        triplet = data[i:i+3]
        # get intersection element of 2 lists
        distinct_element = set(triplet[0]) & set(triplet[1]) & set(triplet[2])
        distinct_element = distinct_element.pop()
        # get element value
        match distinct_element.islower():
            case True:
                score_cum += ord(distinct_element) - 96
            case False:
                score_cum += ord(distinct_element) - 38

    print(f"   * Total priorities score is {score_cum}\n")


@click.command()
@click.option("--file-path", type=Path, default = "data")
def main(file_path):
    # load data
    path_file = os.path.join(file_path, "input_p3.txt")
    input_data = load_text_file(path_file)

    print("\n[b] Solution [/] for [u]problem one[/]\n")
    puzzle1(input_data)

    print("[b] Solution [/] for [u]problem two[/]\n")
    puzzle2(input_data)

if __name__ == "__main__":
    main()