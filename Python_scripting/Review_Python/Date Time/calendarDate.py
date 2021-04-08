#------------- Working with Calandars in Python 

# import the calandar module
import calendar

print("\n")

# Create a plain text calandar with Sunday as the first day of the week
#c = calendar.TextCalendar(calendar.SUNDAY) 

# c = calendar.TextCalendar(calendar.MONDAY) # Monday to be 1st day of the week 
# st = c.formatmonth(2021, 1, 0, 0)
# print(st)

print("\n")


# # create an HTML formatted Calandar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2021, 1)
# print(st)

# print("\n")

# Loop over days of a month
# zeroes mean the day of the week is in an overlapping month
# c2 = calendar.TextCalendar(calendar.SUNDAY) 
# for i in c2.itermonthdays(2021, 1):
#     print(i)

# The Calandar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms

print("-------Months:------")
for name in calendar.month_name:
    print(name)

print("\n")
print("--------Days-----")


for day in calendar.day_name:
    print(day)
