from helpers import time_it, load_text_file
from pathlib import Path
from rich import print
import os
import click

# required for problem 1
DICT_FIGURE_MATCH = {'A': 'X', 'B': 'Y', 'C': 'Z'}
DICT_FIGURE_POINTS = {'A': 1, 'B':2, 'C': 3}
DICT_CONTRARY_LOSER_MOVE = {'A':'Y', 'B':'Z', 'C':'X'}

# required for problem 2
DICT_RESULT_POINTS = {'X': 0, 'Y': 3, 'Z': 6}
DICT_CONTRARY_LOSER_FIGURES = {'A':['B','C'], 'B':['C','A'], 'C':['A','B']} 
DICT_IDX_LOSER_FIGURES = {'Z': 0, 'X': 1}

def puzzle1(data):
    """
    List of rock-scissors-paper figures, every
    figure and result has a score, calculate final
    score.
    """
    score_cum = 0
    for element in data:
        element = element.split(' ')

        # sum result points
        score_cum += DICT_FIGURE_POINTS[element[0]]
        
        # if same figure -> draw -> +3 points 
        if DICT_FIGURE_MATCH[element[0]] == element[1]:
            score_cum += 3

        # if winner figure -> win -> +6 points 
        elif DICT_CONTRARY_LOSER_MOVE[element[0]] == element[1]:
            score_cum += 6

    print(f"   * Total score of {score_cum}\n")

def puzzle2(data):
    """
    List of rock-scissors-paper figures & expected
    result, calculate final score.
    """
    score_cum = 0
    for element in data:
        element = element.split(' ')

        # sum result points
        score_cum += DICT_RESULT_POINTS[element[1]]

        # if its a draw -> sum rival figure points
        if element[1] == 'Y':
            score_cum += DICT_FIGURE_POINTS[element[0]]

        # if not, check in DICT_CONTRARY_LOSER_FIGURES,
        # where index 0 is winner and 1 is loser
        else:
            idx_result = DICT_IDX_LOSER_FIGURES[element[1]]
            our_figure = DICT_CONTRARY_LOSER_FIGURES[element[0]][idx_result]
            our_figure_points = DICT_FIGURE_POINTS[our_figure]
            score_cum += our_figure_points

    print(f"   * Total score of {score_cum}\n")


@click.command()
@click.option("--file-path", type=Path, default = "data")
def main(file_path):
    # load data
    path_file_p2 = os.path.join(file_path, "input_p2.txt")
    input_data = load_text_file(path_file_p2)

    print("\n[b] Solution [/] for [u]problem one[/]\n")
    puzzle1(input_data)

    print("[b] Solution [/] for [u]problem two[/]\n")
    puzzle2(input_data)

if __name__ == "__main__":
    main()