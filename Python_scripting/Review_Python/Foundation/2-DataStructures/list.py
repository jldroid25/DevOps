

''' Data structures are containers that organize 
and group data types together in different ways. 

A list is one of the most common and basic data structures in Python.

- So A List is a data type for mutable ordered sequences of elements.

'''
# Here is an Example of List of Strings '''

months = ['Jan','Febb','March','April','May','June',
         'July','Aug','Sep','Oct','Nov','Dec']

#print( "\n\n",  months)

# List have orders & we can target their elements like an array.
print("\n\n ----- From January to May----- \n")

print(months[0])
print(months[1])
print(months[2])
print(months[3])
print(months[4])

# Using - or negative sign to target last elements on a List
print("\n\n ---- From December to July------  \n\n")
print(months[-1])
print(months[-2])
print(months[-3])
print(months[-4])
print(months[-5])
print(months[-6])

#The same as above 


print("\n\nA list with any mix and match of the data type:")
# We mixing integer, string & boolean in our list
list_of_random_things = [1, 2, 3,  4, ' mix with a string ', True]
print(list_of_random_things , "\n")

'''
Why Do We Need Lists?
Let's talk about why we need a data structure like a list or when to use it.
 We will borrow an example from the world of Wall Street for this discussion.
'''

NYSE_Stock_stikers = ['GOOGL', 'APPLE','TESLA', 'ALPHA', 'MICROS']

print(NYSE_Stock_stikers)
myTechInvestmentStock = 'TESLA' in NYSE_Stock_stikers
print("Is TESLA in NYSE STock Exchange LISt:", myTechInvestmentStock)
print("My Most Valuable Stock is:", NYSE_Stock_stikers[2:3])
