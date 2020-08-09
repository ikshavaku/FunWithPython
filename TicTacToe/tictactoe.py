#!/usr/bin/python3

import game
import sys

a=[['.','.','.'],
   ['.','.','.'],
   ['.','.','.']]

player1=input("enter the name of player 1--------> ")
player2=input("enter the name of player 2--------> ")

#print(player1+" gets 0 and "+player2+" gets *")
choice=input("who will take the first turn-------> ")

if choice ==player1:
	g=game.game(player1,player2,a)
elif choice == player2:
	g=game.game(player2,player1,a)
else:
	print("enter a valid choice")
	sys.exit()
if g==0:
	print(player1+" wins")
elif g==1:
	print(player2+" wins")
elif g==None:
	print("Match Draw!!!!")