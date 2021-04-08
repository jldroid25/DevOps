
'''
#---------- Defining Data Class -----------------#
Check out Python doc on Data Classes for more info
Fyi: data classes only works on python version 3.7 & later. So check before use
Using data classes to represent data object.

So Dataclasses allows you to write more consise code and skip alot of
boilerplate code you get by using __init__() & self. 

They are just regular python classes you can use them as any other python class

'''
# 1 : import dataclasses module
from dataclasses import dataclass

#2 : add the decorator
@dataclass
# inside the class get rid of __init__() & all the self keywords before attribute
# behind the scene python is using __init__() for our data
class Book:
    title  : str
    author : str
    pages  : int
    price  : float

    def bookinginfo(self):
        return f"{self.title}, by {self.author}"
    
    

# create some instances
b1 = Book("Brave new World", "Aldous Huxley",1225,  39.95 )
b2 = Book("Catcher in the Rye", "JD Salinger ", 234, 29.95)
b3 = Book("Brave new World", "Aldous Huxley",1225,  39.95 )

print("\n\n")

# access field
print(b1.title)
print(b2.author)

# Print the book itself - dataclasses implement __repr__
#print(b1)

# Compare two dataclasses - they implement __eq__
#print(b1 == b3)

# Change some fields
b1.title = "Anna Karenina"
b1.pages = 864

print(b1.bookinginfo())