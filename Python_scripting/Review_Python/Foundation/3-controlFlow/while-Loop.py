# ----- Working with While Loop------------- 
# For-loops are "defined Iteration" (body of loop runs for specified # of time) 
# whereas while loops are "indefined iteration" (loop runs for an unknown # times
# & ends when some condition is met.).
print("\n\n")

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = [] 

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more

#While-loop | Condition to be checked
while sum(hand) < 17:
    #code to be executed if condition above is true until it becomes false
    hand.append(card_deck.pop())


# ----------------Finding FActorials of 6 with while loop

# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

#track the current number being multiplied
current = 1

while current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1

#Print the factorial #
print(product)


print("\n")

# ----------------Finding FActorials of 6 with For-loop
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# calculate factorial of number with a for loop
for num in range(2, number + 1):
    product *= num

# print the factorial of number
print(product)

# With Loops we can use the "break" to abrutly terminate the loop.
#  But we can also used the "continue" statement 
# (Terminates one iteration of a for or while loop) to skip ietration when on a condition
# becomes and keep going with  rest of loop until main condition becomes false.
# it is also recommened to use print-statement for debugging on your loop.

# the code breaks the loop when weight exceeds or reaches the limit
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break # Leave loop immediately
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))


print("------------------------------------------------")

check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break

# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:    
            print("{} IS a prime number".format(num))


'''
Zip() returns an iterator that combines multiple iterables into one sequence of tuples.
Each tuple contains the elements in that position from all the iterables. 
For example, printing.

Like we did for range() we need to convert it to a list or iterate through it with a loop to see the elements.

You could unpack each tuple in a for loop like this.

'''
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letters, num in zip(letters, num):
    print("{}: {}".format(letters, num))

# In addition to zipping two lists together, 
# you can also unzip a list into tuples using an asterisk.

some_list = [('a', 1), ('b', 2), ('c', 3)]

letters, num = zip(*some_list)

'''

Enumerate:
enumerate() is a built in function that returns an iterator of tuples 
containing indices and values of a list. 

You'll often use this when you want the index along with each 
element of an iterable in a loop.

'''
letters = ['a', 'b', 'c', 'd', 'e']

for i, in letters in enumerate(letters):
    print(1, letters)

#-------- More Practice with Zip() & Enumarate()  --------------#

#Zip Coordinates

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)


#Zip Lists to a Dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

# Unzip Tuple
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)
print(names)
print(heights)


cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)

print("\n\n")

