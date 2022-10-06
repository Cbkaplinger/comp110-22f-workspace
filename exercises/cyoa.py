"""Play some fun Python games."""

__author__ = "730570002"

import random

points: int = 0
player: str = ""
game: bool = True


def main() -> None:
    """Gives a pathway to quit, play Rock Paper Scissors, or play a fun UNC basketball trivia game."""
    greet()

    print("Choose one of these options from above: Option 1 ends the game, option 2 is Rock Paper Scissors, and option 3 is a UNC basketball trivia game. ")
    options = input("Which option do you choose? ")

    if options == "1":
        print(f"Thanks for playing! You ended up with {points} points.")

    if options == "2":
        rock_paper_scissors()

    if options == "3":
        UNC_basketball_game()


def greet() -> None:
    """Greets the player and asks for their name."""
    print("Welcome to a Python version of Rock Paper Scissors or a UNC Basketball trivia game")
    global player
    player = input("What is your name? ")


def rock_paper_scissors() -> None:
    """User and ai play Rock Paper Scissors."""
    global points
    global game
        
    while game:
        user = input(f"\nHello {player}. Choose 'Rock' for rock, 'Paper' for paper, or 'Scissors' for scissors please. ")
        ai = random.choice(['Rock', 'Paper', 'Scissors'])
        print(f"\nYou chose {user}, computer chose {ai}.\n")

        if user == ai:
            print(f"You tied! Both players selected {user}.")
        elif user == "Rock":
            if ai == "Scissors":
                print("You win! Rock beats scissors!")
                points += 1
            else:
                print("You lost. Paper beats rock.")
                points -= 1
        elif user == "Paper":
            if ai == "Rock":
                print("You win! Paper beats rock!")
                points += 1
            else:
                print("You lost. Scissors beats paper!")
                points -= 1
        elif user == "Scissors":
            if ai == "Paper":
                print("You win! Scissors beats paper.")
                points += 1
            else:
                print("You lose. Rock beats scissors.")
                points -= 1
        
        print(f"You have {points} points")
        play_again = input("Play again? Type 'Yes', 'No', 'Other Game': ")
        if play_again == "Other Game":
            UNC_basketball_game()
        if play_again == "No":
            game = False
            print(f"You ended up with {points} points")


def UNC_basketball_game() -> None:
    """A fun UNC basketball trivia game."""
    global points
    global game

    print(f"Hello {player}, welcome to the UNC Basketball trivia game where you can test if you're a real Tar Heel fan")

    while game:
        Q1 = input("\nHow many NCAA championships does UNC Basketball have? ")
        Q1_answer = "6"
        if Q1 == Q1_answer:
            print("Correct")
            points += 1
        else:
            print(f"Incorrect, UNC has {Q1_answer} NCAA championships")
            points -= 1
        print(f"You have {points} points")
        
        Q2 = input("\nWhat conference do the Tar Heels play in? ")
        Q2_answer = "ACC"
        if Q2 == Q2_answer:
            print("Correct")
            points += 1
        else:
            print(f"Incorrect, they play in the {Q2_answer}")
            points -= 1
        print(f"You have {points} points")

        Q3 = input("\nWho is the all time leading scorer of UNC Basketball? ")
        Q3_answer = "Tyler Hansbrough"
        if Q3 == Q3_answer:
            print("Correct")
            points += 1
        else:
            print(f"Incorrect, it's {Q3_answer}")
            points -= 1
        print(f"You have {points} points")

        Q4 = input("\nWho did UNC beat in the 2022 final four? (Hint it's our biggest rival) ")
        Q4_answer = "Duke"
        if Q4 == Q4_answer:
            print("Correct")
            points += 1
        else:
            print(f"Incorrect, it's {Q4_answer}")
            points -= 1
        print(f"You have {points} points")

        Q5 = input("\nWhat is the name of the stadium the Tar Heels play in? ")
        Q5_answer = "Dean Dome"
        if Q5 == Q5_answer:
            print("Correct")
            points += 1
        else:
            print(f"Incorrect, it's the {Q5_answer}")
            points -= 1
        print(f"You have {points} points")
       
        play_again = input("Play again? Type 'Yes', 'No', or 'Other Game': ")
        if play_again == "Other Game":
            rock_paper_scissors()
        if play_again == "No":
            game = False
            print(f"You ended up with {points} points")
 
                
if __name__ == "__main__":
    main()