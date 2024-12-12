#Empty Tuple
my_tuple = ()
print(my_tuple)

#Tuple with integers
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

#Mixed data types
my_tuple = ("Mayo", 9, 33.7)
print(my_tuple)

#Nested Tuple
my_tuple = ("Momo", [7, 8, 9], (8, 4, 6))
print(my_tuple)

#Accessing elements
my_tuple = ("M", "a", "y", "o", "m", "i", "k", "u", "n")
print(my_tuple[0])
print(my_tuple[8])

#N-tuple
n_tuple = ("Momo", [7, 8, 9], (8, 4, 6))
print(n_tuple[0][3] )
print(n_tuple[1][2])

#Slicing tuple
print("Sliced: ", my_tuple[1 : 4])

#Iterate tuple
for letters in (my_tuple):
    print("Hello", letters)