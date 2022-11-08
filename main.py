from game import *

board = [[white + "-" for i in range(7)]for i in range(6)]

#Asks player for column number
def playerTurn(board):
	columnNum = input(white + "Enter a column number:")
	if columnNum.isnumeric() and int(columnNum) <= len(board[0]):
		columnNum = int(columnNum)
		rowNum = checkPlacement(columnNum,board)
	else:
		return False
	if rowNum != -1:
		placeChip(rowNum,columnNum,1,board)
		return True
	else:
		return False

def AITurn(board):
	return None

def minimax(board, depth, isMax):
	score = checkWin(board)

	if score == "Yellow Wins":
		return -10

	if score == "Red Wins":
		return 10

	if isMovesLeft(board) == False:
		return 0

	if depth > 4:
		return 0
	
	if isMax:
		bestVal = -1000
		for column in range(1,8):
			rowNum = checkPlacement(column,board)
			if rowNum != -1:
				placeChip(rowNum,column,2,board)
				printBoard(board)
				print()
			value = minimax(board, depth+1, False)
			estVal = max(bestVal, value) 
			placeChip(rowNum,column,"Clear",board)
		return bestVal
	else:
		bestVal =1000 
		for column in range(1,8):
			rowNum = checkPlacement(column,board)
			if rowNum != -1:
				placeChip(rowNum,column,1,board)
				printBoard(board)
				print()
			value = minimax(board, depth+1, True)
			estVal = max(bestVal, value) 
			placeChip(rowNum,column,"Clear",board)
		return bestVal
			
def findBestMove(board):
	bestVal = -1000
	bestMove = -1
	for column in range(1,8):
			rowNum = checkPlacement(column,board)
			if rowNum != -1:
				placeChip(rowNum,column,2,board)
			value = minimax(board, 0, False)
			if value > bestVal:
				bestMove = column
				bestVal = value
			placeChip(rowNum,column,"Clear",board)
	print("Best Move is ", column)
	

				
#Main game loop
start = time.time()
while turn > 0:
	if turn % 2 != 0:
		if playerTurn(board) == True:
			turn += 1
		else:
			print("Invalid Input")
	elif turn % 2 == 0:
		findBestMove(board)
		AITurn(board)
		turn +=1

	winner = checkWin(board)

	#clear()
	printBoard(board)
	
	if winner != None:
		print(winner)
		turn = -1
end = time.time()
print(end - start)