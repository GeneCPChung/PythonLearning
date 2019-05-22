import random

random_number = random.randint(1, 10)

guess = None
while guess != random_number:
    guess = input("Pick a number from 1 to 10 \n")
    guess = int(guess)
    if guess < random_number:
        print("TOO LOW!\n")
    elif guess > random_number:
        print("TOO HIGH!\n")
    else:
        print("YOU GOT IT!!")
        break
print(random_number)
