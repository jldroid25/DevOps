'''
# the __post_init__() function lets us customize additional properties
    # after the object has been initializes via built-in __init__()

 # -------- Using Post initialization function ---------------

'''

# -----Using the postinit function in data classes----
from dataclasses import dataclass

@dataclass
class Book:
    title  : str
    author : str
    pages  : int
    price  : float

    # the __post_init__() function lets us customize additional properties
    # after the object has been initializes via built-in __init__()
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


# create some instances
b1 = Book("Brave new World", "Aldous Huxley", 1225,  39.95 )
b2 = Book("Catcher in the Rye", "JD Salinger ", 234, 29.95)
b3 = Book("Election Notice", "James Comey",353,  59.95 )

print("\n\n")

# use the description attribute
print(b1.description)
print(b3.description)

print("\n\n")