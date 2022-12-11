from helpers import time_it, load_text_file
from pathlib import Path
from rich import print
import os
import click


def update_directories(input_data):
    dir_list = ['/']
    dir_dict = {}
    # depth index list
    deep_levels = [0]

    # index to control backward going
    threshold_control = 0
    # depth of the current folder
    dir_deep = 0
    dir_path = ''

    for element in input_data[1:]:
        # if changing directory
        if '$ cd' in element:
            # if accessing a folder
            if '..' not in element:
                # compose full directory path
                dir_path = dir_list[deep_levels[dir_deep]] + element.split()[2] + '/'
                dir_list.append(dir_path)
                # update depth indicator
                dir_deep += 1

                # if in a new depth level add index to deep_levels
                if dir_deep >= len(deep_levels):
                    deep_levels.append(len(dir_list)-1)
                # else over-write in the depth level the new index
                else:
                    deep_levels[dir_deep] = len(dir_list)-1
                threshold_control = 0

            # if going backwards and threshold_control is not higher than deep
            # aka, it's trying to go more backwards than possible
            elif '..' in element and threshold_control <= dir_deep: 
                dir_deep -=1
                threshold_control +=1

        # else if element is a file
        elif element[0].isdigit():
            file_size = int(element.split()[0])

            # if dirpath is recorded in dir_dict append         
            if dir_dict.get(dir_path) is not None:
                dir_dict[dir_path].append(file_size)

            # else create list with size
            else: 
                dir_dict[dir_path] = [file_size]

    return dir_list, dir_dict


@click.command()
@click.option("--file-path", type=Path, default = "data")
def main(file_path):
    # load data
    path_file = os.path.join(file_path, "input_p7.txt")
    input_data = load_text_file(path_file)

    dir_list, dir_dict = update_directories(input_data)

    size_dict = {}
    size_cum_filter = 0
    for path in dir_list:
        # initialize size counter
        size_cum = 0
        for key in dir_dict:
            if path in key:
                size_cum += sum(dir_dict[key])

        size_dict[path] = size_cum
        if size_cum < 100000:
            size_cum_filter += size_cum

    space2delete =  30000000 - (70000000 - max(size_dict.values()))
    candidates_2delete = [v for v in size_dict.values() if v > space2delete]
    candidates_2delete.sort()

    print("\n[b] Solution [/] for [u]problem one[/]\n")
    print(f"   * Total size of directories with size than 100m is: {size_cum_filter}\n")

    print("\n[b] Solution [/] for [u]problem two[/]\n")
    print(f"   * Size of the directory to delete is: {candidates_2delete[0]}\n")



if __name__ == "__main__":
    main()