age = 8
# 2-8 2 dollar ticket

# > 65 5 dollar ticket

# 10 dollars for everyone else


if not ((age >=2 and age <=8) or age >= 65):
    print(" you pay 10 dollars and are not a child or a senior!")
else:
    print("you are a child or a senior")

x = 0
y = -1

(x or y) and (x - 1 == y) and (y + 1 == x)