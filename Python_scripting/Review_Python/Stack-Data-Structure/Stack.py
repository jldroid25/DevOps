'''
@------------ Common Stack Operations ------------
Stack is a data structure in which all insertions and
deletions are made in at one end, called the top(not necessarily vertical top)
of the stack.

Stack is L.I.F.O data structure : "Last one in first one out"

Push(item): push item to the top of the stack
Pop(item): remove and return the top item
Peek(item): return the top item without removing it
Is_empty(item):return true if the stack is empty

# ---------Some Common Applications Stack data Struc is used--------
- Reverse Polish notation for evaluating arithmetic expressions
- syntax parsing
- Cold stack (in CPU): space for para,eters & local variables is created
- Used in recursion
- Undo & redo operations in word processors
- Low level assembly programming

'''

#--------How to create  a stack in Python -------------#

class Stack:

    # create a constructor & initialize it with an empty list
    def __init__(self):
        self.items = []

    # check if the stack is empty
    def is_empty(self):
        #return len(self.items) == 0 
        return not self.items # same as above but pythonik

    # add item to the stack with push()
    def push(self, item):
        self.items.append(item)
    
    # Removed item from the stack
    def pop(self):
        return self.items.pop()

    # Return the last item in the list without removing it
    def peek(self):
        return self.items[-1]

    # Find the size of our stack
    def size(self):
        return len(self.items)
   
   # This __str__() enables us to use the print statement 
   # to inspect our stack object
    def __str__(self):
        return str(self.items)

'''
If we wanted to import our stack class to another file.
it would be a problem if we had code here on line 59 & below.

So we are using python Magic methods __main__()
to say that "if this is the main file being run then
only execute the file from line 65 and below ().
If not just use the class & don't worry about code below it
'''
if __name__ == "__main__":

    #We use a capital letter to represent a Stack so that it doesn't
    # get confuse for a obj
    S = Stack()

    print("\n\n")

    print(S)
    print(S.is_empty())
    S.push(3)
    S.push(7)
    S.push(5)
    S.push("Canada")
    print(S)
    print(S.pop())
    print(S)
    print(S.peek())
    print(S.size())

    print("\n\n")