import os
from time import sleep

from sync_folders import main

if __name__ == '__main__':
    home = os.path.expanduser('~') + '/'
    for subdir in os.listdir(home):
        subdir_ = home + subdir + '/'
        if os.path.isdir(subdir_):
            try:
                dir_list = os.listdir(subdir_)
                if '.git' in dir_list:
                    print(subdir_)
                    os.system(f'cd {subdir_} && git fetch')
                    sleep(5)
                    drive_subdir = home + 'OneDrive/Repos/' + subdir
                    if not os.path.exists(drive_subdir):
                        os.mkdir(drive_subdir)
                    main.sync(home + subdir, drive_subdir)

            except Exception as e:
                print(e)
