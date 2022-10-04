# This class reads from a text file and writes each line. Specifically ALL the commands.
import random


def help_commands(usr_command):
    read_file = open('Resources/help_commands.txt', 'r')  # Specifies the file to read.
    return_value = read_file.read() # What we return.

    return str(return_value)