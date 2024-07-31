import numpy as np
import random
import csv 
import tkinter as tk
import time

class Player: 
    def __init__(self, money = 7000, investment = 0, pyramidscheme = 0, Start = "Go", show = False): 
        self.money = money
        self.investment = investment
        self.pyramidscheme = pyramidscheme
        self.properties = set()
        self.stock = set()
        self.travelvoucher = set()
        self.publicworkscard = set()
        self.othercards = set()
        self.tile_at_position = ""
        self.jailcount = 0
        self.is_in_jail = False

        if Start == "Cruise":
            self.position = ["Second", "4", 0]
        elif Start == "Go":
            self.position = ["Main", "2", 0]
        
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
    def showothercards(self):
        print(f"Other cards: {self.othercards}")
    def showposition(self):
        print(f"Position: {self.position[0]} board" + f", Ring {self.position[1]}" + f", {self.tile_at_position}" )
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
        self.showothercards()
        self.showposition()

class Properties:
    def __init__(self, Titledeedsfile):
        with open(Titledeedsfile,'r') as infile:
            file = csv.reader(infile, delimiter=';')
            Deeds = [row for row in file]   
            Deeds = Deeds[1:]
        
        # Titledeedelements have the form 
        # {Name : [Color, Price, Rent, 1 House, 2 Houses, 3 Houses, 4 Houses, Hotel, Skyscraper, 
        # Cost of 1 house upgrade, Public works, Amount of houses, Mortgaged if True, owner, Property-type]}
        self.Titledeeds = {}
        for row in Deeds:
            for i in range(len(row)-2): 
                row[i+2] = int(row[i+2])
            self.Titledeeds[row[0]] = {
                "color" : row[1],
                "price" : row[2],
                "rent" : row[3:9],
                "house_price" : row[10],
                "public works" : row[11],
                "houses" : 0,
                "mortgaged" : False,
                "owner" : None,
                "type" : "TD"

            }
            #self.Titledeeds[row[0]] = row[1:] 
        
        # Railroadelements have the form 
        # {Name : [Price, Rent, 2 RR owned, 3 RR owned, .., 11 RR owned, Property-type]}
        self.Railroads = {}
        self.Railroadnames = ["Jersey Central", "West Jersey Railroad", "Williamstown Railroad", "B & O Railroad", "Pennsylvania Railroad", "Short Line", "Seashore Lines", "Reading Railroad", "Atlantic Railroad", "Philadelphia Railway", "Central Railroad"]
        for Name in self.Railroadnames: 
            self.Railroads[Name] = {
                "price": 200, # price
                "rent": [25, 50, 75, 100, 150, 200, 300, 400, 550, 750, 1000], # rent
                "owner": None, # available or not
                "mortgaged" : False,
                "type" : "RR" # type
            }
        
        # Airportelements have the form 
        # {Name : [Price, Rent 1 AP owned, 2 AP owned, 3 AP owned, 4 AP owned, rent with terminal for 1 AP etc, terminal built or not, Bought, Property-type]}
        self.Airports = {}
        self.Airportnames = ["O'Hare Airport", "Los Angeles International Airport", "John F. Kennedy Airport", "Hartsfield Jackson Airport"]
        for Name in self.Airportnames: 
            self.Airports[Name] = {
                "price": 500, # price
                "rent": [60, 125, 250, 500], # rent
                "rent_w_terminal": [120, 250, 500, 1000], # rent with terminal
                "terminal": False, # terminal built or not
                "terminal_price": 250, # price of terminal
                "owner": None, # available or not
                "mortgaged" : False,
                "type" : "AP" # type
            }
        
        # Harborelements have the form 
        # {Name : [Price, Rent, 2 H owned, 3 H owned, 4 H owned, rent with port for 1 H etc, port built or not, Bought, Property-type]}
        self.Harbors = {}
        self.Harbornames = ["Chelsea Harbor", "Delta Basin", "Snug Harbor", "State Marina"]
        for Name in self.Harbornames:
            self.Harbors[Name] = {
                "price": 400, # price
                "rent": [50, 100, 200, 400], # rent
                "rent_w_port": [100, 200, 400, 800], # rent with 
                "port": False, # port built or not
                "port_price": 200, # price of port
                "owner": None, # available or not
                "mortgaged" : False,
                "type" : "H" # type
            }
        
        # Cabcompanyelements have the form
        # {Name : [Price, Rent, 2 CC owned, 3 CC owned, 4 CC owned, Bought, rent with stand for 1 CC etc, stand built or not, Property-type]}
        self.Cabcompanies = {}
        self.Cabcompanynames = ["Yellow Cab Co.", "Checker Cab Co.", "Black & White Cab Co.", "Ute Cab Co."]
        for Name in self.Cabcompanynames:
            self.Cabcompanies[Name] = {
                "price": 300, # price
                "rent": [35, 75, 150, 300], # rent
                "rent_w_stand": [70, 150, 300, 600], # rent with stand
                "stand": False, # stand built or not
                "stand_price": 150, # price of stand
                "owner": None, # available or not
                "mortgaged" : False,
                "type" : "CC" # type
            }
        
        # Monorailelements have the form 
        # {Name : [Price, Rent, 2 MR owned, 3 MR owned, 4 MR owned, Bought, Property-type]}
        self.Monorails = {}
        self.Monorailnames = ["Red Monorail", "Yellow Monorail", "Green Monorail", "Blue Monorail"]
        for Name in self.Monorailnames:
            self.Monorails[Name] = {
                "price": 600, # price
                "rent": [75, 150, 300, 600], # rent
                "owner": None, # available or not
                "mortgaged" : False,
                "type" : "MR" # type
            }
        
        # Cellblockelements have the form
        # {Name : [Price, Rent, 2 CB owned, 3 CB owned, 4 CB owned, Bought, Property-type]}
        self.Cellblocks = {}
        self.Cellblocknames = ["Cell Block A", "Cell Block B", "Cell Block C", "Cell Block D"]
        for Name in self.Cellblocknames: 
            self.Cellblocks[Name] = {
                "price": 250, # price
                "rent": [125, 250, 500, 1000], # rent
                "owner": None, # available or not
                "mortgaged" : False,
                "type" : "CB" # type
            }
        
        # Utilityelements have the form 
        # {Name : [Price, Multipliers per amount of utilities owned, Property-type]}
        self.Utilities = {}
        self.Utilitynames = ["Alarm Company", "Postal Service", "Water Works", "Cable Company", "Electric Company", "Internet Service Provider", "Gas Company", "Trash Collector", "Telephone Company", "Sewage System", "Recycling Center", "Satellite Television Provider", "Compost Center", "Cell Phone Company"]
        for Name in self.Utilitynames: 
            self.Utilities[Name] = {
                "price": 150, # price
                "rent": [4, 10, 20, 30, 40, 60, 80, 100, 150, 200, 250, 300, 400, 500], # rent
                "owner": None, # available or not
                "mortgaged" : False,
                "type" : "U" # type
            }
        
        # Stockelements have the form
        # {Name : [ Par Value, Dividents per amount of shares, Property-type, Number of available stocks]}
        self.Stocks = {
            "Motion Pictures" : {"price": 100, "dividends" : [10, 40, 90, 160, 250], "type" : 'S', "amount" : 5, "owner" : None}, 
            "Allied Steamships" : {"price" : 110, "dividends" : [11, 44, 99, 176, 275], "type":'S', "amount": 5, "owner" : None}, 
            "National Utilities" : {"price" : 120, "dividends" : [12, 48, 108, 192, 300],"type": "S","amount" : 5, "owner" : None},
            "General Radio" : {"price":130, "dividends" : [13, 52, 117, 208, 325], "type" : 'S', "amount" : 5, "owner" : None},
            "United Railways" : {"price" : 140,"dividends" : [14, 56, 126, 224, 350], "type" :'S',"amount": 5, "owner" : None},
            "American Motors" : {"price" : 150, "dividends" : [15, 60, 135, 240, 375], "type" :'S',"amount" : 5, "owner" : None}
        }
        
        # Merging all properties in one dictionary
        self.allproperties = dict()
        self.dictionaries = [self.Airports, self.Cabcompanies, self.Cellblocks, self.Harbors, self.Monorails, self.Railroads, self.Titledeeds, self.Stocks, self.Utilities]
        for dictionary in self.dictionaries: 
            self.allproperties.update(dictionary)
        
        # Making a dictionary to easily find the needed properties without using too many if statements
        self.type = {
            "TD" : self.Titledeeds,
            "U" : self.Utilities,
            "CB" : self.Cellblocks,
            "CC" : self.Cabcompanies,
            "RR" : self.Railroads,
            "S" : self.Stocks, 
            "MR" : self.Monorails,
            "H" : self.Harbors, 
            "AP" : self.Airports
        }

class Cards: #this just sets up all the cards, functions for each card will have to be added in the Game Class
    def __init__(self):
        self.Global_Events = {"Reverse, Reverse!", "Stock Market SOARS!", "Bull Market", "Authorities Tipped", "Sneaky Schemers", "Taxation Crisis!", "The Most Common Number", "..."}

class Dice:
    def __init__(self):
        self.Regularediewhite = [1,2,3,4,5,6]
        self.Regularediegreen = [1,2,3,4,5,6]
        self.Regularedieblue = [1,2,3,4,5,6]
        self.Regularedieteal = [1,2,3,4,5,6]
        self.Speeddie = [1,2,3,'Mr. Monopoly', 'Mr. Monopoly', 'Bus']
        self.Speedierdie = [4,5,6,'Mr. Monopoly', 'Mr. Monopoly', 'Bus']
        self.Investmentdie_updown = ['Investment Up','Investment Up','Investment Up','Investment Up','Investment Down','Investment Down']
        self.Investmentdie_amount = [100, 50,'15%','20%','30%','50%']
        self.Schemedie = ['Pyramid', 'Dividends', 'Investment Down by 5%', 'Investment Up by 10%', 'Single Die', 'Mystery Card']
        self.Mysterydie = ['Chance', 'Community Chest', 'Roll3!', 'Public Works','Travel Voucher', 'Global Event', 'Employee', 'Shady Business', 'Shenanigans', 'Wild']
        self.Jaildie_Oddjob = [1,2,3,4,5, 'Odd Jobs card']
        self.Jaildie_Inmate = [1,2,3,4,5, 'Inmate card']
        self.dice = [self.Regularediewhite, self.Regularediewhite, self.Regularediegreen, self.Regularedieblue,self.Regularedieteal, self.Speeddie,self.Speedierdie,self.Investmentdie_updown,self.Investmentdie_amount,self.Schemedie, self.Mysterydie,self.Jaildie_Oddjob,self.Jaildie_Inmate]
        self.roll_one = 0
        self.roll_two = 0
        self.roll_three = 0

    # This function will roll the dice and return the result
    def Roll_normal_v1(self):
        print("********************************")
        print("Rolling dice ...")

        time.sleep(1)

        self.roll_one = random.choice(self.Regularediewhite)
        self.roll_two = random.choice(self.Regularediewhite)
        self.roll_three = random.choice(self.Speeddie)
        self.total_roll = 0

        # Based on whether the speed die is a number or a special icon, the total roll will be calculated
        if self.roll_three == 1 or self.roll_three == 2 or self.roll_three == 3:
            self.total_roll = self.roll_one + self.roll_two + self.roll_three
            print(f"You rolled a {self.roll_one}, a {self.roll_two} and a {self.roll_three} for a total of {self.total_roll}!")
        else:
            self.total_roll = self.roll_one + self.roll_two
            print(f"You rolled a {self.roll_one}, a {self.roll_two} and a {self.roll_three} for a total of {self.total_roll}!")

        return self.total_roll
    
    # Pop-up window will appear for bus icon and Mr. Monopoly
    # TODO: implement functionality of the buttons
    def Rolling_monop_or_bus(self):
        if self.roll_three == "Bus":
            time.sleep(1)
            window = tk.Tk()
            window.title("Bus Icon")

            window.configure(bg='goldenrod1')

            label = tk.Label(window, text=f"You rolled a Bus Icon!", bg='goldenrod1', font=('Helvetica', 48))
            label.pack()

            stay_button = tk.Button(window, text="Draw a Travel Voucher", command=window.destroy, bg='gray', font=('Helvetica', 12), padx=10, pady=5)
            stay_button.pack(pady=15)

            cross_button = tk.Button(window, text="Advance", command=window.destroy, bg='gray', font=('Helvetica', 12), padx=10, pady=5)
            cross_button.pack(pady=15)

            window.mainloop()
        
        elif self.roll_three == "Mr. Monopoly":
            time.sleep(1)
            window = tk.Tk()
            window.title("Mr. Monopoly")

            window.configure(bg='red2')

            label = tk.Label(window, text=f"You rolled a Mr. Monopoly!", bg='red2', font=('Helvetica', 48))
            label.pack()

            stay_button = tk.Button(window, text="To be added", command=window.destroy, bg='white', font=('Helvetica', 12), padx=10, pady=5)
            stay_button.pack(pady=15)

            window.mainloop()

class Board:
    def __init__(self):
        self.Main_Ring1 = np.array(['Stock Exchange', 'Cass Ave.', 'Woodward Ave.', 'Eight Mile Rd.', 'Gratiot Ave.', 'Telegraph Rd.', 'Checker Cab Co.', "Reading Railroad", "Esplanade Ave.", "Jackson Square", "Canal St.", "Chance", "Cable Company", "Magazine St.", "Bourbon St.", "Chip Shot Challenge", "Auction", "Katy Freeway", "Westheimer Rd.", "Galveston St.", "Shady Business", "Kirbyq Dr.", "Cullen Blvd.", "Chelsea Harbor", "Black & White Cab Co.", "Piedmont Park", "Dekalb Ave.", "Community Chest","Andrew Young Intl Blvd.", "Decatur St.", "Peachtree St.", "Pay Day", "Pritzker Pavilion", "Randolph St.", "Chance", "Lake Shore Dr.", "Wacker Dr.", "Michigan Ave.", "Yellow Cab Co.", "B & O Railroad", "Shenanigans", "South Temple", "East Temple", "West Temple", "Trash Collector", "North Temple", "Temple Square", "London Bridge", "South St.", "Broad St.", "Delancey St.", "Walnut St.", "Shady Business", "Market St.", "Housing Tax", "Delta Basin", "Ute Cab Co.", "Birthday Gift", "Mulholland Dr.", "Riverside Dr.", "Ventura Blvd.", "Shenanigans", "Rodeo Dr." ])
        self.Main_Ring2 = np.array(["Go", "Mediterranean Ave.","Community Chest", "Baltic Ave.", "Arctic Ave.", "Income Tax", "Reading Railroad", "Oriental Ave.", "Chance", "Vermont Ave.", "Massachusetts Ave.", "Connecticut Ave.", "Just Visiting", "St. Charles Place", "States Ave.", "Virginia Ave.", "Pennsylvania Railroad", "St. James Place", "Community Chest", "Tennessee Ave.", "New Jersey Ave.", "New York Ave.", "Free Parking", "Kentucky Ave.", "Chance", "Indiana Ave.", "Illinois Ave.", "Arkansas Ave.", "B & O Railroad", "Atlantic Ave.", "Ventnor Ave.", "California Ave.", "Water Works", "Marvin Gardens", "Go to Jail", "Pacific Ave.", "No. Carolina Ave.", "Community Chest", "Pennsylvania Ave.","So. Carolina Ave.", "Short Line", "Chance", "Park Place", "Luxury Tax", "Ohio Ave.", "Boardwalk" ])
        self.Main_Ring3 = np.array(["Squeeze Play", "The Embarcadero", "Pasadena Blvd.", "Fisherman's Wharf", "Telephone Company", "Chance", "Beacon St.", "Bonus", "Boylston St.", "Newbury St.", "Fenway Park", "Pennsylvania Railroad", "Fifth Ave.", "Shenanigans", "Madison Ave.", "Roll3!", "Central Park", "Wall St.", "Gas Company", "Jersey Central", "Community Chest", "Florida Ave.", "Hartsfield Jackson Airport", "Subway", "Miami Ave.", "Ocean Dr.", "Biscayne Ave.", "Short Line", "Swap", "Lombard St.", "Shady Business"])
        self.Main_Ring4 = np.array(["Holland Tunnel", "Roan St.", "Wild Card", "Five Points", "Holiday Sale", "Laura St.", "Gator Bowl Blvd.", "Tax Refund", "Opening Bell", "Ponte Vedra Blvd.", "Jersey Central", "Watuaga Ave.", "Commission", "Unaka Ave.", "Stock Tax", "John Exum Parkway"])
        self.Second_Ring1 = np.array(["Stock Exchange", "Setor Noroeste", "Lago Norte", "Park Way", "Lago Sul", "Eixo Monumental", "Chance", "Independence Ave.", "Williamstown Railroad", "Pionerskaya St.", "Nyamiha St.", "Vankovica St.", "Zhasminovaya St.", "Shenanigans", "Brivibas St.", "Elizabetes St.", "Central Market", "Stimulus Check", "Kalku St.", "Albert St.", "Shady Business", "Schreiberweg", "Postal Service", "Larochegasse", "Ringstrasse", "Tuchlauben", "Snug Harbor", "Kohlmarkt", "Yellow Monorail", "Market Lane", "Oriental Parade", "Grass St.", "McFarlane St.", "Shenanigans", "Bayview Terrace", "London Bridge", "Rua Antonio Saldanha", "Rua Garrett", "Avenida Marginal", "Green Monorail", "Avenida Da Liberdade", "Rua Do Salitre", "Shady Business", "Leidsestraat", "West Jersey Railroad", "Herengracht", "Prinsengracht", "Kalverstraat","Keizergracht", "Community Chest", "Rue Du Marche Aux Fromages", "Chaussee D'Ixelles", "Ave. Louise", "Stimulus Check", "Rue Du Buisson", "Rue Neuve", "Chance", "Emirates Rd.", "Al-Khail Rd.", "Blue Monorail", "Al-Seef St.", "Jumeirah St.", "State Marina", "Sheikh Zayed Rd.", "Community Chest", "Ave. De La Madone", "Ave. De La Costa", "Alarm Company", "Place Du Casino", "Ave. Princesse Grace", "Investment Tax"])
        self.Second_Ring2 = np.array(["Draw an Employee Card", "Ujazdow Ave.", "Nowy Swiat St.", "Community Chest", "Kirkeveien", "Bogstadveien", "Pilestredet", "Williamstown Railroad", "Karl Johans Gate", "Ulleval Hageby", "Shady Business", "Avenida De Asturias", "Paseo Del Prado", "Calle De Alcala", "Squeeze Play", "Tax Break", "Calle De Serrano", "Gran Via", "Chance", "Majura Rd.", "Londen Circuit", "Central Railroad", "Garema Place", "Property Tax", "Bunda St.", "Kings Ave.", "Shenanigans", "Rue Lafayette", "Go to Jail", "Ave. Henri-Martin", "Rue De La Paix", "Cell Phone Company", "Ave. Des Champs-Elysees", "Ave. Foch", "Chance", "West Jersey Railroad", "Burkliplatz", "Rennweg", "Limmatquai", "Bahnhofstrasse", "Paradeplatz", "Pyramid Scheme", "Shenanigans", "Calle Genova", "Avenida Madero", "Internet Service Provider", "Avenida Mexico", "Eje Central", "Seashore Lines", "Avenida Insurgentes", "Shady Business", "Shady Business", "Wolska St.", "Miodowa St.", "Speeding Fine", "Marsa St."])
        self.Second_Ring3 = np.array(["Investment" , "Shenanigans", "Via Sacra", "Piazza Del Popolo", "Via Dei Condotti", "Philadelphia Railway", "Abbey Rd.", "Sewage System", "Downing St.", "Trafalgar Square", "Lotto", "Mayfair", "Oxford St.", "O'Hare Airport", "Chausseestrasse", "Central Railroad", "Potsdam Square", "Eberstrasse", "Shady Business", "Unter Den Linden", "Global Event", "Kurfurstendamm", "Community Chest", "Satellite Television Provider", "Gotgatan", "Atlantic Railroad", "Kopmangatan", "Nytorget Square", "Import Tariff", "Strandvagen", "Subway", "Union St.", "Chance", "Academy St.", "Church St.", "Seashore Lines", "High St." ,"John F. Kennedy Airport", "Via Del Corso", "Gianicolo Promenade"])
        self.Second_Ring4 = np.array(["Cruise", "Belvedere Place", "Summit Circle", "Philadelphia Railway", "Community Chest", "Arbat St.", "Holland Tunnel", "Tverskaya St.", "Theatre Square", "Compost Center", "Red Square", "Shenanigans", "Roll3!", "Mosaic St.", "Omotesando Ave.", "Atlantic Railroad", "Chance", "Shibuya Crossing", "Shinkansen", "Ginza", "Recycling Center", "The Boulevard","Sherbrooke St.", "Shady Business"])
        self.Jail_Ring1 = np.array(["Entry1", "Possessions Seized", "Additional Charges", "Roll Call", "Land Seized", "Cell Block A", "Settlement", "Sentence Reduced", "Inmate Card", "Antitrust", "Odd Jobs", "Get Therapy", "Make A Friend", "Pyramid Scheme Discovered!", "Inmate Card", "Cell Block B", "Caught Smuggling", "Lawyer Bill", "Community Service", "Guard Pockets Bribe", "Odd Jobs", "Inmate Card", "Pardoned!", "Take Classes", "Conduct Violation", "Cell Block C", "Employee Poaching", "Inmate Card", "Tax Embezzlement", "Spoon Digging", "Escape Tunnel", "Caught Escaping", "Inmate Card", "Make A Friend", "Perjury", "Cell Block D", "Reverse Direction", "insider Trading", "Release Paperwork", "Inmate Of The Year", "Post Bail"])
        self.Jail_Ring2 = np.array(["Entry2", "Retrial", "Skilled Cellmate", "Cell Block A", "House Arrest", "Dumpster Diving", "Odd jobs", "Inmate Card", "Asset Forfeiture", "Cell Block B", "Legal Fines", "Caught With Contraband", "Odd jobs", "Assets Frozen", "Inmate Card", "Cell Block C", "Mistrial", "Make A Friend", "Odd Jobs", "Community Service", "Cell Block D", "Model inmate", "Exploit Legal Loophole", "Post Bail"])

        # Use of dictionaries to reduce a players position to 3 variables
        self.Main = {"1" : self.Main_Ring1, "2" : self.Main_Ring2, "3" : self.Main_Ring3, "4" : self.Main_Ring4 }
        self.Second = {"1" : self.Second_Ring1, "2" : self.Second_Ring2, "3" : self.Second_Ring3, "4" : self.Second_Ring4 }
        self.Jail = {"1" : self.Jail_Ring1, "2" : self.Jail_Ring2}

        self.Full_Board = {"Main" : self.Main, "Second" : self.Second, "Jail" : self.Jail}

class Game:
    def __init__(self, number_of_players): 
        # Creating an instance of classes so it F***ing works :)
        self.board = Board()
        self.properties = Properties('Title deeds.csv')
        self.dice = Dice()
        self.pool = 0
        self.special_action_allowed = False
        self.move_with_travelvoucher = False
        
        # Initiating players
        self.p = []
        for i in range(number_of_players):
            self.p.append(Player())
            self.Update_position(i)

    def Update_position(self,player_index):
        self.p[player_index].tile_at_position = self.board.Full_Board[self.p[player_index].position[0]][self.p[player_index].position[1]][self.p[player_index].position[2]]
    
    # Use this to take a step in position to prevent index out of bound issues
    def Take_step(self, player_index, Backwards = False):
        self.p[player_index].position[2] = (self.p[player_index].position[2] + 1) % len(self.board.Full_Board[self.p[player_index].position[0]][self.p[player_index].position[1]])
    
    # This function will move players directly to a certain tile, without rolling dice. Can be used f.e. with the Mr. Monopoly move, Go To Jail, etc ...
    def Move_directly(self, player_index, board, ring, tile_index):
        self.p[player_index].position[0] = board
        self.p[player_index].position[1] = ring
        self.p[player_index].position[2] = tile_index
        self.Update_position(player_index)

        if board == "Main" and ring == "1" and tile_index == 31:
            self.Collect_Paycorner_highest(player_index, "Pay Day")
    
    # This function can be used to move players while using travel vouchers that say the exact amount of steps forward or backwards
    def Move_in_steps(self, player_index, steps, backwards):
        self.move_with_travelvoucher = True
        if backwards == False:
            for i in range(steps):
                self.Update_position(player_index)
                print(self.p[player_index].tile_at_position)

                # This resolves railroads
                if self.p[player_index].tile_at_position in self.properties.Railroadnames and steps%2 == 0:
                    self.Pass_Railroad(player_index)
            
                # This will resolve London Bridge
                elif self.p[player_index].tile_at_position == "London Bridge" and steps >= 8:
                    self.Pass_LondonBridge(player_index,steps) 

                # This will resolve PASSING Go, landing on Go is in Tile_event()
                elif self.p[player_index].tile_at_position == "Go" and i>0: 
                    self.Collect_Paycorner_highest(player_index, "Go")
                    self.Take_step(player_index)
            
                # This will resolve PASSING Cruise
                elif self.p[player_index].tile_at_position == "Cruise" and i>0:
                    self.Collect_Paycorner_highest(player_index, "Cruise")
                    self.Take_step(player_index)
            
                # This will Pass Bonus, landing on Bonus is in Tile_event()
                elif self.p[player_index].tile_at_position == "Bonus" and i>0:
                    self.Collect_Paycorner_highest(player_index, "Bonus")
                    self.Take_step(player_index)
                
                # !! This will Pass Pay Day, landing on Pay Day is in Tile_event() but needs fixing because dice roll are still incorperated in there!!!!
                elif self.p[player_index].tile_at_position == "Pay Day" and i>0:
                    self.Collect_Paycorner_highest(player_index, "Pay Day")
                    self.Take_step(player_index)
                
                # This will pass Stimulus Check, landing on it gives nothing
                elif self.p[player_index].tile_at_position == "Stimulus Check" and i>0:
                    self.Collect_Paycorner_highest(player_index, "Stimulus Check")
                    self.Take_step(player_index)

                else:
                    self.Take_step(player_index)

            self.Update_position(player_index)
            print(self.p[player_index].tile_at_position)
        
            self.Tile_event(player_index)

    
    # Passing railroads
    def Pass_Railroad(self, player_index):
        check_up = str(int(self.p[player_index].position[1]) + 1)
        check_down = str(int(self.p[player_index].position[1]) - 1)
        if self.p[player_index].tile_at_position in self.board.Full_Board[self.p[player_index].position[0]][check_up]:
            self.p[player_index].position[1] = check_up
            self.p[player_index].position[2] = list(self.board.Full_Board[self.p[player_index].position[0]][check_up]).index(self.p[player_index].tile_at_position)
        elif self.p[player_index].tile_at_position in self.board.Full_Board[self.p[player_index].position[0]][check_down]:
            self.p[player_index].position[1] = check_down
            self.p[player_index].position[2] = list(self.board.Full_Board[self.p[player_index].position[0]][check_down]).index(self.p[player_index].tile_at_position)
        self.Take_step(player_index)
    
    # Passing or landing on London bridge
    def Pass_LondonBridge(self, player_index, steps):
        def stay():
            window.destroy()

        def cross():
            if self.p[player_index].position[0] == "Main":
                self.p[player_index].position = ["Second", "1", 35]
            else:
                self.p[player_index].position = ["Main", "1", 47]
            window.destroy()

        if steps == 8:
            window = tk.Tk()
            window.title("London Bridge Decision")

            window.configure(bg='pink')

            label = tk.Label(window, text=f"Player must choose", bg='pink', font=('Helvetica', 48))
            label.pack()

            stay_button = tk.Button(window, text="Stay", command=stay, bg='lightblue', font=('Helvetica', 12), padx=10, pady=5)
            stay_button.pack(pady=15)

            cross_button = tk.Button(window, text="Cross", command=cross, bg='lightblue', font=('Helvetica', 12), padx=10, pady=5)
            cross_button.pack(pady=15)

            window.mainloop()
        else:
            print("You're crossing the London Bridge...")
            time.sleep(2) 
            if self.p[player_index].position[0] == "Main":
                self.p[player_index].position = ["Second", "1", 35]
            else:
                self.p[player_index].position = ["Main", "1", 47]
                
        self.Take_step(player_index)
        
    # Landing on Holland Tunnel
    def Land_HollandTunnel(self, player_index):
        print("You're crossing the Holland Tunnel ...")
        time.sleep(2)
        if self.p[player_index].position[0] == "Main":
            self.p[player_index].position = ["Second", "4", 6]
        else:
            self.p[player_index].position = ["Main", "4", 0]
         
    def Pass_Go(self, player_index):
        print("You passed Go! + 200$ ")
        self.p[player_index].money += 200
        time.sleep(1)
        self.Take_step(player_index)
    
    def Pass_Cruise(self, player_index):
        if self.dice.total_roll == 10 or self.dice.total_roll == 11 or self.dice.total_roll == 12:
            print(self.dice.total_roll)
            print("You passed Cruise! + 100$")
            self.p[player_index].money += 100
        elif self.dice.total_roll == 6 or self.dice.total_roll == 7 or self.dice.total_roll == 8 or self.dice.total_roll == 9:
            print(self.dice.total_roll)
            print("You passed Cruise! + 200$")
            self.p[player_index].money += 200
        elif self.dice.total_roll <= 5:
            print(self.dice.total_roll)
            print("You passed Cruise! + 300$")
            self.p[player_index].money += 300
        time.sleep(1)
        self.Take_step(player_index)
    
    def Collect_Paycorner_highest(self, player_index, case):
        if case == "Go":
            print("You receive a bonus! 200$")
            self.p[player_index].money += 200
        elif case == "Cruise" or "Bonus":
            print("You receive a bonus! 300$")
            self.p[player_index].money += 300
        elif case == "Pay Day":
            print("You receive a bonus! 400$")
            self.p[player_index].money += 400
        elif case == "Stimulus Check":
            print("You receive a bonus! 500$")
            self.p[player_index].money += 500
        time.sleep(1)
            
    def Pass_Bonus(self, player_index):
        print("You receive a bonus!\n + 250$")
        self.p[player_index].money += 250
        time.sleep(1)
        self.Take_step(player_index)
    
    def Pass_stimcheck(self, player_index):
        if self.dice.total_roll <= 5:
            print("You passed Stimulus Check! + 300$")
            self.p[player_index].money += 300
        elif self.dice.total_roll == 6 or self.dice.total_roll == 7 or self.dice.total_roll == 8 or self.dice.total_roll == 9:
            print("You passed Stimulus Check! + 400$")
            self.p[player_index].money += 400
        else:
            print("You passed Stimulus Check! + 500$")
            self.p[player_index].money += 500
        time.sleep(1)
        self.Take_step(player_index)
    
    def Pay_day(self, player_index):
        if self.dice.total_roll % 2 != 0:
            print("Pay Day! + 300$")
            self.p[player_index].money += 300
        else:
            print("Pay Day! + 400$")
            self.p[player_index].money += 400
        time.sleep(1)
    
    # If Commission is landed on or passed from a Single Die Bonus Move, only the pips
    # showing on that die are considered: this still needs implementation !
    def Commission(self, player_index):
        bonus = self.dice.total_roll * 20
        print(f"Commission! You receive {bonus}$")
        self.p[player_index].money += bonus
        time.sleep(1)
    
    def Go_to_Jail(self, player_index):
        time.sleep(1)
        window = tk.Tk()
        window.title("Go to Jail")

        window.configure(bg='LavenderBlush4')

        label = tk.Label(window, text=f"Uh-oh! You're going to jail!", fg='white', bg='LavenderBlush4', font=('Helvetica', 36))
        label.pack()

        button = tk.Button(window, text="Ah sh*t", command=window.destroy, bg='white', font=('Helvetica', 12), padx=10, pady=5)
        button.pack(pady=15)

        window.mainloop()

        if self.p[player_index].jailcount < 3:
               self.Move_directly(player_index, "Jail", "2", 0)
               self.p[player_index].jailcount += 1
        else:
                self.Move_directly(player_index, "Jail", "1", 0)
                self.p[player_index].jailcount += 1
    
    '''
    def printAllPlayers(self):
        for player in self.p:
            player.showbank()
    '''
    # These functions can be used to transfer money between players
    def receiveMoneyFromPlayers(self, player_index, amount):
        self.p[player_index].money += amount
        for i in range(len(self.p)):
            if i != player_index:
                self.p[i].money -= amount
        print(f"Player {player_index} received {amount}$ from all other players")
        time.sleep(1)
    
    def receiveMoneyFromOnePlayer(self, player_index, target, amount):
        self.p[player_index].money += amount
        self.p[target].money -= amount
        print(f"Player {player_index} received {amount}$ from player {target}")
        time.sleep(1)

    # This will perform all the actions for the tile that was landed on
    def Tile_event(self, player_index):
       # Checking if player landed on "Go To Jail and perform the necessary actions"
        if self.p[player_index].tile_at_position == "Go to Jail":
            self.Go_to_Jail(player_index)
        
        # Checking if player landed on the Holland Tunnel
        elif self.p[player_index].tile_at_position == "Holland Tunnel":
                self.Land_HollandTunnel(player_index)
        
        # Checking if player landed on "Tax Break" and perform the necessary actions
        elif self.p[player_index].tile_at_position == "Tax Break":
            receive = self.pool / 4
            self.p[player_index].money += receive
            self.pool -= receive
            print(f"Player received {receive}$ from the pool")
            time.sleep(1)
        
        # Checking if player landed on "Tax Refund" and perform the necessary actions
        elif self.p[player_index].tile_at_position == "Tax Refund":
            receive = self.pool / 2
            self.p[player_index].money += receive
            self.pool -= receive
            print(f"Player received {receive}$ from the pool")
            time.sleep(1)
        
        # Checking if player landed on one of the pay corners
        elif self.p[player_index].tile_at_position == "Bonus":
            self.Collect_Paycorner_highest(player_index, "Bonus")
        
        elif self.p[player_index].tile_at_position == "Go":
            self.Collect_Paycorner_highest(player_index, "Go")
        
        elif self.p[player_index].tile_at_position == "Pay Day":
            if self.move_with_travelvoucher == True:
                self.Collect_Paycorner_highest(player_index, "Pay Day")
            else:
                self.Pay_day(player_index)
        
        # Still needs fixing for when landing with travel voucher
        elif self.p[player_index].tile_at_position == "Commission":
            self.Commission(player_index)
        
        # If player lands on Stimulus Check, normal routine; if player landed with travel voucher or bonus move he gets highest reward
        elif self.p[player_index].tile_at_position == "Stimulus Check":
            if self.move_with_travelvoucher == True:
                self.Collect_Paycorner_highest(player_index, "Stimulus Check")
            else:
                self.Pass_stimcheck(player_index)
        
        elif self.p[player_index].tile_at_position == "Speeding Fine":
            fine = self.dice.total_roll * 30
            print(f"Speeding Fine! You pay {fine}$")
            self.p[player_index].money -= fine
            time.sleep(1)
        
        self.special_action_allowed = True
            
            


    # This Moves the player on the board for a given roll and performs any action necessary in passing tiles.
    def Move_with_dice(self,player_index):
        self.move_with_travelvoucher = False
        steps = self.dice.Roll_normal_v1()
        print("--------------------------------")
        for i in range(steps):
            self.Update_position(player_index)
            print(self.p[player_index].tile_at_position)

            # This resolves railroads
            if self.p[player_index].tile_at_position in self.properties.Railroadnames and steps%2 == 0:
                self.Pass_Railroad(player_index)
            
            # This will resolve London Bridge
            elif self.p[player_index].tile_at_position == "London Bridge" and steps >= 8:
                self.Pass_LondonBridge(player_index,steps) 

            # This will resolve PASSING Go, landing on Go requires a different function
            elif self.p[player_index].tile_at_position == "Go" and i>0: 
                self.Pass_Go(player_index)
            
            # This will resolve PASSING Cruise
            elif self.p[player_index].tile_at_position == "Cruise" and i>0:
                self.Pass_Cruise(player_index)
            
            # This will Pass bonus, landing on bonus is in Tile_event()
            elif self.p[player_index].tile_at_position == "Bonus" and i>0:
                self.Pass_Bonus(player_index)
            
            # This will pass Pay Day, landing on Pay Day is in Tile_event()
            elif self.p[player_index].tile_at_position == "Pay Day" and i>0:
                self.Pay_day(player_index)
                self.Take_step(player_index)
            
            # This will pass Stimulus Check, landing on it is in Tile_event()
            elif self.p[player_index].tile_at_position == "Stimulus Check" and i>0:
                self.Pass_stimcheck(player_index)
            
            # This will pass Commision, landing on it is in Tile_event()
            elif self.p[player_index].tile_at_position == "Commission" and i>0:
                self.Commission(player_index)
                self.Take_step(player_index)

            else:
                self.Take_step(player_index)

        self.Update_position(player_index)
        print(self.p[player_index].tile_at_position)
        
        # After moving is done, tile event will be resolved
        self.Tile_event(player_index)

        # Calling special dice functions if player has rolled a special icon, checks are built-in the function
        # Will only happen after all regular tile events have been resolved
        if self.special_action_allowed == True:
            self.dice.Rolling_monop_or_bus()
    
    # Buying properties 
    def Buy_property(self, player_index, propertyname):
        if self.properties.allproperties[propertyname]["owner"] == None:
            self.p[player_index].money -= self.properties.allproperties[propertyname]["price"]
            self.properties.allproperties[propertyname]["owner"] = player_index
            print(f"Player {player_index} bought {propertyname} for {self.properties.allproperties[propertyname]['price']}$")
            time.sleep(1)
        else: 
            print(f"Property is alread owned by player {self.properties.allproperties[propertyname]['owner']} ")
            time.sleep(1)
        self.Update_owned_properties(player_index)
    
    def Update_owned_properties(self, player_index):
        for propname in self.properties.allproperties: 
            if self.properties.allproperties[propname]["owner"] == player_index: 
                self.p[player_index].properties.add(propname)
            



    # Updating how many RRs, MRs, CCs, etc. are owned by each player by changing the rent_index
    def Update_amount_of_props_owned(self):
        None

    
        
        
          
                
    






game = Game(4)
# Test case for receiving money from other players
'''
game.receiveMoneyFromPlayers(2, 1000)
game.receiveMoneyFromOnePlayer(0, 3, 550)
game.p[0].showbank()
game.p[2].showbank()
game.p[3].showbank()
'''

# testcase for buying properties
game.Buy_property(0, "Cass Ave.")
game.p[0].showbank()
game.Buy_property(1,"Cass Ave.")
game.p[0].showproperties()

# test case for railroads
'''
game.Move_with_dice(3)
game.p[3].showposition()
'''


# test case for London bridge
'''
game.p[2].showposition()
game.Move_with_dice(2,78)
game.Move_with_dice(2,1)
game.p[2].showposition()
game.Move_with_dice(2,8)
game.p[2].showposition()
'''

#test case for Go
'''
game.Move_with_dice(0,45)
game.Move_with_dice(0,1)
game.p[0].showall()
'''

#test case Bonus
'''
game.Move_with_dice(1,48)
game.Move_with_dice(1,14)
game.p[1].showall()
'''

#test case for rolling dice
'''
dice = Dice()
dice.Roll_normal_v1()
'''

#test case for moving directly
'''
game.p[0].showposition()
game.Move_directly(0, "Main", "1", 31),
game.p[0].showposition()

'''












