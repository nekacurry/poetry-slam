#Poetry Slam

import random
bd = "bonedog.txt"


#Poem Functions ------>

def get_file_lines(filename):
    infile = open(filename)
    return infile.readlines()


def lines_printed_default(lines_list):
    infile = open(lines_list)
    for line in infile:
        print(line)

    infile.close()

def lines_printed_backwards(lines_list):
    infile = open(lines_list)
    revLines = infile.readlines()
    count = 72

    for line in reversed(revLines):
        count -= 1
        print(str(count) + '\t' + line)
        #\t adds space bewteen number and line
    infile.close()


def lines_printed_random(lines_list):
    infile = open(lines_list)

    with infile as ran:
        lines = list(ran)
        #turns file lines into a list to be shuffled
    random.shuffle(lines)

    for line in lines:
        print(line)

    infile.close


def lines_printed_custom(lines_list):
    infile = open(lines_list)

    for line in sorted(infile):
        print(line)

    infile.close()


#UI Control-------->

def main():
    intro()
    choice = question()
    processing(choice)

def intro():
    print()
    print("Bonedog by Eva H.D.")
    print()

def processing(choice):
    for num in choice:
        if choice == "1":
            lines_printed_default(bd)

        elif choice == "2":
            lines_printed_backwards(bd)

        elif choice == "3":
            lines_printed_random(bd)

        elif choice == "4":
            lines_printed_custom(bd)
            


def question():
    while True:

        choice = ()
        print("How would you like to read this poem?:")
        print("     1 = Default")
        print("     2 = Backwards")
        print("     3 = Randomly")
        print("     4 = Alphabetical")

        choice = input("--->", )

        if choice[0] >= "1" and choice[0] < "5" and len(choice) == 1:
                break
        print()
    print()
    return choice


#Call program --->

main()