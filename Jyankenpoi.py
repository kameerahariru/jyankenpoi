#Computer1 Versus Computer2

import random

class jyankenpoi:
    def __init__(self):
        self.candidate_1 = "computer_1"
        self.candidate_2 = "computer_2"

        self.possibility_1 = """

            __________
          /         __|
----------          __|
----------          __|
          \         __|
           ___________/

"""
        self.possibility_2 = """

            _____________
          /         _____|____
----------          __________|
----------          ___________|
          \         _________|
            ________________|

"""
        self.possibility_3 = """

            _______
          /        \____________
----------       \  \___________|
----------        \  \__________|
          \   |____\_/___|
           \__|________|

"""
        self.possibilities = [self.possibility_1, self.possibility_2, self.possibility_3]
        self.result_1 = "It's a tie!"
        self.result_2 = "Computer_1 wins!"
        self.result_3 = "Computer_2 wins!"

    def get_prediction(self):
        while True:
            print("Welcome to the Prediction Game!")
            prediction_game = input(f"Who do you think is going to win the battle? {self.candidate_1} or {self.candidate_2}? ").strip().lower()

            if prediction_game in [self.candidate_1, self.candidate_2]:
                return prediction_game
            else:
                print("INVALID CHOICE! Please choose between {} or {}.".format(self.candidate_1, self.candidate_2))

    def get_computer_choices(self):
        computer_1 = random.choice(self.possibilities).lower()
        computer_2 = random.choice(self.possibilities).lower()
        return computer_1, computer_2

    def determine_winner(self, computer_1, computer_2):
        if computer_1 == computer_2:
            result = self.result_1
        elif computer_1 == self.possibility_1 and computer_2 == self.possibility_3:
            result = self.result_2
        elif computer_1 == self.possibility_2 and computer_2 == self.possibility_1:
            result = self.result_2
        elif computer_1 == self.possibility_3 and computer_2 == self.possibility_2:
            result = self.result_2
        else:
            result = self.result_3
        return result

    def play_game(self):
        prediction_game = self.get_prediction()

        print("Let's play Rock, Paper, Scissors!")
        print("Rock beats Scissors")
        print("Paper beats Rock")
        print("Scissors beats Paper")

        while True:
            computer_1, computer_2 = self.get_computer_choices()
            print(f"COMPUTER_1 CHOOSE: {computer_1}")
            print(f"COMPUTER_2 CHOOSE: {computer_2}")

            result = self.determine_winner(computer_1, computer_2)

            text_1 = f"Your prediction is correct! {prediction_game} is the winner!"
            text_2 = f"Your prediction is wrong! {prediction_game} is the loser!"
            text_3 = "It's a tie! Repeat the battle!"

            if (prediction_game == self.candidate_1 and result == self.result_2) or (prediction_game == self.candidate_2 and result == self.result_3):
                print(text_1.upper())
            elif result == self.result_1:
                print(text_3.upper())
            else:
                print(text_2.upper())

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing!")
                break

game = jyankenpoi()
game.play_game()
