import json


def load_metadata(path):

    with open(path, "r") as file:
        return json.load(file)