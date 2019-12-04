import requests


# get personal access token from here
# https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
def get_github_file(url_of_raw_page, git_token):
    headers = {
        'Authorization': f"token ${git_token}",
        'Accept': 'application/vnd.github.v3.raw',
    }
    try:
        r = requests.get(url_of_raw_page, headers=headers)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
