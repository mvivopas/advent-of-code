from helpers import time_it, load_text_file
from pathlib import Path
from rich import print
import os
import click

dict_moves = {'U': [1, 0], 'R': [0, 1], 'L':[0, -1], 'D': [-1, 0]}
diagonal_moves = {'UR':[-1,-1], 'UL':[-1,1], 'DL':[+1,-1], 'DR':[1,1]}

def sum_lists(l1,l2):
    return list(map(sum, zip(l1, l2)))

def update_vec(h_position, t_position):
    """Update tail vector (t_position) with dependency
    to h_position.
    """
    # list candidate cross positions
    cross_positions = [sum_lists(t_position,d) for d in dict_moves.values()]
    # list candidate diagonal positions
    diagonal_positions = [sum_lists(t_position,d) for d in diagonal_moves.values()]

    # if head is not in the forelisted positions,
    # nor in the same position than tail [0,0]
    # then move tail position in the direction of heads
    if h_position not in [*cross_positions, *diagonal_positions, [0,0]]:
        diff_postion = [x-y for x,y in zip(t_position, h_position)]
        trans_vec = [int((-1)*a/abs(a)) if a !=0 else 0 for a in diff_postion]
        t_position = sum_lists(t_position, trans_vec)

    return t_position

def rope_movement(data, num_tails):
    """Track all rope movements, updating vectors and saving
    tail distinct positions (final output).
    """
    rope_positions =  (num_tails + 1)*[[0,0]]
    t_position_record = [rope_positions[-1]]

    for move in data:
        for i in range(int(move[1])):
            movement_vec = dict_moves[move[0]]
            rope_positions[0] =  sum_lists(rope_positions[0], movement_vec)

            for j in range(len(rope_positions[1:])):
                rope_positions[j+1] = update_vec(rope_positions[j],rope_positions[j+1])

                if j == len(rope_positions[1:]) - 1 and rope_positions[j+1] \
                        not in t_position_record:
                    t_position_record.append(rope_positions[j+1])
    
    return len(t_position_record)


@click.command()
@click.option("--file-path", type=Path, default = "data")
def main(file_path):
    # load data
    path_file = os.path.join(file_path, "input_p9.txt")
    input_data = [e.split(' ') for e in load_text_file(path_file)]

    t_position_rec_1_tail = rope_movement(input_data, 1)
    t_position_rec_9_tail = rope_movement(input_data, 9)

    print("\n[b] Solution [/] for [u]problem one[/]\n")
    print(f"   * Total distinct positions tail has visited are: {t_position_rec_1_tail}\n")

    print("\n[b] Solution [/] for [u]problem two[/]\n")
    print(f"   * Total distinct positions tail has visited are: {t_position_rec_9_tail}\n")



if __name__ == "__main__":
    main()



