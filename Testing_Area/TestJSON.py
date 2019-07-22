import json

with open("./extensions/config.json", 'r') as f:
    config = json.load(f)
print(config["MAIN"]["WELCOME_MSG"])