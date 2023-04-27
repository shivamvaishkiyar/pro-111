import os 
import shutil

from_dir = "C:/Users/ADMIN/Downloads"
to_dir = "C:/WhiteHatJr/"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for files_name in list_of_files:
    name,extension =os.path.splitext(files_name)
    print(name)
    print(extension)