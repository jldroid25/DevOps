
#-------- in python we define a function with the word "def" -------#

print("\n\n")

def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

# call the function with the  required parameter's values
cylinder_volume(10, 3)

# function with a default param value, if the param is not defined 
# when the function is called , the default value will be used
def cylinder_volume2(height, radius = 5):
    pi = 3.14159
    return height * pi * radius ** 2

#This function call will have 10 & 5 for redius(the default parameter value)
print(cylinder_volume2(10)) # 782.8975

print("\n")

#-----------Function for a readabled_timedelta

def readabled_timedelta(days):
    
    # use integer division to get the number of weeks
    weeks = days // 7

    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s) .".format(weeks, remainder)

# test your function
print(readabled_timedelta(10))



'''
# Python doesn't allow function to manipulate global variable directly.
# this will cause an error.
# A solution would be to to use global var as a param in function definition
# assign it to another function on function call.

egg_count = 0

#def buy_eggs():
 #   egg_count += 12 # purchase a dozen eggs

# buy_eggs()
'''

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()

print("\n\n")


#-------DocString Example for your functions --------------#
def readable_timedelta4(days):
    """Return a string of the number of weeks and days included in days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

# Example 2
def readable_timedelta5(days):
    """Return a string of the number of weeks and days included in days.

    Args:
        days (int): number of days to convert
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

# Example 3
def readable_timedelta3(days):
    """
    Return a string of the number of weeks and days included in days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

