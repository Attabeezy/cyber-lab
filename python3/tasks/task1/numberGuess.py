import random

guess = input("I'm thinking of a number between 1 and 10: ")
answer = random.randint(1,10)

while True:
    if answer == guess:
        print("Yes!!!. Your prediction is right ", answer)
        state = input("Do you want to try again? [y/n]: ")
        if state == "y":
           continue
        elif state == "n":
           break
    if answer != guess:
        print("Try again!!!")
        break
