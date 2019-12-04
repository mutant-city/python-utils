""" A utility module for working with files """
import os, zipfile, shutil


def delete(filename, error=False):
    """ Deletes a file. """
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        if (error == True):
            print("Error: %s file not found" % filename)


def write(filename, in_string=False):
    file = open(filename, 'w')
    if (in_string):
        file.write(in_string)
    file.close()


def to_string(filename, error=False):
    """ Get an entire file back as a string(non-buffering: loads entire file into memory, not meant for large files). """
    if os.path.exists(os.path.dirname(filename)):
        f = open(filename, "r")
        return f.read()
    else:
        if (error == True):
            print("Error: %s file not found" % filename)
    return False


def list_all_in_dir(mypath, recurse=False, path=False):
    """ 
    Returns a string list of every file in a directory. 
    Pass recurse=True to get a list of all files in subdir as well.
    Pass path=True to get the full path instead of just file name.
    
    """
    if recurse:
        out = []
        for f in os.listdir(mypath):
            loc = os.path.join(mypath, f)
            if os.path.isfile(loc):
                if path:
                    out.append(loc)
                else:
                    out.append(f)
            elif os.path.isdir(loc):
                out = out + list_all_in_dir(loc, True, path)
        return out
    else:
        return [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]


def create_zip_file(input_location, output_location):
    """
    can be file or directory,
    Note: .zip extension will be automatically appended to output_location string
    """
    # remove trailing zip extension if present
    output_location = output_location.split(".")
    if output_location[-1] == "zip":
        del output_location[-1]
    output_location = ".".join(output_location)
    try:
        if os.path.isdir(input_location):
            shutil.make_archive(output_location, 'zip', input_location)
        elif os.path.isfile(input_location):
            zipfile.ZipFile(f"{output_location}.zip", mode='w').write(input_location)
        else:
            raise Exception("Input path was neither a file or a directory or could not be found.")
    except Exception as e:
        print("Zip file not created Successfully: " + output_location)
        raise Exception(e)
    print("Zip file was created Successfully:" + output_location)
