"""
TASK 1: Hangman Game
A simple text-based Hangman game where the player guesses a word one letter at a time.
"""

import random

WORDS = ["python", "apple","hangman", "keyboard", "elephant", "sunshine"]

MAX_INCORRECT_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
]


def choose_word():
    """Pick a random word from the predefined list."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """Show the word with unguessed letters replaced by underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed.\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print(HANGMAN_STAGES[incorrect_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Incorrect guesses left: {MAX_INCORRECT_GUESSES - incorrect_guesses}\n")

        guess = input("Guess a letter: ").lower().strip()

        # Basic validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            # Check win condition
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_STAGES[incorrect_guesses])
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    else:
        # Loop ended without breaking -> player lost
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"Game over! You've run out of guesses. The word was: {word}")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
