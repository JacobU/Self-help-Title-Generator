    
import sys

def choose(read_file, write_file):
"""
Takes 2 arguments. The relative/absolute path to an input file that must exist and the relative/absolute path to an output file
may not necessarily exist. The function then iterates the the input file line by line and writes the line to the output file 
depending on the input of the user.

y: Write line
n: Skip line
x: Exit the function
"""

    print("The title of a book will be displayed. \nEnter a 'y' if you think it is a self-help book. \nOtherwise enter 'n'. \nEnter 'x' to exit the program safely.")

    with open(read_file,"r") as rf:
        with open(write_file,"w+") as wf:

            for line in rf:

                print(line)
                choice = input()
                
                while choice != "y" and choice != "n" and choice != "x":
                    print("Invalid input. \nEnter a 'y' if you think it is a self-help book. \nOtherwise enter 'n'. \nEnter 'x' to exit the program safely.")
                    choice = input()

                if choice == "y":
                    wf.write(line)
                elif choice == "n":
                    continue
                elif choice == "x":
                    break

if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise Exception("You've entered the wrong number of command line arguments. This script takes 2 command line arguments")
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    choose(input_file, output_file)