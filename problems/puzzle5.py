from helpers import time_it, load_text_file
from pathlib import Path
from rich import print
import os
import click
import re

def stack_movement(dict_stacks, move, elements_2_move):
    """
    Given a list of stacks of boxes and movements,
    follow instructions and return top box in every
    stack.
    """
    dict_stacks[move[2]].extend(elements_2_move)
    dict_stacks[move[1]] = dict_stacks[move[1]][:-move[0]]


@click.command()
@click.option("--file-path", type=Path, default = "data")
def main(file_path):
    # load data
    path_file = os.path.join(file_path, "input_p5.txt")
    input_data = load_text_file(path_file)

    dict_stacks = {k+1: [] for k in range(9)}
    for _, row in enumerate(input_data[:8]):
        for i,j in enumerate(range(0, len(input_data[0]), 4)):
            if row[j:j+3] != '   ':
                dict_stacks[i+1].append(row[j:j+3])

    for k in list(dict_stacks):
        dict_stacks[k].reverse()

    moves = [re.findall(r'\d+', c) for c in input_data[10:]]  

    dict_stacks_onebyone = dict_stacks.copy()
    dict_stacks_all = dict_stacks.copy()

    for i,move in enumerate(moves):
        move = list(map(int, move))
        elements_2_move_all = dict_stacks_all[move[1]][-move[0]:]
        elements_2_move_onebyone = list(reversed(dict_stacks_onebyone[move[1]][-move[0]:]))

        stack_movement(dict_stacks_onebyone, move, elements_2_move_onebyone)
        stack_movement(dict_stacks_all, move, elements_2_move_all)

    print("\n[b] Solution [/] for [u]problem one[/]\n")
    result_onebyone = [l[-1][1:-1] for l in list(dict_stacks_onebyone.values())]
    print(f"   * Top boxes are [b]{''.join(result_onebyone)}[/]\n")

    print("[b] Solution [/] for [u]problem two[/]\n")
    result_all = [l[-1][1:-1] for l in list(dict_stacks_all.values())]
    print(f"   * Top boxes are [b]{''.join(result_all)}[/]\n")


if __name__ == "__main__":
    main()