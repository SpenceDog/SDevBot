# This is where that all of our bot commands are handled.
from Bot_Commands import rolldice
from Bot_Commands import randomquote
from Bot_Commands import help
from Bot_Commands import dndapi


def bot_commands(command_id, usr_message):
    usr_command = usr_message

    if usr_command.content.startswith(command_id + 'hello'):  # Say hi to the users!
        return 'Hiya!'

    if usr_command.content.startswith(command_id + 'good bot'):  # Say hi to the users!
        return '^_^'

    if usr_command.content.startswith(command_id + 'roll'):  # rolls a dice for us.
        return rolldice.roll_dice(usr_message)

    if usr_command.content.startswith(command_id + 'random fact'):
        return randomquote.random_quote(usr_message)

    if usr_command.content.startswith(command_id + 'help'):
        return help.help_commands(usr_message)

    if usr_command.content.startswith('$5e'):
        return dndapi.dnd_api(usr_message)