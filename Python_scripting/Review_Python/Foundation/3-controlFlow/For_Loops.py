# Loops allow us to repeat a block of code(s)
# in Python there are two Kinds for-loop & while loop.

''' 
For-Loop is use to iterate of an "iterable" which is an object
that can return one of its elements at a time.
'''
print("\n\n")

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

# A for loor to extract data from a List
for city in cities:
    print(city.title())

print("\n")

#  A for loop to create a List

# start with an Empty List
capitalized_cities = []

# now let's loop to create the Cap. cities
for city2 in cities:
    capitalized_cities.append(city2.title())

    print(capitalized_cities)

print("\n")

# Using a For-Loop to Modify an existing List
# It requires the  function range(start, stop, step) 
# syntax for ---> range(start, stop, step)
#FYI: to view/print the values of the modifyied data from range() function.
# we can also use range() to repeat an action a coertain # of times.
# you must use a list to print the data.

for index in range(len(cities)):
    cities[index] = cities[index].title()
    print(index)# print the index 0, i , etc
    print(cities[index]) # print each city name be long to that index.

print("\n")
for i in range(5, 35, 5 ):
    print(i)


print("\n\n")

# More Practices

sentence = ["the", "quick", "brown","fox","jumped","over","the", "lazy", "dog"]

for word in sentence:
    print(word)


print("\n\n")

# Modify user names with range()
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)

print("\n\n")

# Count number of token  "<"  (pieces of string) to see if
# if each string begins with an angle brackets

tokens = ['< greeting>', 'Hello World!', '</greeting> ']

count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
print(count)


print("\n\n")

# Create an HTML List
items = ['first string', 'second string']
html_str = "<ul>\n"  

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

print("\n---------------------------------------------------------")

# Using for-Loop to create a dictionary

book_title =  [
    'great', 'expectations','the', 'adventures', 'of', 
    'sherlock','holmes','the','great','gasby','hamlet','adventures',
     'of','huckleberry','fin'
]

# create an empty dictionarry
word_counter = {}

'''
 Iterate through each element in the list. If an element is already 
 included in the dictionary, add 1 to its value. If not, 
 add the element to the dictionary and set its value to 1.
'''

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)



print("\n")

# Second Way
for word2 in word_counter:

    word_counter[word2] = word_counter.get(word2, 0) + 1

print("\n\n")


print("\n---------------------------------------------------------")

# use item() to iterate over Keys and values, 
# items() returns tuples of key, value pairs which you 
# use to iterate over dictionaries in for loops

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for key in cast:
    print(key)

print("\n")

for kev, value in cast.items():
    print("Actor: {}  Role: {}".format(key, value))

print("\n-----------------------------------------")
# Count number of fruits in a dictionary
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
   if object in fruits:
       result += count

print("There are {} fruits in the basket.".format(result))

print("\n\n")



print("\n-----------------------------------------")




