# ------- Inheritance in Python --------------#

'''
class Book:
    
    # Let's override the init function

   # __init__() is a special Python function . __init__() is called when
    #the instance is created and ready to be initialized
    
    def __init__(self, title, author, pages, price):
        # TODO: add properties (AKA instance attribute)
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages

class Magazine:

    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.publisher = publisher
        self.period = period

class Newspaper:

     def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.publisher = publisher
        self.period = period

'''

'''
If you noticed there are duplicates in the code/classes attributes above.
for price, author, publisher , & title.
We can impove the code with inheritance to reduce duplication.

'''

# let's first create a base class call publication that have title & price attributes

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

# Let's do the same for Newspaper Class and Magazine class by
# creating a Periodical class
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.publisher = period
        self.periord = publisher


# now let's the Book class inherit attributes from Publication class 
# by passing it as a parameter
class Book(Publication):
    
    def __init__(self, title, author, pages, price): 
        # Now we need to call the super() to access the Parent class attributes
        super().__init__(title, price)
        # now we only need to create new attributes
        self.author = author
        self.pages = pages

# Now Define our class to inherit from based-class Periodical
class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):

        super().__init__(title, price, period, publisher)

# Now Define our class to inherit from based-class Periodical
class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):

        super().__init__(title, price, period, publisher)

        
b1 = Book("Brave new World", "Aldous Huxley", 311 , 29.0 )
n1 = Newspaper("NTTimes", "New Yopk Times Company ", 6.0 , "Daily"  )
m1 = Magazine("Scientific American", "Spring Nature ", 5.99 , "Monthly" )

print("\n\n")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)

print("\n")