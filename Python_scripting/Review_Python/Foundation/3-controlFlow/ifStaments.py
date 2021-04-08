
'''
print("\n\n")

#If-statements run or skip a code base on weather a condition is true or false
bank_balance = 20
phone_balance = 4

print(phone_balance, bank_balance)
#here we have if-statement, condition, follow by colon. 
# This is is a boolean expression that evaluate to either true or false
if phone_balance < 5:
  #block of code to execute if condition is true
  phone_balance += 10
    # or execute this one if false
  bank_balance -= 10
print(phone_balance, bank_balance)

'''
print("\n\n")
'''
# Using else-statement to run a different line of code if condition is false.
n = 17

if n % 2 == 0:
  print("Number " + str(n) + " is even. ")
else:
  print("Number " + str(n) + " is odd. ")

'''

'''
Alternatively we can use elif to run other block of code when
first condition is evaluate to false .

'''

# Recall Python doesn't use {} in block of codes instead it used indentation.
# So always make sure codes are properly indented.
# indentation conventionally comes in multiples of four spaces.
# so be strict about this convention
season = "winter"

if season == "Spring":
      print("plant the garden !")
elif season == "summer":
      print("water the garden !")
elif season == "winter":
      print("stay indoor !")
else:
      print("Unpredictable season")

print("\n\n")

# Complex Boolean expression by mixing multiples operators & logical operators.
unsubscribed = "no"
location = "CAN"

if(not unsubscribed) and (location == "USA" or location == "CAN"):
  print("send email")

  # -----Bad Conditional statement you should never run. ------------

  # " while True" this will always be true
  # " if False " this will always be false , condition will never accur

  # You can use the "not" operator if you wanna check a boolean is false.

