""" A utility module for working with lists. """


def list_intersection(list1, list2):
    """
    Get the intersection of two lists
    """
    return [value for value in list1 if value in list2]


def list_difference(list1, list2):
    """ 
        Get the difference between two lists
    """
    return [item for item in list1 if item not in list2]
