import requests
import json

def dnd_api(usr_command):
    begin_command = "$5e " # What the beginning of this command is.
    line_break = "```" # Used to simulate a linebreak on Discord.
    command_message = " " # Generic string that we return the value of any of our searches.

    dnd_search = str(usr_command.content).split(begin_command)[1]  # Gets the string after the '$5e' deliminator in the command.
    if dnd_search.lower() == "classes": # If we searched for classes...
        command_message = dnd_api_classes_general(dnd_search, line_break)

    else:
        command_message = line_break + 'Use this command to search the D&D 5e SRD Content. Can specifiy content by entering "Classes" as a parameter.' + line_break

    return str(command_message) # Sends it in the channel it was called from.

def dnd_api_classes_general(command_search, break_line):
    http_response = requests.get("https://www.dnd5eapi.co/api/" + command_search + "/")  # Call the API.
    api_data = http_response.json()  # Saves the raw JSON of our request.
    resultsList = api_data['results']  # Gets the total amount of results.
    api_response = " " # Sets up are variable for the response.

    for http_response in resultsList:  # Loops through the list of our responses and generates our response.
        api_response += break_line
        api_response += http_response['name']
        api_response += break_line


    return str(api_response)  # Sends it in the channel it was called from.