# Compound DataStructure is a combination of dictionary inside another
# to have elements names to another dictionary that stores that collection data.
# Essentially it's a nested dictionary

print("\n\n")

elements = {
    'hydrogen': {'number': 1, 'weight': 1.000794, 'Symbol' : 'H'} , 
     'helium': {'number': 2, 'weight': 3.1007, 'Symbol' : 'He'} , 
     'carbon': {'number': 6, 'weight': 4.200, 'Symbol' : 'Ca'}}

print(elements)
print("\n\n")

print("Hydrogen:", elements['hydrogen'])
print("helium:", elements['helium'])
print("number:", elements['carbon'])

print("\n")

VTSAX = {
    'Apple': {'Sticker':'APPL', 'Price': 1056, 'Yield': 0.679} , 
     'Tesla': {'Sticker': 'TesT', 'Price': 3006, 'Yield': 790.89} , 
     'Lyft': {'Sticker': 'LYT', 'Price': 56, 'Yield': 0.0023}
     }
print("Apple Stock info :", VTSAX['Apple'])
print("Tesla Stock Info:", VTSAX['Tesla'])
print("Lyft Stock Info :", VTSAX['Lyft'])

print("\n\n")

# We can also use get() method to find elements by their key

print(elements.get('calcium', 'There\'s no such element'))
print("\n")
print(VTSAX.get('Microsoft', 'There\'s no such stock info'))

print("\n\n")

# we can also look up by more keys with [] 
print("Hydrogen:", elements['hydrogen']['weight'])

print("Lyft:", VTSAX['Lyft'][''])