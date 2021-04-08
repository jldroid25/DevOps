
# Implementing default values in data classes
# Beside the default value below we can also 
# we can also use the "yield" function to provide more flexibility

# -----Using the postinit function in data classes----
from dataclasses import dataclass, field
import random


# a function to return a random price
def price_func():
    return float(random.randrange(20, 40))

@dataclass
class Book:
    # you can define default values when attributes are declared
    title  : str = "No Title"
    author : str = "No Author"
    pages  : int = 0
    #price  : float = 0.0
    #price  : float = field(default=10.0) # using yied()
    
    # We can also use the default_factory()
    price  : float = field(default_factory=price_func)

    # FYi attribute(s) without any value will come first in dataclasses
    # this will give an error
    #price  : float  

# now we can create a book with no arguments & printed it out
print("\n\n")

b1 = Book("Brave new World", "Aldous Huxley", 1225,  39.95 )
b2 = Book("Election Notice", "James Comey",353)

b1 = Book()
print(b1)
print(b2) # now we will get random prices for b2

print("\n\n")