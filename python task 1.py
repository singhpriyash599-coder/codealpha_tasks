import random

def hangman():
    words = ["python", "hangman", "random", "string", "loop"]
    word = random.choice(words)  # Randomly select a word
    guessed_letters = []
    attempts = 6
    display_word = ["_"] * len(word)

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have", attempts, "incorrect guesses allowed.")
    print(" ".join(display_word))
    while attempts > 0 and "_" in display_word:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts)

        print(" ".join(display_word))

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game over! The word was:", word)

hangman()