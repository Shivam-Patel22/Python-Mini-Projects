import random
def Guessing():
    number=random.randint(0,100)
    attempts=0
    while True:
        guess=int(input("Guess A Number Between 1-100="))
        attempts+=1
        if guess<number:
            print("Low")
        elif guess>number:
            print("High")
        else:
            print("Your Guess is Right,You done in",attempts,"Attempts")
            break
Guessing()