# Basic Rock Paper Scissors game. Rules:
# Rock beats Scissors
# Paper beats Rock
# Scissors beat Paper

#Note to self, you should have started with the tie to reduce the amount of if else statements.

def one_more_game() -> bool:
    while True:
        again = input("would you like to play again?(y/n): ")
        if again.lower() == "y":
            return True
        else:
            return False

def p_input() -> str:
    while True:
        player_input = input("player1 type R, P or S ([R]ock, [P]aper or [S]cissors): ")
        if player_input in ["R", "P", "S"]:
            return player_input   


def start_game():
    play_again = True
    while play_again == True:
        player1 = p_input()
        player2 = p_input()
        if player1 == "R":
            if player2 == "P":
                print("player2 wins. Paper beats Rock")
                play_again = one_more_game()
            elif player2 == "S":
                print("player1 wins, Rock beats Scissors")
                play_again = one_more_game()
            else:
                print("it's a tie")
                play_again = one_more_game()
        elif player1 == "P":
            if player2 == "R":
                print("player1 wins, Paper beats Rock")
                play_again = one_more_game()
            elif player2 == "S":
                print("player2 wins, Scissors beat Paper")
                play_again = one_more_game
            else:
                print("it's a tie")
                play_again = one_more_game()
        else:
            if player2 == "R":
                print("player2 wins, Rock bets Scissors")
                play_again = one_more_game
            elif player2 == "P":
                print("player1 wins, Scissors beat Paper")
                play_again = one_more_game
            else:
                print("it's a tie")
                play_again = one_more_game()

start_game()