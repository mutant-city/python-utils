""" A module with utility method for working with strings. """
import re, os, base64


def to_base64(in_string):
    """ Converts a string to base64. """
    return base64.b64encode(str.encode(in_string)).decode('utf-8')


def from_base64(in_string_base64):
    """ Decodes base64 string data(note: ascii, utf8, utf16, utf32 are all subsets of unicode and valid here). """
    return base64.b64decode(in_string_base64).decode("unicode_escape")


def is_truthy(in_string):
    """ Takes a string and tests it for truthiness. """
    return in_string.lower() in ("yes", "true", "t", "1")


def is_falsey(in_string):
    """ Takes a string and tests it for falsiness. """
    return in_string.lower() in ("no", "false", "f", "0")


def to_file(in_string, filename):
    """ Non-buffering string write to file. """
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    f = open(filename, "a")
    f.write(in_string)
    f.close()


def to_snake_case(in_string):
    """
    Convert a camel, underscore, or spaced case to snake.
    'The TestStr is_a test'  =>  'the_test_str_is_a_test'
    """
    data = in_string.split(' ')
    out = []
    for item in data:
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', item)
        item = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
        out.append(item)
    return '_'.join(out)


def to_camel_case(in_string):
    """
      Convert a string to camel case.
      'The TestStr is_a test'  =>  'TheTestStrIsATest'
    """
    out = re.findall(r'\s+[A-Za-z0-9][a-z0-9]*|\_+[A-Za-z0-9][a-z0-9]*|[A-Z0-9][a-z0-9]*|^[a-z][a-z0-9]*', in_string)
    return ''.join(x.replace("_", "").replace(" ", "").title() for x in out)


def remove_white_space(in_string):
    """ Removes all white space from a string """
    return "".join(in_string.split())
