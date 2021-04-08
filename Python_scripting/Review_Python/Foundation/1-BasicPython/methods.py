'''

A method in Python behaves similarly to a function. 
Methods actually are functions that are called using dot notation. 
For example, lower() is a string method that can be used like this, 
on a string called "sample string": sample_string.lower().

other examples:

sample_string.lower()
sample_string.count('a')
sample_string.find('a')


'''

'''
One important string method: format()
We will be using the format() string method a good bit 
in our future work in Python, and you will find it very 
valuable in your coding, especially with your print statements.

We can best illustrate how to use format() 
by looking at some examples:


Notice how in each example, the number of pairs of curly braces 
{} you use inside the string is the same as the number of 
replacements you want to make using the values inside format()

'''
print("Mohammed has {} balloons".format(27))

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))


'''
Another important string method: split()

This function or method returns a data container called a list 
that contains the words from the input string. 


The split method has two additional arguments (sep and maxsplit).

 The sep argument stands for "separator". 

It can be used to identify how the string should be split up 
(e.g., whitespace characters like space, tab, return, newline;
specific punctuation (e.g., comma, dashes)). 
If the sep argument is not provided, 
the default separator is whitespace.

the maxsplit argument provides the maximum number of splits.



'''
new_str = "The cow jumped over the moon."
new_str.split()
print(new_str.split() , "\n")
#['The', 'cow', 'jumped', 'over', 'the', 'moon.']


print(new_str.split(' ', 3) , "\n")
#['The', 'cow', 'jumped', 'over the moon.']

new_str.split('.')
#['The cow jumped over the moon', '']

new_str.split(None, 3)
#['The', 'cow', 'jumped', 'over the moon.']

