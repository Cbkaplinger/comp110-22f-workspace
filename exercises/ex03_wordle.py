"""Structured Wordle."""

__author__ = "730570002"


def contains_char(secret_word: str, char: str) -> bool:
    """Indexing through to see if the character is in the word."""
    assert len(char) == 1
    index: int = 0
    letter_found: bool = False
    while index < len(secret_word):
        if char == secret_word[index]:
            letter_found = True   
        index += 1
    
    if letter_found is True:
        return True
    else:
        return False


def emojified(guess: str, secret_word: str) -> str:
    """Outputs a string of emojis."""
    assert len(guess) == len(secret_word)
    index: int = 0

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    sw_index: int = 0  # the index of the secret_word
    progress: str = ""

    while index < len(secret_word):
        if guess[index] == secret_word[index]:     
            progress += GREEN_BOX
        else:
            inside_word: bool = contains_char(secret_word, guess[index])

            # iterates through checking if a letter of the guess matches any of the other letters in the secret word
            while sw_index <= (len(secret_word) - 1):
                if guess[index] == secret_word[sw_index]:
                    progress += YELLOW_BOX
                    inside_word = True
                sw_index += 1
            if inside_word is False:
                progress += WHITE_BOX
        # resets the inside_word and sw_index back to their original values and shifts the index by 1 to the next character in the guess
        inside_word = False
        sw_index = 0  
        index += 1
    return progress


def input_guess(length: int) -> str:
    """Checks if the guess is the same length as the secret word."""
    guess: str = input(f"Enter a {length} character word: ")

    while (len(guess) != length):
        guess = input(f"That wasn't {length} chars! Try again: ")
    else:
        return guess


def main() -> None:
    """Wordle gameplay."""
    secret_word: str = "codes"
    turn: int = 1
    user_win: bool = False

    while turn < 7:
        if user_win is False:
            print(f"=== Turn {turn}/6 ===")
            final_guesses: str = input_guess(len(secret_word))
            emojified(final_guesses, secret_word)
            if (final_guesses == secret_word):
                print(f"You won in {turn}/6 turns!")
                user_win = True
        turn += 1

    if (user_win is not True):
        print("X/6 - Sorry try again tomorrow!")


if __name__ == "__main__":

    main()