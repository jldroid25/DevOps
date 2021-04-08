# Dictionary :
''' 
A Data Type for mutable object that store pairs or mappings of unique keys to values.

'''

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6 }

elements['lithium']= 3

print("\n\n")
print(elements)

print("\n\n")

# We can also use " in" in dictionaries to check if an element is present.

print("Jl" in elements)

print("\n\n")

# Get() methods , looks up dictionary's values in a dictionary, it returns none or default value 
# you had provided if the value  is not found.

print(elements.get("DevOps", "DevOps is Not Found"))

print("\n\n")

# You can check if a dictionary's Key returns "none" with the identity "is" operator
# & manage code from there to preven a crash

jobDesc = elements.get('Site Reliability')
#is_null = jobDesc is None

# "is not" the opposite operator of "is"
is_null = jobDesc is not None
print(is_null)

print("\n\n")


VTXAS = {'MICOS': 133, 'Tesla': 1540, 'Appl': 850, 'Lyft': 345}

VNQ = {'MICOS': [133, -6.51], 'Tesla': [1540, 0.78], 'Appl': [850, 17.01], 'Lyft': [345, 0.79] }
print("VTXAS index fund Stocks & Prices\n", VTXAS)
print("\n")

print("VNQ index fund Stock, Price, & Yield of returns:\n",VNQ)
print("\n\n")

