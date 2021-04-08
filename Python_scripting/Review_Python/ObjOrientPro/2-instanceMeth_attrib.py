#----------Inheritance in Python ---------------#

class Stadiagames:
    
    # Let's override the init function
    '''
    __init__() is a special Python function . __init__() is called when
    the instance is created and ready to be initialized
    '''
    def __init__(self, title, company, developer, price):
        # TODO: add properties (AKA instance attribute)
        self.title = title
        self.company = company
        self.developer = developer
        self.price = price

        '''
        IN python we can use a double underscore infront of an attribute
        to prevent other and subclasses from accessing it
        '''
        self.__secret = "This is a secret"

    # now lets add an instance methods
    #  method for for the  price that take the "object" as argument
    def getprice(self):
        '''
        Since setdicount() may not be called when we need it
        let's test/check if it is there by using the "hasattr() function
        '''
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
           return self.price

    def setdiscount(self, amount):
        '''
        the underscore "_discount" is a hint to other developers to let them know 
        this is internal attribute to the class & cannot/shouldn't be access out
        side of the class. 
        '''
        self._discount = amount

# Create instance of book class
firstgame = Stadiagames("Death by Daylight", "Ubisoft", "DAve Marino", 59.99) 
secondgame= Stadiagames("Lola 2 Brat","Euphoria-Soft", "N-Princess", "$250")

print("\n\n")
# Let's call the getprice() instance method
#print("Current Price: ",firstgame.getprice())

# Try to set a discount 
firstgame.setdiscount(0.25)
print("Discounted Price with 25% off: ",firstgame.getprice())


#print("Expensive Stadai Pro Games: ")
print(firstgame.title)

#This will give an AttributeError due to double underscore in attribute's name
#print(secondgame.__secret)
#  but we can access it with the classname__secret
#print(secondgame._Stadiagames__secret)

print("\n")