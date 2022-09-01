import os
import re

from core.colors import run, que, good, green, end, info
from core.requester import requester


def updater():
    """Update the current installation.

    git clones the latest version and merges it with the current directory.
    """
    print(f'{run} Checking for updates')
    # Changes must be separated by ;
    changes = '''major bug fixes;removed ninja mode;dropped python < 3.2 support;fixed unicode output;proxy support;more intels'''
    latest_commit = requester('https://raw.githubusercontent.com/s0md3v/Photon/master/core/updater.py', host='raw.githubusercontent.com')
    # Just a hack to see if a new version is available
    if changes not in latest_commit:
        changelog = re.search(r"changes = '''(.*?)'''", latest_commit)
        # Splitting the changes to form a list
        changelog = changelog[1].split(';')
        print(f'{good} A new version of Photon is available.')
        print(f'{info} Changes:')
        for change in changelog: # print changes
            print(f'{green}>{end} {change}')

        current_path = os.getcwd().split('/') # if you know it, you know it
        folder = current_path[-1] # current directory name
        path = '/'.join(current_path) # current directory path
        choice = input(f'{que} Would you like to update? [Y/n] ').lower()

        if choice != 'n':
            print(f'{run} Updating Photon')
            os.system(f'git clone --quiet https://github.com/s0md3v/Photon {folder}')
            os.system(
                f'cp -r {path}/{folder}/* {path} && rm -r {path}/{folder}/ 2>/dev/null'
            )

            print(f'{good} Update successful!')
    else:
        print(f'{good} Photon is up to date!')
