# MASTERMIND GAME
#PYTHON INTERNSHIP
#CIPHER BYTE TECHNOLOGIES
'''Two players play the game against each other
let’s assume Player 1 and Player 2.
Player 1 plays first by setting a multi-digit number.
Player 2 now tries his first attempt at guessing the number.
If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not , then Player 1 hints by revealing which digits or numbers Player 2 got correct.
The game continues till Player 2 eventually is able to guess the number entirely.
Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
If not , then Player 2 wins the game.
I have to do the python code for this to execute as same as it mentioned'''

#SOURCE CODE
import random
def check_guess(secret, guess):
    correct_digits = sum(
        [1 for i in range(len(secret)) if secret[i] == guess[i]])
    return correct_digits

def main():
    print("Welcome to the Mastermind game!")

    # Player 1 sets a multi-digit number
    player1_number = input("Hey Player 1:- please enter a multi-digit number:- ")

    # Player 2 guesses Player 1's number
    player2_attempts = 0
    while True:
        player2_guess = input("Hey Player 2 , Now make your guess:- ")
        player2_attempts += 1

        if player2_guess == player1_number:
            print(
                f"Player 2 is crowned Mastermind in {player2_attempts} attempts!")
            break
        else:
            correct_digits = check_guess(player1_number, player2_guess)
            print(f"Hint: {correct_digits} digits are correct.")

    # Player 2 sets a multi-digit number
    player2_number = input("Player 2, please enter a multi-digit number: ")

    # Player 1 guesses Player 2's number
    player1_attempts = 0
    while True:
        player1_guess = input("Player 1, make your guess: ")
        player1_attempts += 1

        if player1_guess == player2_number:
            print(
                f"Player 1 is crowned Mastermind in {player1_attempts} attempts!")
            break
        else:
            correct_digits = check_guess(player2_number, player1_guess)
            print(f"Hint: {correct_digits} digits are correct.")

    # Determine the winner
    if player1_attempts < player2_attempts:
        print("Player 1 wins the game and is crowned Mastermind!")
    elif player1_attempts > player2_attempts:
        print("Player 2 wins the game and is crowned Mastermind!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()

#output
''' Welcome to the Mastermind game!
Hey Player 1:- please enter a multi-digit number:- 46
Hey Player 2 , Now make your guess:- 32
Hint: 0 digits are correct.
Hey Player 2 , Now make your guess:- 33
Hint: 0 digits are correct.
Hey Player 2 , Now make your guess:- 36
Hint: 1 digits are correct.
Hey Player 2 , Now make your guess:- 35
Hint: 0 digits are correct.
Hey Player 2 , Now make your guess:- 46
Player 2 is crowned Mastermind in 5 attempts!
Player 2, please enter a multi-digit number: 58
Player 1, make your guess: 58
Player 1 is crowned Mastermind in 1 attempts!
Player 1 wins the game and is crowned Mastermind!'''
