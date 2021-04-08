from abc import ABC, abstractclassmethod
'''
# -----Using Abstract Base class to enforce class constraints --------

With Abstract Base Class we want to provide a base class that other classes 
inherit from but with a couple twist . 

1- classes that will inherit from this Abstract should not or cannot created
instances of the abstrac class itself.  because this is intended to be a blueprint 
or an idea  for sub-class & not to be used directly .

2- Also there are certain Super/Base methods we want inherited class to implement
in their own classes.

# so to prevent direct instantiation from the Base/superclass we will use the Python 
ABC modules & the Abstractmethods above (first line)

Why use abstact methods?:

- Abstract methods can be used to inforce some constraints to the 
consumer of your base-class instances to force them to provide their own version
of it & implement a required PArent class method(s)
'''



class GraphicShapes(ABC):
    def __init__(self):
        super.__init__()

    # use this decorator to indicate calcArea() is an abstract method
    # this is no implementation base-class & each subclass must implement
    # it's own version ro override this method
    @abstractclassmethod
    def calcArea(self):
        pass

class Circle(GraphicShapes):

    def __init__(self, radius):
        self.radius = radius

   # Now let's override the abstrac calcArea() from Base-Class 
   # with our own version of it  for the subclass Circle()
    def calcArea(self):
        return 3.14 * (self.radius ** 2)

# Now let's override the abstrac calcArea() from Base-Class 
   # with our own version of it  for the subclass square()

class Square(GraphicShapes):
    
    def __init__(self, side):
        self.side = side

    def calcArea(self):
         return self.side * self.side 

print("\n\n")
# Let's try direct instantiation of the abstract class
# this cause an error
#g = GraphicShapes()

c = Circle(10)
print(c.calcArea())

s = Square(12)
print(s.calcArea())


print("\n\n")