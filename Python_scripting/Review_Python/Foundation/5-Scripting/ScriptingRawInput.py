# -------------Scripting Raw Input ------------------#

#using the input() function

name = input("Enter a name: ")
#print("Welcome come in ", name.title())

# When using the the input() with numbers
# you must include the data type "int()" or "float()" funtion
#  else python will throw an error

print('\n')
num = int(input('enter a number: '))
#print('What\'s number ?', num )

print("Wow expensive {} chages {} per hour".format(name, num))

# ---- We can also use eval() to evaluate a string as a line of  Python
num = 30

x = eval('num + 42')
print(x)

print("\n")

