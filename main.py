from Models.player import Player
from Models.properties import Properties
from Models.board import Board
from Models.dice import Dice

import tkinter as tk

properties = Properties('Title deeds.csv')
board = Board()
p1 = Player()
dice = Dice()
p1.Move(96)
i = list(board.Full_Board["Main"]["1"]).index("London Bridge")
print(i)