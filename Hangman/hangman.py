#%%
#Hangman python script

import random

possible_words = ["water", "amalgamation", "democracy", "president", "logistic", "headache", "computation"]

bad_guesses = []
good_guesses = []
bad_attempts = 0
max_guesses = 10


def new_game_word():
    to_guess = random.choice(possible_words)
    print("The word has been chosen. Now you must guess it")
    return to_guess

new_game_word = new_game_word()
display_word = "_" * len(new_game_word)

print(display_word)

def user_guess(good_guesses, bad_guesses,new_game_word,bad_attempts):
    print("A guess must be made soon.")
    valid_input = False
    while valid_input == False:
        already_guessed = list(set(good_guesses + bad_guesses))
        user_input = input("Guess a letter: ")
        if len(user_input) > 1 or len(user_input) == 0 or user_input in already_guessed or user_input.isnumeric():
            print("You must guess one letter only, no previous letters are allowed")
            print(f"Your previous guesses were: {already_guessed}")
            valid_input = False
        else:
            if user_input in new_game_word:
                print(f"Your guess {user_input} was correct!")
                good_guesses.append(user_input)
                valid_input = True
            else:
                print(f"Your guess {user_input} was wrong!")
                bad_guesses.append(user_input)
                bad_attempts += 1
                valid_input = True

def display_word(new_game_word, display_word, good_guesses):
    for letter_position in range(len(new_game_word)):
        if new_game_word[letter_position] in good_guesses:
            display_word[letter_position] = new_game_word[letter_position]
    print(f"Your guesses show {display_word} so far!")
    return display_word

def game_over(new_game_word, display_word):
    if new_game_word == display_word:
        print(f"Congratulations, you guessed {new_game_word} and get to see another day!")
        game_over = True
        return game_over
    elif bad_attempts == max_guesses + 1:
        print(f"You have used all your guesses. Game over. NOW YOU HANG!")
        game_over = True
        return game_over
    else:
        guesses_remaining = max_guesses - bad_attempts
        print(f"You have {guesses_remaining} guesses left! Use them wisely!")
        game_over = False
        return game_over

def game_on():
    print("the game has begun! Choose your letter wisely and you will live")
    while game_over() is False:
        print("Round begins")
        display_word1 = display_word()
        print(f"Guess the word {display_word1} or be hanged!")
        user_guess()
        print("Round over")
        game_over()
        

game_on()


# %%
