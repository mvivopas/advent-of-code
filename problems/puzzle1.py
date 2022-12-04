from helpers import time_it, load_text_file
from pathlib import Path
from rich import print
import os
import click

def puzzle1(file_path):
    """
    List of calories/elf, the '' element marks
    the separation between 2 elves. Keep and report
    the maximum calories carried by an elf.
    """
    max_calories = 0
    calories_elfo = 0
    for element in data:

        if element == '': 
            if max_calories < calories_elfo:
                max_calories = calories_elfo
            calories_elfo = 0
        
        else:
            element = int(element)
            calories_elfo += element

    print("   * The elfo carrying most calories brings a total"
          f"of {max_calories}\n")

def puzzle2(data):
    """
    Now report top 3 elves carrying most calories.
    """
    calories_elfo = 0
    calories_list = []
    for element in data:
        if element != '': 
            element = int(element)
            calories_elfo += element
        else:
            calories_list.append(calories_elfo)
            calories_elfo = 0

    sorted_calories = sorted(calories_list, reverse=True)

    print("   * The top 3 elfos carrying most calories brings"
          f"a total of {sum(sorted_calories[:3])}\n")


@click.command()
@click.option("--file-path", type=Path, default = "data")
def main(file_path):
    # load data
    path_file_p1 = os.path.join(file_path, "input_p1.txt")
    input_data = load_text_file(path_file_p1)

    print("\n[b] Solution [/] for [u]problem one[/]\n")
    puzzle1(input_data)

    print("[b] Solution [/] for [u]problem two[/]\n")
    puzzle2(input_data)

if __name__ == "__main__":
    main()

