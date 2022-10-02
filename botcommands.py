# This is where that all of our bot commands are handled.
import random

def bot_commands(usr_message):
    usr_command = usr_message

    if usr_command.content.startswith('$hello'): # Say hi to the users!
        return 'Hiya!'

    if usr_command.content.startswith('$roll'): # rolls a dice for us.
        return_value = "You rolled: " # String with the data we return.
        rolls_total = 0 # Total of our rolls.

        try:
            times_to_roll = str(usr_command.content)[str(usr_command.content).index(" ") + 1: str(usr_command.content).index("d")] # Cuts the numbers down to what is before the 'd' deliminator.
            sides_to_roll = str(usr_command.content).split("d")[1] # Gets the number after the 'd' deliminator in the command.


            for x in range(int(times_to_roll)): # For each die...
                roll_done = random.randint(1, int(sides_to_roll)) # Rolls the dice with a random number based on the sides specified.
                return_value += str(roll_done) + ", " # Sets the return value.
                rolls_total += roll_done
        except:
            return "`Invalid entry: Please enter as $roll (Amount of dice)d(Sides of dice)`"

        return_value += " which totals " + str(rolls_total) + "."

        return return_value