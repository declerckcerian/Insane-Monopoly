from .board import Board
from .properties import Properties
from .player import Player
from .dice import Dice

class Game:
  def __init__(self, number_of_players): 
    players = {}
    for i in range(number_of_players):
      players[ "p" + f"{i+1}"] = Player()
    
      
