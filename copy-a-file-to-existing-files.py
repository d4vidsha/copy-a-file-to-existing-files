from os import listdir, getcwd
from os.path import isfile, join
from shutil import copyfile

# current project directory
PATH = getcwd()

# name of files to sync
ZAPIER_DEFAULTS = "sync-to-here.txt"

# name of file to sync from
MASTER = "master.txt"

''' Given a `path` to the directory you would like to sync, the `master` 
    filename which will contain the data to copy from, and the `filename`
    to copy into, do the syncing.

    Note that `master` and `filename` must not be the same file.
'''
def sync_files(path, master, filename):
    for f in listdir(path):
        new_path = join(path, f)
        if isfile(new_path):
            if f == filename:
                copyfile(master, new_path)
                print("Copied to", new_path)
        else:
            sync_files(new_path, master, filename)

def main():
    print(f"Copying from \"{MASTER}\" to all files named \"{ZAPIER_DEFAULTS}\"")
    print()
    sync_files(PATH, MASTER, ZAPIER_DEFAULTS)

if __name__ == "__main__":
    main()