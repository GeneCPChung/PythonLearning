# APPEND - always adds to the end of a list
data = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 0]
words = ["This", "is", "a", "bunch", "of", "words"]


# data.append("purple")
# print(data)

# EXTEND - allows you to add more than one element to a list (basically another list of elements)
# data.extend([4, 5])
# print(data)

# INSERT - allows you to insert an element wherever you want
# data.insert(2, "hi")
# print(data)

# CLEAR - allows you to clear all elements from a list
# data.clear()
# print(data)

# POP - allows you to remove an item as a specific index
# by default it removes the last item in the list
# you can also assign the removed item to a variable
# data.pop(2)
# print(data)

# REMOVE - removes an item from a list of a specific value
# data.remove(3) # in this case it is searching for the first instance of the number 3 and removing it from the list
# print(data)

# INDEX - returns the index of the specified element in a list
# data.index(5)
# print(data)
#
# # you can also specify a start and end point (or both)
# find_num data.index(5, 5)
# print(find_num)

# find_num = data.index(7, 8, 10)
# print(find_num)

# COUNT - returns the number of times x appears in the list
# will return zero if the element is not found
# count_num = data.count(7)
# print(count_num)

# REVERSE - reverses the elements in a list (in-place)
# data.reverse()
# print(data)

# SORT - sort the items of a list (in-place)
# data.sort()
# print(data)

# JOIN - used to join (concatenate) a list of strings
# join_words = ' '.join(words)
# print(join_words)

# SLICING - make a new list (a copy) from a part (or all) of an existing list
# operates similar to range where you have a start, end and step

# SLICING(START) only using start point will slice from the starting point and
# include the rest of the list
# sl_data = data[2:]
# print(sl_data)

# using a negative number will start the slice
# counting from the end of the list
# sl_data = data[-3:]
# print(sl_data)

# SLICING(END) only using end point, will begin the slice at the start
# of the list and continue to the element before the designated end point (exclusive).
# it is the same as using zero as the start point or leaving the start point empty
# sl_data = data[:6]
# print(sl_data)

# adding a start point will begin the slice at the designated element
# sl_data = data[4:8]
# print(sl_data)

# SLICING(STEP) creates a slice based on the number of skips(steps) between elements
# BEGINNING AND STEP
# sl_data = data[1::2]
# print(sl_data)
#
# # ONLY STEP
# sl_data = data[::3]
# print(sl_data)
#
# # NEGATIVE NUMBERS FOR STEPS
# sl_data = data[3::-2]
# sl_data = data[:10:-4]
# print(sl_data)

# SWAPPING VALUES - allows you string variables together to manipulate list elements
# names = ["James", "Michelle"]
# names[0], names[1] = names[1], names[0]
# print(names)



















