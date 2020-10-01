bonedog = "bonedog.txt"

def get_file_lines(filename):
    infile = open(filename, "r")
    for line in infile:
        print(line)


get_file_lines(bonedog)