import random

comp_choice = random.choice(["rock", "paper", "scissors"])
player_choice = input("Player 1, choose ur player: ")

if player_choice == comp_choice:
	print("tie")
elif player_choice == "rock":
	if comp_choice == "scissors":
		print("player1 wins!")
	elif comp_choice == "paper":
		print("player2 wins!")
elif player_choice == "paper":
	if comp_choice == "rock":
		print("player1 wins!")
	elif comp_choice == "scissors":
		print("player2 wins!")
elif player_choice == "scissors":
	if comp_choice == "paper":
		print("player1 wins!")
	elif comp_choice == "rock":
		print("player2 wins!")	
else:
	print("something went wrong")