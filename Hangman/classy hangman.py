#%%
#Hangman python class

from hangman import bad_guesses, good_guesses, new_game_word, possible_words
import random

class Hangman():
    def __init__(self) -> None:
        self.possible_words = ["water", "amalgamation", "democracy", "president", "logistic", "headache", "computation"]
        self.guess = new_game_word()
        self.word_display
        self.bad_guesses = []
        self.good_guesses = []
        self.wrong_attempts = 0
        self.lives = 10

    def new_game_word(self):
        to_guess = random.choice(self.possible_words)
        print("The word has been chosen. Now you must guess it")
        return to_guess
    
    def user_guess(self):
        print("A guess must be made soon!")
        valid_input = False
        while valid_input == False:
            already_guessed = list(set(good_guesses + bad_guesses))
            user_input = input("Guess a letter: ")
            if len(user_input) > 1 or len(user_input) == 0 or user_input in already_guessed or user_input.isnumeric():
                print("You must guess one letter only, no previous letters are allowed")
                print(f"Your previous guesses were: {already_guessed}")
                valid_input = False
            else:
                if user_input in self.guess:
                    print(f"Your guess {user_input} was correct!")
                    good_guesses.append(user_input)
                    valid_input = True
                else:
                    print(f"Your guess {user_input} was wrong!")
                    bad_guesses.append(user_input)
                    self.wrong_attempts += 1
                    valid_input = True
    
    def display_word(self):
        for letter_position in range(len(new_game_word)):
            if new_game_word[letter_position] in good_guesses:
                temp_list = list(self.word_display)
                temp_list[letter_position] = new_game_word[letter_position]
                self.word_display = str(temp_list)
        print(f"Your guesses show {self.word_display} so far!")
        return self.display_word

    def game_over(self):
        if self.guess == self.word_display:
            print(f"Congratulations, you guessed {new_game_word} and get to see another day!")
            game_over = True
            return game_over
        elif self.wrong_attempts == self.lives + 1:
            print(f"You have used all your guesses. Game over. NOW YOU HANG!")
            game_over = True
            return game_over
        else:
            guesses_remaining = self.lives - self.wrong_attempts
            print(f"You have {guesses_remaining} guesses left! Use them wisely!")
            game_over = False
            return game_over