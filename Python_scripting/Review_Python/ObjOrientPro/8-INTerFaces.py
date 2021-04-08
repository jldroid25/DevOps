from abc import ABC, abstractclassmethod

'''
An interface is a contract between the subclass an the Interface class
which dictate if you imvoke/implement me as an interface 
you must override the interface's defined methods in your code.

Interface helps us reducing further code duplications in Parent- Class and
sub-classes in inheritance

Example:
If we wanted to return the result of CalcArea() as a Json representation of object
We could  define a jsonify() in the Super class ans an abstract class
now every sub-class must implement it.

The problem here if a sub class doesn't need it they still have to implement it.

However, we can create an interface and any subclass that need that particular 
function can do a "Multi-Inheriatnce" for just that one sub class & override that
interface's method

'''

# Let's define an Interface 
# notice it is not part of the super class Graphicshapes.

class JSonify(ABC):
    @abstractclassmethod
    # define interface class that must be implemented by inherent sub-class
    def toJson(self):
        pass

class GraphicShapes(ABC):
    def __init__(self):
        super.__init__()

    # use this decorator to force class_bastraction rules
    @abstractclassmethod
    def calcArea(self):
        pass

class Circle(GraphicShapes, JSonify):
    def __init__(self, radius):
        self.radius = radius

   # Now let's override the abstrac calcArea()
    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    # Let's implement the  interface method toJson()
    def toJson(self):
        return f"{{\" Circle\" :  { str(self.calcArea()) } }}" 

print("\n\n")

c = Circle(10)
print(c.calcArea())

print(c.toJson())

print("\n\n ")

