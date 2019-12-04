""" A module for working with any form of collection data structure. """
import json


def recursive_stringerizer(data):
    """ 
    Recursively converts all keys and values to strings.
    Return type = original python collection object 
    """
    if isinstance(data, list):
        return [recursive_stringerizer(item) for item in data]
    if isinstance(data, dict):
        return {str(k): recursive_stringerizer(data[k]) for k in data}
    if isinstance(data, tuple):
        return tuple(recursive_stringerizer(item) for item in data)
    return str(data)


def to_json(data):
    """ Converts any collection to json. """
    data = recursive_stringerizer(data)  # converts every k/v to a string
    json_data = json.loads(json.dumps(data))  # convert to json
    return json_data


def keys_exists(dict, keys):
    _element = dict
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return True


def nested_set(dic, keys, value):
    if not keys_exists(dic, keys):
        return False
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value
