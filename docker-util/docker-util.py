import subprocess


def docker_image_present(docker_image):
    command = "docker images | awk '{print $1}'"
    out = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        shell=True,
        check=True
    ).split("\n")
    if docker_image in out:
        return True
    return False
