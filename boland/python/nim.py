# nim.py

# Latoya Boland
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: https://www.youtube.com/watch?v=cYPtxxV4wYk

#Game settings
StoneAmount=0
turn=1
GameEnd=False

#Game Start
StoneAmount=int(input("Choose the amount of stones to start the game: "))

#Loop...Stones left after each turn
StoneAmountToTake=0
while GameEnd=False:
	print("total number of remaining stones: "+str(StoneAmount))

#Game Loop...each player conditions for next turn or win
	
	if turn==1:
		print("Player 1's turn")
		StoneAmountToTake=int(input("Choose an amount of stones between (1-3): "))
		StoneAmount-StoneAmount-StoneAmountToTake
		if StoneAmount==0
			GameEnd=True
			print("Winner is Player 1")
		turn=2
		
  elif turn==2:
		print("Player 2's turn")
		StoneAmountToTake=int(input("Choose an amount of stones between (1-3): "))
		StoneAmount-StoneAmount-StoneAmountToTake
		if StoneAmount==0
			GameEnd=True
			print("Winner is Player 2")
		turn=3

	else:
		print("Computer's turn")
		StoneAmountToTake=int(input("Choose an amount of stones between (1-3): "))
		StoneAmount-StoneAmount-StoneAmountToTake
		if StoneAmount==0
			GameEnd=True
			print("Winner is Computer")
		turn=1
		