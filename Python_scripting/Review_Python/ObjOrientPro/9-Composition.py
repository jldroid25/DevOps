'''
IN Python using simple Object to create complex one 
is called "Composition"

The basic idea with composition is  to have each object defines
its own data and each separate object a composition together to create a 
a complex one. 

Therefore composition has a "has-type-relationship" objects to object.
Whereas classic Base class/subclass inheritance has a "is-type-relationship"


# if you notice this is a "Is-type Ralationship "
# We can use composition to have a "has-type relationship"
# defining separate objects has a whole object
class Book():
    def __init__(self, title, price, authorfname, authorlname):
        self.title = title
        self.price = price

        # we can treat this as a separate entity 
        # We might want have group of authors
         # so this make a good candidate for composition
        self.authorfname = authorfname
        self.authorlname = authorlname

        #to build a list of chapters
        self.chapters = []

    # we might also want a specific chapter
    # so this make a good candidate for composition
    def addchapters(self, name, pages):
        self.chapters.append((name, pages))

# Create Book Objects & add some Chapters to the list
b1 = Book("War and Peace ", 39.0, "Leo", "Tolstoy")

b1.addchapters("chapter 1", 125)
b1.addchapters("chapter 2", 97)
b1.addchapters("chapter 3", 143)


'''
# ------Rewrite as a Composition so Base class can have a "has-type relationship" -----------#


# now our Book now "has" a collection of authors and chapters
class Book:
    def __init__(self, title ,price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

     # to add chapters to the list
    def addchapters(self, chapter):
        self.chapters.append(chapter)

    #Book can calculate its own page count
    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

# Let's start by extacting the author in its own class
class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    #Using magic method to override the string method & using format()
    # see next lesson on magic method
    def __str__(self):
        return f"{self.fname} {self.lname}"

# a Separate chaper class
class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

print("\n\n")
    
# Create Book Objects & add some Chapters to the list
auth = Author("Leo", "Tolstoy")

b1 = Book("War and Peace ", 39.0, auth)

b1.addchapters(Chapter("chapter 1", 125))

b1.addchapters(Chapter("chapter 2", 97))

b1.addchapters(Chapter("chapter 3", 143))

print(b1.author)
print(b1.title)
print(b1.getbookpagecount())

print("\n\n")