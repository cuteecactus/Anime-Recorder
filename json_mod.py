import json

def read_json(path):
    with open (path, "r") as json_file:
        data = json.load(json_file)
        return data


def write_json(path, data):
    with open (path, 'w') as json_file:
        json.dump(data, json_file, indent=4)