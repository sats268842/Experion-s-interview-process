# Experion-interview-process

                                                                 
                                                              Python - Instructions to Build & Execute

Solution without Build files
If you are providing a solution without using the build file, we want you to name your Main file as geektrust.py. This is the file that will contain your main method.

This file should receive in the command line argument and parse the file passed in. Once the file is parsed and the application processes the commands, it should only print the output.

For e.g your geektrust.py file will look like this

def main():
    input_file = sys.argv[1]
    # sys.argv[1] should give the absolute path to the input file
    # parse the file and process the command
    # print the output

if __name__ == "__main__":
    main()
We build and run the solution by using the following command.

python -m geektrust <absolute_path_to_input_file>
