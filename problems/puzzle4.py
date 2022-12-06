from helpers import time_it, load_text_file
from pathlib import Path
from rich import print
import os
import click

def total_overlap(pair1, pair2):
    """
    Find totally overlapping pairs.
    """
    farter_start = max(pair1[0],pair2[0])
    closer_end = min(pair1[1],pair2[1]) 

    if any([farter_start,closer_end] == x for x in [pair1, pair2]):
        return 1
    else:
        return 0


def partial_overlap(pair1, pair2):
    """
    Find partially overlapping pairs.
    """
    if max(pair1[0], pair2[0]) <= min(pair1[1], pair2[1]):
        return 1
    else:
        return 0


@click.command()
@click.option("--file-path", type=Path, default = "data")
def main(file_path):
    # load data
    path_file = os.path.join(file_path, "input_p4.txt")
    input_data = load_text_file(path_file)

    score_total_overlap = 0
    score_partial_oiverlap = 0
    for element in input_data:
        pair1, pair2 = element.split(',')
        pair1 = [ int(p) for p in pair1.split('-')]
        pair2 = [ int(p) for p in pair2.split('-')]

        score_total_overlap += total_overlap(pair1, pair2)
        score_partial_oiverlap += partial_overlap(pair1, pair2)

    print("\n[b] Solution [/] for [u]problem one[/]\n")
    print(f"   * Number of totally overlapped pairs is {score_total_overlap}\n")

    print("[b] Solution [/] for [u]problem two[/]\n")
    print(f"   * Number of partially overlapped pairs is {score_partial_oiverlap}\n")


if __name__ == "__main__":
    main()