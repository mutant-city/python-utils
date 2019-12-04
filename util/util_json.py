""" A utility module for working with json """
import json


def dumps_no_whitespace(data):
    """ Ensure no whitespace with a json dumps. """
    if isinstance(data, str):
        data = json.loads(data)
    return json.dumps(data, separators=(',', ':'))


def is_valid_json(data):
    try:
        json_object = json.loads(data)
    except ValueError as e:
        return False
    return True
