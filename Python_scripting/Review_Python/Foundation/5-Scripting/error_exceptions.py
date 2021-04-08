#---------- Error & Exceptions  in Python -----------------

'''
# enter the word "ten" to see a ValueError msg
x = int(input('Enter a number: '))
x += 20
print(x)


# This will throw a NameError
#print(nonexistant_variable)

# Try-Block Exception to handle errors

try:
    x = int(input('Enter a number: '))
    
except:
    print('That\'s not a valid number')

   

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number')

    print('\nAttempted Input')


# If you want code to keep running use a while-loop & 
# break when correct input is entered 

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number')

    print('\nAttempted Input')



# The "finally clause  is used to run a code we want to run before try-block
# exit the code 

while True:
    try:
        x = int(input('Enter a number: '))
        break
    # Throw exception  only when wrong input was entered
    except ValueError:
        print('That\'s not a valid number')
    # ctrl + c to leave terminal
    except KeyboardInterrupt:
        print('\no input taken')
        break

    finally:
        print('\nAttempted Input')


# Accessing Error Messages
# When you handle an exception, you can still access its error message like this:

try:
    # add some code here
except ZeroDivisionError as e:
    # add more code here
    print("ZeroDivisionError occurred: {}".format(e))

# this will print "ZeroDivisionError occurred: integer division or modulo by zero"



# So you can still access error messages, even if you handle them to keep your 
# program from crashing! If you don't have a specific error you're handling, 
# you can still access the message like this:
try:
    # some code here
    int(input("enter a number: "))

except Exception as e:
    
    # some code here
    print("Exception occured: {}".format(e)) 
#Exception is just the base class for all built-in exceptions. 
# You can learn more about Python's documentation.
'''