""" A module with import helper utilities """
import os, sys


def paths(directory_list_of_import_paths):
    """ Add list of folders to system path for importing. """
    for path_dir in directory_list_of_import_paths:
        path = os.path.abspath(path_dir)
        sys.path.append(path)
