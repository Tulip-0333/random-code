# Hangman in Python
import random

def hangman():
    word_list = ["python", "javascript", "java", "csharp", "swift"]
    random_word = random.choice(word_list)
    word = list(random_word)
    letters_guessed = []
    word_guessed = []
    for i in word:
        word_guessed.append("_")
    tries = 6
    print("Welcome to Hangman! Guess a programming language.")
    print(word_guessed)

    while tries > 0:
        user_guess = input("Guess a letter: ").lower()
        if user_guess in letters_guessed:
            print("You already guessed that letter. Try again.")
        elif user_guess in word:
            letters_guessed.append(user_guess)
            for i in range(0, len(word)):
                if user_guess == word[i]:
                    word_guessed[i] = user_guess
            if "_" not in word_guessed:
                print("Congratulations! You guessed the word: " + "".join(word_guessed))
                break
        else:
            letters_guessed.append(user_guess)
            tries -= 1
            print("Incorrect. You have " + str(tries) + " tries left.")
        print(word_guessed)

    if "_" in word_guessed:
        print("Sorry, you ran out of tries. The word was " + "".join(word) + ".")

if __name__ == '__main__':
    hangman()
