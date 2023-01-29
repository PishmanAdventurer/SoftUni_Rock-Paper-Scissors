import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
comp_move = ""

player_move = input("Chose [r]ock, [p]aper or [s]cissors:")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

comp_rand_num = random.randint(1, 3)

if comp_rand_num == 1:
    comp_move = rock
elif comp_rand_num == 2:
    comp_move = paper
elif comp_rand_num == 3:
    comp_move = scissors

print(f"The Computer chose {comp_move} and You chose {player_move}.")

if comp_move == player_move:
    print("Draw")
elif (comp_move == rock and player_move == paper) or (comp_move == paper and player_move == scissors) or \
        (comp_move == scissors and player_move == rock):
    print("You Win!")
else:
    print("You Lose!")
