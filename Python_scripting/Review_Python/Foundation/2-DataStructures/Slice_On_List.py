# Slice and Dice with Lists

#You saw that we can pull more than one value 
# from a list at a time by using slicing. 

'''When using slicing, it is important to remember that the lower 
index is inclusive and the upper index is exclusive.
'''
list_of_random_things = [1, 3.4, 'a string', True]
# start slicing at 2nd element of list upto 3rd element

print("\n start slicing at 2nd element of list up to 3rd element\t:", 
list_of_random_things[1:2] , "\n\n") 

#If you know that you want to start at the beginning, 
# of the list you can also leave out this value & only include last one.
# here we'ew saying do not include 1rst element
print(list_of_random_things[:2])

# or to return all of the elements to the end of the list, 
# we can leave off a final element.

print(list_of_random_things[1:], "\n\n")

# Using "in" or "not in" to return a bool of whether an element exists within our list.
# if a string is a sub string of another
my_strings = 'this' in 'this is a string'

my_other_var = 5 not in [1, 2, 3, 4, 5, 6, 10]

my_other_var_two = 5 not in [1, 2, 3, 4,  6, 10]

print( my_strings, "\n")
print(my_other_var, "\n")
print(my_other_var_two, "\n")

print("\n\n")