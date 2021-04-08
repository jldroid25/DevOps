
# Useful Functions for Lists

# len() methods  returns how many elements are in a list

# max() methods returns the greatest elements in a list
# FYi:  with integers is the greatest 
#  but with string it returns element occurs last if list sorted alphabetically.
python_varieties = ['Burmese Python', 'Africa Python', 'Ball Python', 
'Reticulated Python', 'Angolan Python ']

print(max(python_varieties))

# min() methods returns the smalles elements in a list

# sorted() methods returns a copy of the list in order from smallest to largest.
# leaving the original list unchange
# We can use reverse=True to sort from highest to smallest

print("\n\n")

highest_salary = [60000, 20000, 100, 2, 1000000, 78900, 456]
print(sorted(highest_salary))

print("Using reverse=true to sort from highest to smalles\n")
print(sorted(highest_salary, reverse=True))

# Useful Functions for Lists II

# join() method  is a string method that takes a list of strings as an argument,
#  and returns a string consisting of the list elements joined by a separator string.
# Failure to add a seperator will cause unexpected result
          #Separator "\t".join()
new_str = "\t" .join(['Kiera', 'Jade', 'Rubic', 'Shania'])
print(new_str)


# Append() method A helpful method called append adds an element to the end of a list.

letters = ['a', 'b', 'c']
letters.append('d')
print("\n\n", letters, "\n")