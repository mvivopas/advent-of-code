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
    for element in data:
        pair1, pair2 = element.split(',')
        pair1 = [ int(p) for p in pair1.split('-')]
        pair2 = [ int(p) for p in pair2.split('-')]

        farter_start = max(pair1[0],pair2[0])
        closer_end = min(pair1[1],pair2[1]) 

        if any([farter_start,closer_end] == x for x in [pair1, pair2]):
            score_cum += 1

    print(f"   * Number of totally overlapped pairs is {score_cum}\n")


def puzzle2(data):
    score_cum = 0
    for element in data:
        pair1, pair2 = element.split(',')
        pair1 = [ int(p) for p in pair1.split('-')]
        pair2 = [ int(p) for p in pair2.split('-')]

        if max(pair1[0], pair2[0]) <= min(pair1[1], pair2[1]):
            score_cum += 1

    print(f"   * Number of totally overlapped pairs is {score_cum}\n")


@click.command()
@click.option("--file-path", type=Path, default = "data")
def main(file_path):
    # load data
    path_file = os.path.join(file_path, "input_p4.txt")
    input_data = load_text_file(path_file)

    print("\n[b] Solution [/] for [u]problem one[/]\n")
    puzzle1(input_data)

    print("[b] Solution [/] for [u]problem two[/]\n")
    puzzle2(input_data)

if __name__ == "__main__":
    main()