#Computer1 Versus Computer2

import random

candidate_1 = "Computer_1"
candidate_2 = "Computer_2"

candidate = [candidate_1, candidate_2]

#input

print("Welcome to the Prediction Game!")
prediction_game = input("Who do you think is going to win the battle? {} or {}?".format(candidate_1, candidate_2))

# multistrings

possibility_1 = """
            __________
          /         __|
----------          __|
----------          __|
          \         __|
           ___________/
"""
possibility_2 = """
            _____________
          /         _____|____
----------          __________|
----------          ___________|
          \         _________|
            ________________|
"""
possibility_3 = """
            _______
          /        \____________
----------       \  \___________|
----------        \  \__________|
          \   |____\_/___|
           \__|________|
"""

result_1 = "It's a tie!"
result_2 = "Computer_1 win!"
result_3 = "Computer_2 win!"

print("Let's play Rock, Paper, Scissors!")
print("Rock beats Scissors")
print("Paper beats Rock")
print("Scissors beats Paper")

#tuple

possibilities = [possibility_1, possibility_2, possibility_3]

Computer_1 = random.choice(possibilities)
Computer_2 = random.choice(possibilities)

print(f"Computer_1 choose : {Computer_1}")
print(f"Computer_2 choose : {Computer_2}")

if Computer_1 == Computer_2:
    result = result_1
elif Computer_1 == possibility_1 and Computer_2 == possibility_3:
    result = result_2
elif Computer_1 == possibility_2 and Computer_2 == possibility_1:
    result = result_2
elif Computer_1 == possibility_3 and Computer_2 == possibility_2:
    result = result_2
else:
    result = result_3

#boolean, AND & OR function

text_1= f"Your prediction is correct!{prediction_game} is the winner!"
text_2= f"Your prediction is wrong!{prediction_game} is the loser!"
text_3= "It's a tie! Repeat the battle!"

if (prediction_game == candidate_1 and result == result_2) or (prediction_game == candidate_2 and result == result_3):
    print(text_1.upper())
elif result == result_1:
    print(text_3.upper())
else:
    print(text_2.upper())
