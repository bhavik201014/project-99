import os
import shutil
a=input("enter your source folder:")
b=input("enter your destination folder:")
a=a+"/"
b=b+"/"
c=os.listdir(a)
for i in c:
    shutil.move((a+i),b)