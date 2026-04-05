import random

# Predefined word list
WORDS = ["python", "hangman", "programming", "computer", "keyboard"]

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def get_display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("\n" + "="*40)
    print("   Welcome to HANGMAN!")
    print("="*40)

    while wrong_guesses < max_wrong:
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"Word: {get_display_word(word, guessed_letters)}")
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print()

        # Check if player has won
        if all(letter in guessed_letters for letter in word):
            print(f"🎉 Congratulations! You guessed the word: '{word.upper()}'")
            break

        # Get player input
        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try another letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.\n")

    else:
        print(HANGMAN_STAGES[max_wrong])
        print(f"💀 Game Over! The word was: '{word.upper()}'")

    play_again = input("\nPlay again? (yes/no): ").lower().strip()
    if play_again in ("yes", "y"):
        play_hangman()
    else:
        print("\nThanks for playing Hangman! Goodbye! 👋")

if __name__ == "__main__":
    play_hangman()
