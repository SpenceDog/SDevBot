import requests
from Bot_Commands.DND_API.API_For_List import dnd_api_for_list

def dnd_api_classes_general(command_search, break_line):
    http_response = requests.get("https://www.dnd5eapi.co/api/" + command_search + "/")  # Call the API.
    api_data = http_response.json()  # Saves the raw JSON of our request.
    resultsList = api_data['results']  # Gets the total amount of results.
    api_response = dnd_api_for_list(http_response, resultsList, break_line) # Converts the list into readable output.


    return str(api_response)  # Sends it in the channel it was called from.