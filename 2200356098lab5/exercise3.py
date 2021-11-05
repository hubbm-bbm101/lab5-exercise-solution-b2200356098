from random import randint
number = randint(0,100)
guess = None
while guess!= number:
    guess =int(input("type your guess:\n"))
    if guess == number:
        break
    elif guess > number:
        print("decrease your number\n")
    else:
        print("increase your number\n")
print("You won!")



