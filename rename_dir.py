import os
generic_name = "{project_name}"

subdirs = []
from pathlib import Path
def rename_project(src):
    for subdir, dirs, files in os.walk(src,topdown=False):
        subdirs.append(subdir)

    for subdir in subdirs:
        print(subdir)
        path = Path(subdir)
        og_directory_name = os.path.basename(subdir)
        parent_path = path.parent.absolute()
        if "localhost" in og_directory_name:
            new_directory_name = og_directory_name.replace('localhost', 'tahd')
            newdir =  str(parent_path) + os.sep + new_directory_name
        # print newdir
            os.rename(subdir, newdir)

rename_project("/home/jtrevino/sos-test-2")
