''' ------------OOP terms and Principle--------
- Class : A blueprint for creating objects of a particular type
- Methods: Regular functions that are part of a class
- Attributes: Variables that hold data that are part of a class
- Object: A specific instance of a class
- Inheritance: Means by which a class inherit capabilities from another
- Composition: Means of building complex object out of other objects
'''

# create a basic class. Since class doesn't inherit from other class
# we can leave out the paranphesis
class book:
    pass

# Create instance of book class
b1 = book()  

#---------Another class example 
class Stadiagames:

    # Let's override the init function
    '''
    __init__() is a special Python function that when a class is created,
    it initialize the new object with information (but it is not a constructor)
    & it is called before any other function in the class
    '''
    def __init__(self, title):
        self.title = title

# Create instance of book class
firstgame = Stadiagames("Brave New World") 
secondgame= Stadiagames("War on Peace")
thirdgame = Stadiagames("Death by Daylight")
fourthgame= Stadiagames("Destiny 2")      

# Lets access the value of the properties with the dot notation

print("\n\n")
print("Current Free Games on Stadia : ")
print(firstgame) #print object location
print(firstgame.title) # print object data
print(secondgame.title)
print(thirdgame.title)
print(fourthgame.title)

print("\n")