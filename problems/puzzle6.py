from helpers import time_it, load_text_file
from pathlib import Path
from rich import print
import os
import click


def signal_position(data, n_distinct_chars):
    """
    Return position after the fisrt set of 
    n_distinct_chars
    """
    signal = False
    marker = [0,n_distinct_chars]
    while signal is False and marker[1] < len(data):
        
        signal_data = data[marker[0]:marker[1]]

        if len(set(signal_data)) < n_distinct_chars:
            marker = list(map(sum, zip(marker, [1, 1])))
        else:
            signal = True
            print(f"The marker is in position {marker[1]}")
            print(f"{signal_data}\n")


@click.command()
@click.option("--file-path", type=Path, default = "data")
def main(file_path):
    # load data
    path_file = os.path.join(file_path, "input_p6.txt")
    input_data = load_text_file(path_file)[0]

    print("\n[b] Solution [/] for [u]problem one[/]\n")
    signal_position(input_data, 4)

    print("[b] Solution [/] for [u]problem two[/]\n")
    signal_position(input_data, 14)

if __name__ == "__main__":
    main()