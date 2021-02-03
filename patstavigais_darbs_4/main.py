import random

words = ["apple", "banana", "cherry"]
guessed_letters = []

hangman = (
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
      +---+
      |   |
      o   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  | 
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
     / \  |
          |
    =========
    """
)


def get_word_with_guessed_letters(guessed_letters, word):
    result = ""
    for character in word:
        if character in guessed_letters:
            result += character
        else:
            result += "-"

    return result


def game():
    fails = 0
    random_word = random.choice(words)

    while fails < 6:
        print(hangman[fails])

        guessed_letters_string = ', '.join(guessed_letters)
        print("Guessed letters: " + guessed_letters_string)

        word_with_dashes = get_word_with_guessed_letters(guessed_letters, random_word)
        print(word_with_dashes)

        if random_word == word_with_dashes:
            print("You won!")
            break

        letter = input("Enter letter: ")
        guessed_letters.append(letter)

        if not letter in random_word:
            fails += 1

    if fails == 6:
        print(hangman[6])
        print("You lost!")


while True:
    print("Enter 1 to play hangman, 2 to add a new word, 3 to quit program")
    action = int(input("Enter number: "))

    if action == 1:
        game()
    elif action == 2:
        word = input("New word: ")
        words.append(word)
        print(f"Added {word}")
    elif action == 3:
        quit()