from Bot_Commands.DND_API.dnd_api_classes_general import dnd_api_classes_general

def dnd_api(usr_command):
    begin_command = "$5e " # What the beginning of this command is.
    line_break = "```" # Used to simulate a linebreak on Discord.
    command_message = " " # Generic string that we return the value of any of our searches.

    try:
        dnd_search = str(usr_command.content).split(begin_command)[1]  # Gets the string after the '$5e' deliminator in the command.
        if dnd_search.lower() == "classes":  # If we searched for classes...
            command_message = dnd_api_classes_general(dnd_search, line_break)

        else:
            command_message = line_break + 'Use this command to search the D&D 5e SRD Content. Can specifiy content by entering "Classes" as a parameter.' + line_break
    except:
        command_message = line_break + 'Use this command to search the D&D 5e SRD Content. Can specifiy content by entering "Classes" as a parameter.' + line_break


    return str(command_message) # Sends it in the channel it was called from.

