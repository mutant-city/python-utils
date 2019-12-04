""" A module with utility methods for working with python objects. """


def to_string(obj):
    """ Outputs an object as a string. """
    for k in dir(obj):
        if not k.startswith('__'):
            print(k, ":", getattr(obj, k))
    return ""


class DynamicObject:
    """ A generic object which further attributes can be appended to. """

    def __str__(self):
        return to_string(self)
