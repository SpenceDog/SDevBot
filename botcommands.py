# This is where that all of our bot commands are handled.
from Bot_Commands import rolldice


def bot_commands(usr_message):
    usr_command = usr_message

    if usr_command.content.startswith('$hello'):  # Say hi to the users!
        return 'Hiya!'

    if usr_command.content.startswith('$roll'):  # rolls a dice for us.
        return rolldice.roll_dice(usr_message)
