import os, subprocess, shlex


# note: this will give the out put in real time but will not capture the output
def run_os_command(command):
    os.system(command)

# note this will only give the output after it's completed but the output will be captured
def run_os_command_v2(command, return_output_only=True, throw_on_err=False):
    """
        Run an OS command with some sane defaults.
        Awesome reference: https://codecalamity.com/run-subprocess-run/
    """
    params = {
        'stdout': subprocess.PIPE,
        'stderr': subprocess.PIPE,
        'universal_newlines': True,
        'shell': True
    }

    if throw_on_err:
        params["check"] = True

    subproc = subprocess.run(
        command,
        **params
    )

    if return_output_only:
        if subproc.returncode is 0:
            return subproc.stdout
        else:
            raise Exception(subproc.stderr)

# this is the version that needs to be developed to 1>capture output and 2> display output in real time simoultaneously
def run_os_command_v3(command):
    """ 
        https://www.endpoint.com/blog/2015/01/28/getting-realtime-output-using-python
    """
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc
