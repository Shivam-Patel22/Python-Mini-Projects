import random
choice=["Rock","Paper","Scissors"]
computer_select=random.choice(choice)
user=input("Select Rock,Paper and Scissors=")
if user in choice:
    print("User Selected=",user)
    print("Computer Selected=",computer_select)
    if computer_select==user:
        print("It Was A Tie,Try Again")
    elif user=="Rock" and computer_select=="Paper" or user=="Paper" and computer_select=="Rock" or user=="Scissors" and computer_select=="Paper":
        print("User Wins")
    else:
        print("Computer Wins")
else:
    print("Invalid Choice")
