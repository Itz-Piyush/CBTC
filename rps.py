#CIPHER BYTE TECHNOLOGY
#INTERNSHIP

'''ROCK PAPER SCISSOR GAME
Winning Rules as follows:

Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.'''

#SOURCE CODE
import random
# Creating winner function by passing two parameters
def winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == "rock":
        if computer_choice == "paper":
            return "Computer wins!"
        else:
            return "Player wins!"
    elif player_choice == "paper":
        if computer_choice == "scissor":
            return "Computer wins!"
        else:
            return "Player wins!"
    elif player_choice == "scissor":
        if computer_choice == "rock":
            return "Computer wins!"
        else:
            return "Player wins!"
    else:
        return "Invalid input. Please choose rock, paper, or scissor."


choices = ["rock", "paper", "scissor"]

while True:
    computer_choice = random.choice(choices)

    player_choice = input(
        "Enter your choice (rock/paper/scissor), or type 'exit' to quit: ").lower()

    if player_choice == "exit":
        print("Thank you for playing!")
        break

    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissor.")
        continue

    print(f"Computer's choice: {computer_choice}")
    print(winner(player_choice, computer_choice))

#output format
'''Enter your choice (rock/paper/scissor), or type 'exit' to quit: rock
Computer's choice: scissor
Player wins!
Enter your choice (rock/paper/scissor), or type 'exit' to quit: paper
Computer's choice: rock
Player wins!
Enter your choice (rock/paper/scissor), or type 'exit' to quit: scissor
Computer's choice: rock
Computer wins!
Enter your choice (rock/paper/scissor), or type 'exit' to quit: exit
Thank you for playing!'''
