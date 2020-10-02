import random
bonedog = "bonedog.txt"

def get_file_lines(filename):
    infile = open(filename)
    return infile.readlines()
    infile.close()

def lines_printed_backwards(lines_list):
    infile = open(lines_list)
    revLines = infile.readlines()
    count = 72
    for line in reversed(revLines):
        count -= 1
        print(str(count) + '\t' + line)
    infile.close()


def lines_printed_random(lines_list):
    infile = open(lines_list)
    with infile as ran:
        lines = list(ran)
    random.shuffle(lines)
    for line in lines:
        print(line)
    infile.close

lines_printed_random(bonedog)