
from dataclasses import dataclass, field

'''
# --- Create Immutable Data Classes ----

Immutable Data Class for when you don't your classes to change.

'''

@dataclass(frozen=True) # The "Frozen" parameter makes the class immutable

class ImmutableClass:
    value1 : str = "Value1"
    value2 : int = 0

    #This will give an error due to Frozen=True above
    def somefunc(self, newval):
        self.value2 = newval


obj = ImmutableClass()

print("\n\n")

print(obj.value1)



#Attempting to change the value of an immutable class throws an execuable error
# This will give a "FrozenInstanceError"
#obj.value1 = "Another Value"
#print(obj.value1)


# even functions within the class can't change anything
obj.somefunc(20)

print("\n\n")

