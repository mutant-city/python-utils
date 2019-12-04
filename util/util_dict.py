"""
A module with utility methods for working with a dictionary.
For this module a dictionary is considered to be a single level key/value collection.
For nested dictionaries see the collection.py module.
"""
import json, re, collections
import util_json, util_obj


def dict_to_obj(dict):
    """ converts a dict to an object """
    new_object = util_obj.DynamicObject()
    for k in dict:
        v = dict[k]
    setattr(new_object, k, v)
    return new_object


def map_values(destination_data, source_data, in_map, throw_if_absent=False):
    """ Maps values from source dict to destination dict. """
    for key, value in in_map.items():
        if key in destination_data and value in source_data:
            destination_data[key] = source_data[value]
    return destination_data


def transform_values(in_dict, k_v_map):
    """ Takes a dictionary object and key value map and transforms the dict
    values with the values in the k/v map. """
    for key, value in k_v_map.items():
        if key in in_dict:
            in_dict_val = in_dict[key]
            for original, replacement in value.items():
                try:
                    if in_dict_val in original:
                        in_dict[key] = replacement
                except TypeError:
                    if in_dict_val == original:
                        in_dict[key] = replacement
    return in_dict


def allowed_values(in_dict, key_value_dict, check_presence=False):
    """
    Pass in a dictionary and a map of key values and returns error list for the values that don't match.
    Setting check presence to True also add to the list if keys arent present
    """
    invalid = []
    for key, value in key_value_dict.items():
        if key not in in_dict:
            if check_presence:
                invalid.append({key: "Key not present"})
            continue

        if in_dict[key] not in value:
            invalid.append({key: value})

    return invalid


def required_keys(in_dict, required_key_list):
    """ 
    Ensures the passed in keys are present in the dictionary. 
    Pass false as last parameter to return a list of errors instead of throw exception.
    """
    invalid = []
    for item in required_key_list:
        if (item not in in_dict):
            invalid.append(item)
    return invalid


def find_key_by_regex(data_dict, regex):
    """ Searches a dict for a key by a matching regex. """
    for key in data_dict:
        if re.search(regex, key):
            return key
    return None


def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def check_type(in_dict, key_type_match):
    out_mismatches = []
    for key, value in key_type_match.items():
        if key not in in_dict:
            continue
        if not type(in_dict[key]) == type(value):
            out_mismatches.append(key + "should be: " + str(type(value)))
    return out_mismatches
