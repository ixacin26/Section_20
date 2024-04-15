import random


while True:
    my_answer = input("What do you choose - rock, paper or scissors? ")
    my_answer = my_answer.lower()
    print("My answer is", my_answer)
    
    if my_answer != "rock" and my_answer != "paper" and my_answer != "scissors":
        print("No valid answer - try again!")
        continue
    else:
        your_answer= random.choice(["rock","paper","scissors"])
        print("Your answer is", your_answer)
        if my_answer == your_answer:
            print("No winner - repeat!")
            continue
        else:
            if (my_answer == "rock" and your_answer == "paper") or (my_answer == "paper" and your_answer == "scissors") or (my_answer == "scissors" and your_answer == "rock"):
                print("The computer has won!")
                continue
            else:
                print("You have won!")
                break
