import json

def get_data(json_filepath):
    """ simple wrapper function to get data """
    with open(json_filepath) as f:
        my_data = json.load(f)

    return my_data