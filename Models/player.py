from .board import Board
from .properties import Properties

class Player: 
    def __init__(self, money = 7000, investment = 0, pyramidscheme = 0, Start = "Go", show = False): 
        self.money = money
        self.investment = investment
        self.pyramidscheme = pyramidscheme
        self.properties = set()
        self.stock = set()
        self.travelvoucher = set()
        self.publicworkscard = set()

        # creating instance of classes so it f***ing works
        self.board = Board()
        self.properties = Properties('Title deeds.csv')

        if Start == "Cruise":
            self.position = ["Second", "4", 0]
        elif Start == "Go":
            self.position = ["Main", "2", 0]
        self.Update_position()
        
        if show == True:
            self.showall()

    def showbank(self):
        print(f"Bank account: {self.money}")
    def showpyramidscheme(self):
        print(f"Pyramidscheme value: {self.pyramidscheme}")
    def showinvestment(self):
        print(f"Investments: {self.investment}")
    def showproperties(self):
        print(f"Properties: {self.properties}")
    def showstocks(self):
        print(f"Stocks: {self.stock}")
    def showvouchers(self):
        print(f"Travel vouchers: {self.travelvoucher}")
    def showpublicworkscards(self):
        print(f"Public works cards: {self.publicworkscard}")
    def showposition(self):
        print(f"Position: {self.position[0]} board" + f", Ring {self.position[1]}" + f", {self.board.Full_Board[self.position[0]][self.position[1]][self.position[2]]}" )
    def showcounters(self):
        self.showbank()
        self.showinvestment()
        self.showpyramidscheme()
    def showall(self):
        self.showcounters()
        self.showproperties()
        self.showstocks()
        self.showvouchers()
        self.showpublicworkscards()
        self.showposition()

    def Update_position(self):
        self.tile_at_position = self.board.Full_Board[self.position[0]][self.position[1]][self.position[2]]
    
    # Use this to take a step in position to prevent index out of bound issues
    def Take_step(self, Backwards = False):
        self.position[2] = (self.position[2] + 1) % len(self.board.Full_Board[self.position[0]][self.position[1]])

    #
    def Move(self, steps): 
        print("--------------------------------")
        for i in range(steps):
            self.Update_position()
            print(self.tile_at_position)

            # This resolves railroads
            if self.tile_at_position in self.properties.Railroadnames and steps%2 == 0:
                check_up = str(int(self.position[1]) + 1)
                check_down = str(int(self.position[1]) - 1)
                if self.tile_at_position in self.board.Full_Board[self.position[0]][check_up]:
                    self.position[1] = check_up
                    self.position[2] = list(self.board.Full_Board[self.position[0]][check_up]).index(self.tile_at_position)
                elif self.tile_at_position in self.board.Full_Board[self.position[0]][check_down]:
                    self.position[1] = check_down
                    self.position[2] = list(self.board.Full_Board[self.position[0]][check_down]).index(self.tile_at_position)
                self.Take_step()
            
            # This will resolve London Bridge
            elif self.tile_at_position == "London Bridge" and steps >= 8:
                if steps == 8:
                    print("Player must Choose") # pop-up window needed, this is only a temporary fix
                    stay_or_cross = "Stay"
                    if stay_or_cross == "Stay":
                        None
                    else:
                        if self.position[0] == "Main":
                            self.position = ["Second", "1", 35]
                        else:
                            self.position = ["Main", "1", 47]
                else: 
                    if self.position[0] == "Main":
                        self.position = ["Second", "1", 35]
                    else:
                        self.position = ["Main", "1", 47]
                self.Take_step()



            
            # This will resolve ...
                
            
            else:
                self.Take_step()
        
            
        
        self.Update_position()
        print(self.tile_at_position)