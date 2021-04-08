
# Example file for working/Using File system shell Methods

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile
import datetime
from datetime import date, time, timedelta
import time


def main():
    # make Duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        # Let's make a backup copy by appending "devopSReE" to the file name
        dest = src + ".devopSRE"

        # copy over the permission with shutil, modification times, & other info
        # shutil.copy(src, dest)

        # # Using copystat() to copy over file meta data i,e date modified etc.
        # shutil.copystat(src, dest)

        # # Check/verify file metadata for time modified
        # td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
        # print("It has been " + str(td) + " since the file was modified")

        # rename the original file
        # os.rename("textfile.txt.devopSRE", "awsEc2DevopSRE.txt")

        # now put things/content of dir in  a zip archive 
        # We will use the shell methods make_archive()

        # 1 -  get the dir path for the file with split()
        root_dir, tail = path.split(src)

        # 2 - call the make_archive() with desired name, desired format (zip)
        # & pass it root directory to we need to compress
        # note this will archive every thing in the directory
        # shutil.make_archive("DevopsProjectArchive", "zip", root_dir)


        # More fine-grained control over ZIP files
        # 1-  use the "with" keyword to define a local scope to 
        # simplify working with objects. 
        # So Create a new zip file, with we write mode, & use the object
        # to manipulate or add data/file(s) to the new archive
        with ZipFile("BetterDevopsProjArchive.zip", "w") as newzip: 
            newzip.write("awsEc2DevopSRE.txt")
            newzip.write("awsCodeEKS")
            newzip.write("infra-aws.txt")


        #---------- my solution -----------
        #  get the path to the file in the current directory
        # print("File Location in directory: " + str(path.isdir("textfile.txt")))
        # # Let's make a backup copy by appending "devopSReE" to the name
        # f = open("textfile.txt", "a")
        # # copy over the permission, modification times, & other info
        # for i in f:
        #     f.write("DevopSRE" + str(i) + "\r\n")
        #     print("textfile.txt")
        # f.close()

        # rename the original file

        # now put things/file in  a zip archive 



if __name__ == "__main__":
    main()