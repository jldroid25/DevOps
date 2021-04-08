# ---------How to Reand & Write file in Python ---------------#

'''
# we can use the built-in open() function to read a file
# always use the built-in close() when done to not overuse resources else 
# python will thgrow an error.

# Reading a file.
# create a variable, use open() with file location & 'r' for reading mode
# create sencond variable assign first variable with the read()
# then close() the file
f = open('data4python.txt', 'r')
file_data = f.read()
print(file_data)
f.close()

print('\n')
#------------  Writing to a file ----------//
# create a variable, use open() with file location & 'w' for writing mode
# create sencond variable assign first variable with the write()
# then close() the file
# if the file does not exist yet python will create a new one with name provided.

# FYI: using write() on an existing file with data will erase 
# all current content of that file to add the new data.
# If you don't want to overwritten the file use appen() instead of write()

file_to_write2 = open('data4python.txt','w')
file_to_write2.write("Euphoria girls are Hot!")
file_to_write2.close()


# "With ""
# Python provides a special syntax that auto-closes a 
# file for you once you're finished using it.
with open('data4python.txt', 'r') as f:
    file_data2 = f.read()
print(file_data2)


#If you pass the read method an integer argument, it will read up to that 
# number of characters, output all of them, and keep the 'window' at that 
# position ready to read on
with open('data4python.txt', 'r') as hobby:
    print(hobby.read(2))
    print(hobby.read(6))

    print('\n')
    print(hobby.read())

# ----- Reading Line by Line ----------
#Python will loop over the lines of a file using the syntax "for line in file". 
# I can use this to create a list of lines in the file. Because each line still 
# has its newline character attached, I remove this using .strip().

merbmsg = []
with open('data4python.txt','r') as f:
    for line in f:
        merbmsg.append(line.strip())

print('\n')
print(merbmsg)

'''
print('\n')

# Create a Flying Circus Cast List function  & print data line by line
def create_cast_list(filename):
    # create a list
    cast_list = []
    #use the "with & open()"
    with open('flying_cast_list.txt', 'r') as f:
        # loop to read line by line
        for line in f:
            # separate characters by a comma starting a element 1
            name = line.split(",")[0]
            # add name to list
            cast_list.append(name)
            # return the data. Fyi not displaying
    return cast_list

# Now let's print the data
cast_list = create_cast_list('flying_cast_list.txt')
for actor in cast_list:
    print(actor)

print('\n')