#%%
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.

from random import randint

def u_input() -> int:
    while True:
        number = input("please input a natural number between 1-9 or exit to quit: ")
        if number == "exit":
            print("quitting game...")
            return number
        elif int(number) in range(1,10):
            return int(number)
        else:
            print("the number has to be an integer between 1-9")

def randomizer():
    a = randint(1,9)
    return a

def game_on():
    to_guess = randomizer()
    while True:
        guess = u_input()
        if guess == "exit":
            break
        elif guess == to_guess:
            print(f"Congratulations you guessed {to_guess} correctly")
            break
        elif guess < to_guess:
            print(f"You guessed {guess}, but this is lower than the number you need to guess")
        else:
            print(f"You guessed {guess}, but this number is higher than the number you need to guess")

game_on()

# %%
