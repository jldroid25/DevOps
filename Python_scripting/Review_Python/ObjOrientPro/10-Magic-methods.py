'''
Magic Methods are a set of methods that  are automatically
associated with every class definition .

Your class  can also override them to 
 1- Customize object behavior and integrate with the language
 2 - Define how objects are represented as string 
 3 - Controll access to attribute values, both for get and set
 4 - Build in comparizzon and equality testing capabilities
 5 - Allow object to be called like functions


'''

#----------- Magic Methods String Representation ----------------#

'''
# using __str__ and __repr__ magic methods

class Book:
    
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.price = price
        self.author = author
    
    # using __str__  method to  return a string 
    # pronounce (stir)
    def __str__(self):
        return f" {self.title} by {self.author}, costs {self.price} "


    # using __repr__  method to  return an object representation
    # pronounce (reper) is commonly use for debuging purposes

    def __repr__(self):
        return f"title={self.title}, author={self.author}, costs {self.price}"

b1 = Book("Brave new World", "Aldous Huxley", 29.0 )

b2 = Book("Catcher in the Rye", "JD Salinger ", 29.95)

print("\n\n")

print(b1)
print(b2)

print("\n")

print(str(b1))
print(repr(b2))
print("\n")

'''



'''
#----------- Magic Methods Equality and comparison ----------------#

Plain object in Python by default  don't know how to compare
themselves to each other , but we can teach them how to do so
by using the equality and comparison Magic methods



class Book:
    
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.price = price
        self.author = author
    
    #Better way to test/check object equality is with __eq__()
    # Check for greater than and lesser than 

    # the __eq__ method checks for equality between two objects 
    def __eq__(self, value):

        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")

        return(self.title == value.title  and 
        self.author == value.author and  
        self.price == value.price)

    # the __ge__ method establishes >= relationship with another obj
    def __ge__(self, value):
    
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")

        return self.title >= value.title  

     # the __lt__ method establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")

        return self.title < value.title  


b1=  Book("Rubicon", "Kiera indy", 300.01 )
b2 = Book("Catcher in the Rye", "JD Salinger ", 29.95)
b3 = Book("Rubicon", "Kiera indy", 300.01 )
b4 = Book("EuphoriaG", "Skye Heaven", 250.00 )

# Check for Equality
print("\n\n")

#This will yield False because Python compare Object Memory locations not it's values
#print(b1 == b3) 
#print(b1 == b2) 

#print(b1

# Let's try some less than comparison
#print(b2 >= b1) 
#print(b2 < b1) 

# Now we can sort them to
books = [b1, b3, b2, b4]
books.sort()
print([book.title for book in books])

# for further info checkout the Python doc section "special methods"
print("\n\n")

'''

'''

#----------- Access Atributes ----------------#


class Book:
    
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.price = price
        self.author = author
        self._discount = 0.1
    
    # using __str__  method to  return a string 
    # pronounce (stir)
    def __str__(self):
        return f" {self.title} by {self.author}, costs {self.price} "


    # using __repr__  method to  return an object representation
    # pronounce (reper) is commonly use for debuging purposes

    def __repr__(self):
        return f"title={self.title}, author={self.author}, costs {self.price}"

    # __getattribute__ called when an attr us retrieved .
    # Caution Do not directly access the attr name otherwise a recursive loop
    # is created.

    #Example: let's override this method so that we can apply a discount
    # whenever the price attribute is retrieved/accessed

    '''

'''
    
    # comment out to test __getattr__()
    def __getattribute__(self, name):

        if name == "price":
            #using the super() class to get the attrobute price & discount
            #  otherwise if we get it  diretly by name  we will 
            # get a recursion that crash the app.
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p  * d)
        # if we not operate on the attribute(s) just return the name
        return super().__getattribute__(name)
    


    # __setattr__ called when an attribute valye is set .
    # Caution Do not set it directly here  otherwise a recursive loop
    # is created.

    #Example: Let's make sure when the price is set the caller function
    # is using a floating point number.
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attr must be a float")
        return super().__setattr__(name, value)


     # __getattr__ called when __getattribute__ lookup fails You can .
    # Pretty much create attributes on the fly with this method
    def __getattr__(self, name):
        return name + " is not here"




b1 = Book("Brave new World", "Aldous Huxley", 39.95 )
b2 = Book("Catcher in the Rye", "JD Salinger ", 29.95)

# to test __getattribute__() 
#b1.price = 38.95
#print(b1)

#  to test __setattr__()
#b2.price = float(40)
#print(b2)

#  __getattr__() will create attribute on the fly
print(b1.randomprop)

'''
#---------- Callable Objects ------------#

class Book:
    
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.price = price
        self.author = author
        
    
    # using __str__  method to  return a string 
    # pronounce (stir)
    def __str__(self):
        return f" {self.title} by {self.author}, costs {self.price} "

    # the __call__ method can be used to to call the object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.price = price
        self.author = author



b1 = Book("Brave new World", "Aldous Huxley", 39.95 )
b2 = Book("Catcher in the Rye", "JD Salinger ", 29.95)

print("\n\n")

# let's call the object as if it were a function
print(b1)

b1("Anna Karenina", "Leo Tolstoy", 49.95)
print(b1)

print("\n\n")