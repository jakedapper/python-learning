print("rock paper scissorsssss")

player1 = input("player one - choose one: ")
print("***NO CHEATING!\n\n" * 20)
player2 = input("player two - choose one: ")

if player1 == player2:
	print("tie")
elif player1 == "rock":
	if player2 == "scissors":
		print("player1 wins!")
	elif player2 == "paper":
		print("player2 wins!")
elif player1 == "paper":
	if player2 == "rock":
		print("player1 wins!")
	elif player2 == "scissors":z
		print("player2 wins!")
elif player1 == "scissors":
	if player2 == "paper":
		print("player1 wins!")
	elif player2 == "rock":
		print("player2 wins!")	
else:
	print("something went wrong")