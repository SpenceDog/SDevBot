# This class reads from a text file and displays a random line.
import random


def random_quote(usr_command):
    read_file = open('Resources/quotes.txt', 'r')  # Specifies the file to read.
    file_lines = 0  # Holds the total amount of lines in the file.
    picked_line = 0  # The file that was chosen.
    return_value = "A" # What we return.

    with read_file:  # Reads through the file and counts the amount of lines.
        for line in read_file:
            file_lines += 1

    read_file = open('Resources/quotes.txt', 'r')  # Specifies the file to read.
    picked_line = random.randint(0, file_lines)  # Specifies the line that was picked.
    return_value = read_file.readlines()[picked_line - 1]  # Reads the line into the return value.

    return str(return_value)