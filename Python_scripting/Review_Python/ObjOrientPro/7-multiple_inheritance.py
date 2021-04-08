'''
Unlike other Programing languages Python allows sub-classes to inherit from 
multiple Base/Parent Classes. 

But if not careful this can cause a lot's of problems.
'''

class A():

    def __init__(self):
        super().__init__()
        self.foo = "foo"
        #Define the same attribute name as class B
        self.name = " Class A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"

        #Define the same attribute name as class A
        self.name = " Class B"
        

# multi-inheritance 
class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)

        '''
        Now the problem we encounter is python will attribute "name" for class "A" first
        Since it is the first one listed as an argument in Class "C".

        Python use something call "Method-Resolution-Order" to look up obejct
        to acces first so in Class-C it will accesss "foo", "bar", & then "class A"
        since it is listed first(left to right) as a param in the Class C(A, B):  

        We can actually inspect the "Method-Resolution-Order" with the 
        ___mro__ class attribute
        '''
        print(self.name)


# the problem comes when both superclasses define the same attribute
#     
print("\n\n")

# instantiate a C Objects of Parent Class
c = C()

# now lets call showprops()
c.showprops()

# Let's inspect the C-class "Method-Resolution-Order" with the 
print(C.__mro__)

# now notice the order of objects on the display
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

# Because of this added complexity , we don't see multi-inheritance often in python codes
# the only place we get to see them a lot is in "interface"
# see next lesson

print("\n")