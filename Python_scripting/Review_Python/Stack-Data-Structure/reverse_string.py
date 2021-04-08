
#-----Use a stack to decode the the hidden message ------
import Stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
S = Stack.Stack()

# Your solution Here
for char in string:
    S.push(char)

while not S.is_empty():
    reversed_string += S.pop()

print("\n\n")
print(reversed_string)

print("\n\n")