from os import system, name
from random import randint
import time

white = "\033[0;37m"
chip = "⬤"
yellow = "\033[0;93m"
red = "\033[0;31m"
blue = "\033[0;34m"
turn = 1

#Clears the Terminal
def clear():
    if name == 'nt': system('cls')
    else: system('clear')

#Displays the Gameboard
def printBoard(board):
	for row in reversed(board):
		for tile in row:
			print(tile, end = " ")
		print("\n", end="")

#Returns first available tile in column if column is available. Returns -1 otherwise
def checkPlacement(columnNum,board):
	for index in range(len(board)):
		if board[index][columnNum - 1] == white + "-":
			return index + 1
	return -1

#Places coloured chip on board
def placeChip(rowNum,columnNum,playerNum,board):
	if playerNum == 1:
		board[rowNum - 1][columnNum - 1] = yellow + chip
	elif playerNum == 2:
		board[rowNum - 1][columnNum - 1] = red + chip
	elif playerNum == "Clear":
		board[rowNum - 1][columnNum - 1] = white + "-"
		

#Checks Horizontal Wins
def checkHorizontal(board):
	for column in range(len(board[0])-3):
		for row in range(len(board)):
			if all(i == red + chip for i in board[row][column:column + 4]):
				#for index in range(column,column + 4): board[row][index] = blue + chip
				return "Red Wins"
			if all(i == yellow + chip for i in board[row][column:column + 4]):
				#for index in range(column,column + 4): board[row][index] = blue + chip
				return "Yellow Wins"

#Checks Vertical Wins
def checkVertical(board):
	for column in range(len(board[0])):
		for row in range(len(board) - 3):
			if all(item[column] == red + chip for item in board[row:row + 4]):
				#for index in range(row,row + 4): board[index][column] = blue + chip
				return "Red Wins"
			if all(item[column] == yellow + chip for item in board[row:row + 4]):
				#for index in range(row,row + 4): board[index][column] = blue + chip
				return "Yellow Wins"

#Checks Positive Diagonal Wins
def checkPosDiagonal(board):
	for column in range(len(board[0]) - 3):
		for row in range(len(board) - 3):
			if all(item[column + index] == red + chip for index,item in enumerate(board[row:row + 4])):
				#for index in range(4): board[row + index][column + index] = blue + chip
				return "Red Wins"
			if all(item[column + index] == yellow + chip for index,item in enumerate(board[row:row + 4])):
				#for index in range(4): board[row + index][column + index] = blue + chip
				return "Yellow Wins"

#Checks Negative Diagonal Wins
def checkNegativeDiagonal(board):
	for column in range(len(board[0]) - 1,len(board[0]) - 5,-1):
		for row in range(len(board) - 3):
			if all(item[column - index] == red + chip for index,item in enumerate(board[row:row + 4])):
				#for index in range(4): board[row + index][column - index] = blue + chip
				return "Red Wins"
			if all(item[column - index] == yellow + chip for index,item in enumerate(board[row:row + 4])):
				#for index in range(4): board[row + index][column - index] = blue + chip
				return "Yellow Wins"

#Runs check win functions
def checkWin(board):
	Horizontal = checkHorizontal(board)
	Vertical = checkVertical(board)
	PosDiagonal = checkPosDiagonal(board)
	NegativeDiagonal = checkNegativeDiagonal(board)
	if Horizontal != None:
		return Horizontal
	if Vertical != None:
		return Vertical
	if PosDiagonal != None:
		return PosDiagonal
	if NegativeDiagonal != None:
		return NegativeDiagonal

def isMovesLeft(board):
	for collumn in board:
		for tile in collumn:
			if tile == white + "-":
				return True
	return False