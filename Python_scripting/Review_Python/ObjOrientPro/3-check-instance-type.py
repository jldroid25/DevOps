
# -----------Check Class types and instances -------------
'''

'''

class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name

# Create instance of book class
b1 = Book("Brave New World") 
b2 = Book("War on Peace")

N1 = Newspaper("New York Times")
N2 = Newspaper("Washington Post") 

#Use type() to inspect the object type

#print(type(b1))
#print(type(N1))

# Option-1 for  to compare two objects are the same types
#print(type(b1) == type(b2))
#print(type(b1) == type(N2))

#Better --> Option-2 check using built-in isinstance() to check/compare types of objects
print(isinstance(b1, Book))
print(isinstance(N1, Newspaper))
print(isinstance(N2, Book))

#Since in Python every classes is a sub-class of the "Object" type
# Let's also check if (our b & N objects) are of the same type
print(isinstance(N2, object))
print(isinstance(b2, object))
