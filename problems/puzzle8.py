from helpers import time_it, load_text_file
from pathlib import Path
from rich import print
import os
import click

import numpy as np


def tree_counter_outside(Y):
    """Find the nº of tree positions visibles from
    outside the grid."""
    
    lenght = len(Y[0,:])
    counter = 0
    for col in range(lenght):
        for row in range(lenght):
            element = Y[row,col]

            if any(x in [0, lenght - 1] for x in [col, row]):
                counter += 1

            elif element == 0:
                continue
            
            elif any(x < element for x in [max(Y[row,:col]), max(Y[row,col+1:]),
                                            max(Y[row+1:,col]), max(Y[:row,col])]):
                counter += 1
    return counter

def maximum_tree_inside_score(Y):
    """Find the tree position with most tree visibility.
    """
    lenght = len(Y[0,:])
    max_score = 0
    for col in range(lenght):
        for row in range(lenght):
            pos_cum = []
            surronding_trees = [list(reversed(Y[row,:col])), Y[row,col+1:],
                                Y[row+1:,col], list(reversed(Y[:row,col]))]

            for s in surronding_trees:
                if len(s):
                    i = 0
                    val_ = s[0]
                    while i < len(s) - 1 and val_ < Y[row, col]:
                        i += 1
                        val_ = s[i]
                    
                    farter_tree_pos = i + 1
                    pos_cum.append(farter_tree_pos)
                else:
                    pos_cum.append(0)  
            
            prod_ = np.prod(pos_cum)
            max_score = prod_ if prod_ > max_score else max_score

    return max_score


@click.command()
@click.option("--file-path", type=Path, default = "data")
def main(file_path):
    # load data
    path_file = os.path.join(file_path, "input_p8.txt")
    input_data = [list(map(int,list(e))) for e in load_text_file(path_file)]

    Y = np.array(input_data)
    trees_outside_num = tree_counter_outside(Y)
    tree_inside_score = maximum_tree_inside_score(Y)

    print("\n[b] Solution [/] for [u]problem one[/]\n")
    print(f"   * Total number of trees visible from outside the grid are: {trees_outside_num}\n")

    print("\n[b] Solution [/] for [u]problem two[/]\n")
    print(f"   * Score of the tree with maximum tree visibility is : {tree_inside_score}\n")



if __name__ == "__main__":
    main()