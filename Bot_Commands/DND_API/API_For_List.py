def dnd_api_for_list(response, list_data, line_break):
    returnData = " " # Our return variable.

    for response in list_data:  # Loops through the list of our responses and generates our response.
        returnData += line_break
        returnData += response['name']
        returnData += line_break

    return(returnData)