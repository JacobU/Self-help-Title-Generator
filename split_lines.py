    
import sys

def split_lines(read_file, write_file_first, write_file_second):
    """
    Takes 3 arguments. The relative/absolute path to an input file that must exist and the relative/absolute paths to output files
    whichmay not necessarily exist. The function then iterates through the input file line by line and splits the line into the respective output files 
    based on the : character.
    """
    with open(read_file,"r") as rf:
        with open(write_file_first,"w+") as wf_first:
            with open(write_file_second, "w+") as wf_second:
                for line in rf:
                    if ':' in line:
                        wf_first.write(line.split(':')[0] +'\n')
                        wf_second.write(line.split(':')[1])
                    else:
                        wf_first.write(line)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        raise Exception("You've entered the wrong number of command line arguments. This script takes 3 command line arguments")
    
    input_file = sys.argv[1]
    output_file_first = sys.argv[2]
    output_file_second = sys.argv[3]
    split_lines(input_file, output_file_first, output_file_second)