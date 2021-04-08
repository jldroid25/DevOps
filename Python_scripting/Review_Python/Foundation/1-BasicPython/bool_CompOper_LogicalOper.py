'''
---Booleans, Comparison Operators, and Logical Operators ---

The bool data type:
 holds one of the values True or False, 
which are often encoded as 1 or 0, respectively.

Comparison Operators:
< means : Less
> means : greater
<= means : Less Than
>= means : Greather Than
== means : Equal (notice not the same as = )
!= means : Not equal 

Logical Operators: and , or , (flip boolean)

Evaluates if all provided statements are True
and  
--> 5 < 3 and 5 == 5  (False)

Evaluates if at least one of many statements is True
or  
--> 
5 < 3 or 5 == 5   (True)

- Flips the Bool Value
not
 5 < 3	(True) 
 no this change/flip to 3 < 5 therefore True	
''' 

x = 6

y = 12

if(x > y):
    print(True)
else:
    print(False)
