# Using class-level and static methods

class Book:
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # double-underscore properties are hidden from other classes
    __booklist = None
  
    # create a class method that returns booktype list
    # we are using a decorator @classmethod
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # create a static method
      # --------------- static Method to create a singleton 
    # (only one instance of a particular variable or object is ever created)
    @staticmethod
    def getbooklist():
        #if no book list yet create one
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods received a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
         # values the class Book allows
        if (not booktype in Book.BOOK_TYPES):
             raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


# Access the class attribute
print("Book types: ", Book.getbooktypes())
# Create some book instances

b1 = Book("Canada Poppy Sugar", "HARDCOVER")

#Will give an error , comic is not one of predefined book types
#b2 = Book("Montreal Swetten Treats", "COMIC")
b2 = Book("Montreal Swetten Treats", "EBOOK")

# use the static method to access a singleton object
'''
Static methods don't modify the state of either the class or 
a specific object instances. There not great cases for static methods
They are useful, however for scenarios when you don't need to access
any properties of a particular object or the class itself.
This is a way of taking a global function and put it the class namespace.
'''
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
