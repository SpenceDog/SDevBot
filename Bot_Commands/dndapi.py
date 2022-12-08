import requests
from Bot_Commands.DND_API.dnd_api_classes_general import dnd_api_classes_general

def dnd_api(usr_command):
    begin_command = "$5e " # What the beginning of this command is.
    line_break = "```" # Used to simulate a linebreak on Discord.
    command_message = " " # Generic string that we return the value of any of our searches.

    try:
        dnd_search = str(usr_command.content.lower()).split(begin_command)[1]  # Gets the string after the '$5e' deliminator in the command.
        if dnd_search.lower() == "classes":  # If we searched for classes...
            command_message = dnd_api_classes_general(dnd_search, line_break, 'results')

        else:
            class_search = str(dnd_search).split("classes ")[1] # Splits the message after classes.
            search_query = "classes/" + class_search # Builds our query.
            print(search_query)

            http_response = requests.get("https://www.dnd5eapi.co/api/" + search_query + "/")  # Call the API.
            api_data = http_response.json()  # Saves the raw JSON of our request.

            command_message = f"""
Class: class_name
Hit Dice: hit_die
Proficiencies (Choose choose_prof: 
 """

            command_message = command_message.replace("class_name", str(api_data["name"])).replace("hit_die", str(api_data["hit_die"])) # Replaces with our values.


    except:
        command_message = line_break + 'Use this command to search the D&D 5e SRD Content. Can specifiy content by entering "Classes" as a parameter.' + line_break


    return str(command_message) # Sends it in the channel it was called from.

