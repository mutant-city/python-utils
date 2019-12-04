import os, sys, inspect, os.path, shutil


def depth_first_dir_walk(path, max_depth=3, current_depth=0):
    """ walk the directory tree in a depth first fashion with a max_depth limit """
    if current_depth > max_depth:
        return
    for entry in os.scandir(path):
        try:
            yield entry
            if entry.is_dir(follow_symlinks=False):
                yield from depth_first_dir_walk(entry.path, max_depth, current_depth + 1)
        except Exception as e:
            print(e)
            continue


def delete_dir(dirname, error=False):
    try:
        shutil.rmtree(dirname)
    except OSError as e:
        if error:
            print("Error: %s - %s." % (e.filename, e.strerror))


def create_dir(dir, gitkeep=False):
    if not os.path.exists(dir):
        os.makedirs(dir)
    if gitkeep:
        file = open(dir + "/.gitkeep", 'w')
        file.write('')
        file.close()


def dir_is_present(dir):
    return os.path.isdir(dir)


def dir_is_empty(dir):
    """
        Check if a Directory is empty and also check exceptional situations.
    """
    if os.path.exists(dir) and os.path.isdir(dir):
        if not os.listdir(dir):
            return True
        else:
            return False
    else:
        print("Given Directory don't exists")
