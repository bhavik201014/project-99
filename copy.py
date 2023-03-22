import os
import shutil

source = input("enter source folder: ")

dest = input("enter dest folder: ")

source = source + "/"

dest = dest + "/"


list_of_files = os.listdir(source)

for file in list_of_files:
    shutil.copy((source + file),dest)




