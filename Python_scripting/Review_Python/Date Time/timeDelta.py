# Exampole file for working with time Delta objects

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# ------- Working with Time Delta -----------
# Time Delta is a span of time. It is not a particular date or time . 
# So we can use this class to perform time-based mathematics.
# i e if you wanted to let a user know a future date to expect a 
# later/response/document from your organization. 

# print("\n")

# # construct a basic time delta & print it
# print(timedelta(days=365, hours=5, minutes=1))
# print("\n")

# # print today's date
# now = datetime.now()
# print("today is: " + str(now))
# print("\n")

# # print today's date one year from now
# print("one year from now it will be: " + str(now + timedelta(days=365)))
# print("\n")

# # Create a timeDelta that uses more than one argument
# print("In 2 days and 3 weeks, it will be: " + 
# str(now + timedelta(days=2, weeks=3)))

# print("\n")

# # claculate the date 1 week ago, formatted as a string 
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime("%A, %B, %d, %Y")
# print("One week ago it was: " + s )
# print("\n")

# A script to calculate How many days until April Fools' day (afd)

today = date.today()
afd = date(today.year, 4, 1)

# Check if AFD for this year is already passed
if afd < today:
    print("April Fool's Day already went by %d days ago" % ((today - afd).days))
    # If it has passed, used the replace() 
    # to get next year's April Fool Day
    afd = afd.replace(year = today.year + 1)

# Now calculate the amount of time until April Fool's Day
time_to_afd = afd - today
print("It's just ", time_to_afd.days, "days until April Fool's Day")


