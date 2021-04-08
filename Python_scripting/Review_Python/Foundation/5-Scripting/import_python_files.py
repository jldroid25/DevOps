#import useful_functions

import useful_functions as uf

'''

It's the standard convention for import statements to be written at the top of 
a Python script, each one on a separate line. This import statement creates 
a module object called useful_functions. Modules are just Python files that 
contain definitions and statements. To access objects from an imported module, 
you need to use dot notation.


# Now that we have imported our module useful_functions
# Let's  make use of it 

scores = [88, 92, 79, 93, 85]

# accessing mean() from our inported module
mean = useful_functions.mean(scores)

# accessing mean() from our inported module
curved = useful_functions.add_five(scores)

mean_c = useful_functions.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, "New Mean:", mean_c)


- We can add an alias to an imported module to reference it with a different name.
import useful_functions as what-ever-name i e"uf"
# Notice You no longer has to use the imported module's name . Just use "uf." function
uf.add_five([1, 2, 3, 4])


- Using a main block
To avoid running executable statements in a script when it's imported as 
a module in another script, include these lines in an 
if __name__ == "__main__" block. Or alternatively, include them in a function
 called main() and call this in the if main block.

Whenever we run a script like this, Python actually sets a special built-in variable 
called __name__ for any module. When we run a script, 
Python recognizes this module as the main program, 

 and sets the __name__ variable for this module to the string "__main__". 
 For any modules that are imported in this script, 
 this built-in __name__ variable is just set to the name of that module.

Therefore, the condition if __name__ == "__main__"is just checking whether 
this module is the main program.


--------Techniques for Importing Modules
There are other variants of import statements that are useful in different situations.

- To import an individual function or class from a module:
from module_name import object_name

- To import multiple individual objects from a module:
from module_name import first_object, second_object

- To rename a module:
import module_name as new_name

- To import an object from a module and rename it:
from module_name import object_name as new_name

- To import every object individually from a module (DO NOT DO THIS):
This is a bad practice that can lead no confusion with module names.

from module_name import * # this is a no no

If you really want to use all of the objects from a module, 
use the standard import module_name statement instead and access 
each of the objects with the dot notation.

import module_name

---Modules, Packages, and Names
In order to manage the code better, modules in the Python Standard Library 
are split down into sub-modules that are contained within a package. 
A package is simply a module that contains sub-modules. 
A sub-module is specified with the usual dot notation.

Modules that are submodules are specified by the package name 
and then the submodule name separated by a dot. 
You can import the submodule like this.

import package_name.submodule_name
import os.path # os is the module, path is the sub-module
'''
scores = [88, 92, 79, 93, 85]

# accessing mean() from our inported module
mean =uf.mean(scores)

# accessing mean() from our inported module
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, "New Mean:", mean_c)

print(__name__)
print(uf.__name__)