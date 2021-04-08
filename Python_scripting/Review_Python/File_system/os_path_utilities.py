# 
# Example file for working with Os.path module
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the Operating system

    print("\n")

    print(os.name)

    print("\n")

    # Check if an item exists & its type( file, dir)
    # print("\n")

    # print("Item exists: " + str(path.exists("textfile.txt")))

    # print("Item is a file: " + str(path.isfile("textfile.txt")))

    # print("Item is a directory: " + str(path.isdir("textfile.txt")))
    
    # print("\n")
    
    # Work with file paths : 
    print("\n")

    # Get Item full path
    # print("Item path: " + str(path.realpath("textfile.txt")))
    
    # Let's also separate with split() Item name from its path
    # print("Item path and name" +  str(path.split(path.realpath("textfile.txt"))))

    # print("\n")
    
    # Get the some information on a file modification time 
    # print("\n")
    # t = time.ctime(path.getmtime("textfile.txt"))
    # print("File was modified on: " +  t)

    # # Another way of accomplishing the same thing
    # # Let's also build a date time object with 
    # print("File Modification on: ",   datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago the item or file was modified:

    print("\n") 
    
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been " + str(td) + " since the file was modified")
     
    #  Let's print for total seconds
    print("Or, " + str(td.total_seconds()) + " Total seconds")

    print("\n") 

if __name__ == "__main__":
    main()