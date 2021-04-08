# Working with date & time
# Let's just/only import the class we need (date, time & dateTime)
from datetime import date
from datetime import time
from datetime import datetime 


def main():

    # Date OBJECTS:

    # # Get today's date from the simple today() nethod from the date class
    # today = date.today()
    # print("Today's date is : ", today)


    # # print out the date's individual components
    # print("Date components: ", today.month, today.day,  today.year)


    # # retrieve today's weekday  (0=Monday, 6=Sunday)
    # print("Today's weekday number is:", today.weekday())

    # # we can use this on a list with days value name
    # days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    # print("Which is a: ", days[today.weekday()])


    print("\n")
    
    ## DATETIME OBJECT
    # Get today's date from the datetime class

    # Using the now function will give us the current date & time
    today2 = datetime.now()
    print("Current date & time is: ", today2)

    print("\n")

    # Get the current time.
    currentTime = datetime.time(datetime.now())
    print("Current Time is:",currentTime)


if __name__ == '__main__':
    main()
            