command_message = [
    ("add_user", "This will add a user to the Github Org"), 
    ("hello bot", "Say hello to Dash!!")
]

def help():
    message = "Help Menu:\n\n"
    for data in command_message:
        message += f"\t- {data[0]}: {data[1]}\n"

    return message