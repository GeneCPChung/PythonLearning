# Conditional logic allows you to do operations on elements in a list
name = 'gene'
print([char.upper() for char in name])

friends = ["mitch", "rain", "mike", "jon"]
print([friend[0].upper() + friend[1:] for friend in friends])

print([num * 10 for num in range(1, 6)])

print([bool(val) for val in [0, [], '']])

numbers = [1, 2, 3, 4, 5]
print([str(num) for num in numbers])

# LIST COMPREHENSION WITH CONDITIONAL LOGIC
# allows you to do conditional logic on a list with List Comprehension
evens = [num for num in numbers if num % 2 == 0]
print(evens)

odds = [num for num in numbers if num % 2 != 0]
print(odds)

print([num*2 if num % 2 == 0 else num/2 for num in numbers])

lcwithcl = "This how you do it?"
print(''.join(char for char in lcwithcl if char not in "aeiou"))
