#!/usr/bin/python3

def check(board,position):
	if len(position) != 2:
		print("enter the position correctly please")
		return 0
	elif(int(position[0])-1)>2 or int(position[1])-1>2 :
		print("enter a valid position")
		return 0
	elif board[int(position[0])-1][int(position[1])-1] != '.' :
		print("the position is already taken.Kindly enter a valid position")
		return 0
	else :
		return 1
def checkwin(board):
	for eachrow in board :
		if eachrow[0]== eachrow[1] and eachrow[1] == eachrow[2]:
			return eachrow[0]
	for i in range(3):
		if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
			return board[1][i]
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
				return board[0][0]
	elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
				return board[0][2]
