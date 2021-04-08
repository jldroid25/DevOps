
# A set() method is a Data type for Mutable unordered collections of unique elements.
# it helps with removing duplicate from a list data.

countries = ['Norway', 'UK', 'Denamrk', 'Scotland', 'Northern Ireland', 
'Sweden', 'UK', 'Denmark', 'Canada']

country_set = set(countries)
print(country_set)

print("\n\n")

# set supports the list operator the same List do
print('Norway' in countries)
print('Canada' in country_set)

print("\n\n")

# You can add elements to sets set() where you don't use append method
country_set.add("Netherlands")
print(country_set)

print("\n\n")

# Just like List set has a pop() method that removes a random element from a list.
# Also remember since sets are unordered there is no last element.

# Remove a random elements to sets with pop() method

print(country_set.pop())

print("\n\n")
