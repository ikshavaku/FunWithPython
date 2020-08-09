#!/usr/bin/python3
import checkboard

def game(name1,name2,board):
	for i in range(1,10):
		if(i%2 != 0):
			print(name1+" make your move")
			while(1):
				pos=list(input("enter the position where you want to make your move"))
				if(checkboard.check(board,pos)):
					board[int(pos[0])-1][int(pos[1])-1] = '0'
					break
		else:
			print(name2+" make your move")
#			pos=list(input("enter the position where you want to make your move"))
			while(1):
				pos=list(input("enter the position where you want to make your move"))
				if(checkboard.check(board,pos)):
					board[int(pos[0])-1][int(pos[1])-1] = '*'
					break
		print("state of the board is")
		for eachrow in board:
			print(eachrow)
		if checkboard.checkwin(board) == '0':
			return 0
		elif checkboard.checkwin(board) == '*':
			return 1