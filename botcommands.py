# This is where that all of our bot commands are handled.
from Bot_Commands import rolldice
from Bot_Commands import randomquote
from Bot_Commands import help


def bot_commands(usr_message):
    usr_command = usr_message

    if usr_command.content.startswith('$hello'):  # Say hi to the users!
        return 'Hiya!'

    if usr_command.content.startswith('$good bot'):  # Say hi to the users!
        return '^_^'

    if usr_command.content.startswith('$roll'):  # rolls a dice for us.
        return rolldice.roll_dice(usr_message)

    if usr_command.content.startswith('$random fact'):
        return randomquote.random_quote(usr_message)

    if usr_command.content.startswith('$help'):
        return help.help_commands(usr_message)
