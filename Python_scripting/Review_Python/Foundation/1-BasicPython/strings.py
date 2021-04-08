'''
--------Working with Strings in Python 

'''

# double quote 
mydouble_quote_var = "This a for a double quote string"

# single Quote
mysingle_quote_var = 'This a for a single quote string'

# displying double quotes
singlequote_wraps_doublequotes = 'Hello Jldroid you are "Fantastic" '

# displying single quotes with delimeter \
singlequote_with_delimeter = "Hello man you\'re really the man !"

print(mydouble_quote_var + "\n")
print( mysingle_quote_var + "\n")
print( singlequote_wraps_doublequotes + "\n")

print(singlequote_with_delimeter + "\n")

print(  mysingle_quote_var + " : " +singlequote_wraps_doublequotes)

print(" REPEAT ME 5 TIMES \n" * 5 )

# ========================================

# Python built-in length function tells us the length of a string.

print(len(singlequote_wraps_doublequotes))

# or use len() to store return value in a variable

udacity_length = len("udacity")
print(udacity_length)