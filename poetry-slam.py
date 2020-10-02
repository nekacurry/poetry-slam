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

lines_printed_backwards(bonedog)

