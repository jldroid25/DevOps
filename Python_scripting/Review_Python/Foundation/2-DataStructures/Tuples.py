
# Tuple Data Structure 
'''
pronounce toople(z)
A tuple is another useful container. It's a data type for immutable ordered sequences of 
elements. They are often used to store related pieces of information. 
Consider this example involving latitude and longitude:

'''
print("\n\n")

location = (13.4125, 163.86667)
print("Latitude:", location[0])
print("Longitude:", location[1])

print("\n\n")

AngkoWat = (13.4125, 103.866667)
print(type(AngkoWat))

print("AngKor Wat is at latitude: {} ".format(AngkoWat[0]))
print("AngKor Wat is at longitude: {} ".format(AngkoWat[1]))

print("\n\n")

#This is a Tutle, Developers often removes --> () if they don't clariry code
dimensions = 52, 40, 100

length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

#f we won't need to use dimensions directly, we could shorten those two lines of 
# code into a single line that assigns three variables in one go!

length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))