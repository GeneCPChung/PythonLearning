# languages = ["python", "java", "SQL", "JS"]
# print(language[0])
# print(language[1])
# print(language[2])

# for language in languages:
#     print(language)

numbers = [5, 30, 9, 5.5, 18]
# FOR LOOP
# for num in numbers:
#     print(num * num)

#WHILE LOOP
# i = 0
#
# while i < len(numbers):
#     print(numbers[i] * numbers[i])
#     i += 1

# LIST EXERCISE
# Write code that loops over the list and adds all the strings together to form one large combined
# string(don't add any spaces between them)
# The combined string should be in all UPPERCASE as well
# Save the result in a variable called 'result'
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ''
for s in sounds:
    result += s.upper()
print(result)