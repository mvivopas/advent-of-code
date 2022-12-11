from helpers import time_it, load_text_file
from pathlib import Path
from rich import print
import os
import click

def signal_strenght(data):
    """Calculate signal strenght of range(20,240,40)
    cycles.
    """
    X_cycle = []
    X = 1

    for i,signal in enumerate(data):
        X_cycle.append(X)
        
        if len(signal) > 1:
            X_cycle.append(X)
            X += int(signal[1])

    sum_cum = 0
    for i in range(20,240,40):
        sum_cum += X_cycle[i-1]*i

    return sum_cum

def draw_crt(crt, X_pos, cycle):
    element = '.'
    if 0 <= cycle%40 - X_pos < 3:
        element = '#'
    crt.append(element)

def crt_drawing_by_cycle(data):
    """Calculate signal strenght of range(20,240,40)
    cycles.
    """
    X_cycle = []
    X = 1
    crt = []

    for i,signal in enumerate(data):
        X_cycle.append(X)
        draw_crt(crt, X, len(X_cycle))
        
        if len(signal) > 1:
            
            X_cycle.append(X)
            draw_crt(crt, X, len(X_cycle))

            X += int(signal[1])

    return crt


@click.command()
@click.option("--file-path", type=Path, default = "data")
def main(file_path):
    # load data
    path_file = os.path.join(file_path, "input_p10.txt")
    input_data = [e.split(' ') for e in load_text_file(path_file)]

    signal_str = signal_strenght(input_data)
    crt_letters = crt_drawing_by_cycle(input_data)

    print("\n[b] Solution [/] for [u]problem one[/]\n")
    print(f"   * Total signal strenght:: {signal_str}\n")

    print("\n[b] Solution [/] for [u]problem two[/]\n")
    print(f"   * CRT drawing is: \n")
    
    for j in range(0,240,40):
        print(''.join(crt_letters[j:j+40]))


if __name__ == "__main__":
    main()