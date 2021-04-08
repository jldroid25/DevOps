#  Formatting Time and date output

from datetime import datetime


def main():

    # Time & dates can be formatted using a set of predefined string control codes

    now = datetime.now()
    # using the strftime() to format datetime object. 
    # This function  take a string arguments
    #print(now.strftime("The current year is: %Y"))
   

    #------- Date Formatting --------#

    # %y/Y% - Year, %a/A% - weekday,  %b/B%  - month, %d - day of month
    #print(now.strftime("%a, %d, %B, %y"))
     
    print("\n")
    # %c - locale's date and time,  %x - locale's date, %X - locale's time 
    print(now.strftime("Localte date & time: %c"))
    print(now.strftime("Localte date: %x"))
    print(now.strftime("Localte time: %X"))

    print("\n")

    
    
    # ------- Time Formatting  -----

    # %I/H% -  12/24 Hour, %M - minute, %S  - second, % - locale's AM/PM
    print(now.strftime("Current Time: %I:%M:%S %p"))
    print(now.strftime("24-Hour Time: %H:%M"))

    print("\n")



 
if __name__ == "__main__":
        main()