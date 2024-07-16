import csv

class Properties:
    def __init__(self, Titledeedsfile):
        with open(Titledeedsfile,'r') as infile:
            file = csv.reader(infile, delimiter=';')
            Deeds = [row for row in file]   
            Deeds = Deeds[1:]
        
        # Titledeedelements have the form 
        # {Name : [Color, Price, Rent, 1 House, 2 Houses, 3 Houses, 4 Houses, Hotel, Skyscraper, 
        # Cost of 1 house upgrade, Public works, Amount of houses, Mortgaged if True, Property-type]}
        self.Titledeeds = {}
        for row in Deeds:
            for i in range(len(row)-2): 
                row[i+2] = int(row[i+2])
            row.append(0)
            row.append(False)
            row.append('TD')
            self.Titledeeds[row[0]] = row[1:] 
        
        # Railroadelements have the form 
        # {Name : [Price, Rent, 2 RR owned, 3 RR owned, .., 11 RR owned, Property-type]}
        self.Railroads = {}
        self.Railroadnames = ['Jersey Central', 'West Jersey Railroad', 'Williamstown Railroad', 'B & O Railroad', 'Pennsylvania Railroad', 'Short Line', 'Seashore Lines', 'Reading Railroad', 'Atlantic Railroad', 'Philadelphia Railway', 'Central Railroad']
        for Name in self.Railroadnames: 
            self.Railroads[Name] = [200, 25, 50, 75, 100, 150, 200, 300, 400, 550, 750, 1000, 'RR']
        
        # Airportelements have the form 
        # {Name : [Price, Rent, 2 AP owned, 3 AP owned, 4 AP owned, Property-type]}
        self.Airports = {}
        self.Airportnames = ["O'Hare Airport", "Los Angeles International Airport", "John F. Kennedy Airport", "Hartsfield Jackson Airport"]
        for Name in self.Airportnames: 
            self.Airports[Name] = [500, 60, 125, 250, 500, 'AP']
        
        # Harborelements have the form 
        # {Name : [Price, Rent, 2 H owned, 3 H owned, 4 H owned, Property-type]}
        self.Harbors = {}
        self.Harbornames = ["Chelsea Harbor", "Delta Basin", "Snug Harbor", "State Marina"]
        for Name in self.Harbornames:
            self.Harbors[Name] = [400, 50, 100, 200, 400, 'H']
        
        # Cabcompanyelements have the form
        # {Name : [Price, Rent, 2 CC owned, 3 CC owned, 4 CC owned, Property-type]}
        self.Cabcompanies = {}
        self.Cabcompanynames = ["Yellow Cab Co.", "Checker Cab Co.", "Black & White Cab Co.", "Ute Cab Co."]
        for Name in self.Cabcompanynames:
            self.Cabcompanies[Name] = [300, 35, 75, 150, 300, 'CC']
        
        # Monorailelements have the form 
        # {Name : [Price, Rent, 2 MR owned, 3 MR owned, 4 MR owned, Property-type]}
        self.Monorails = {}
        self.Monorailnames = ["Red Monorail", "Yellow Monorail", "Green Monorail", "Blue Monorail"]
        for Name in self.Monorailnames:
            self.Monorails[Name] = [600, 75, 150, 300, 600, 'MR']
        
        # Cellblockelements have the form
        # {Name : [Price, Rent, 2 CB owned, 3 CB owned, 4 CB owned, Property-type]}
        self.Cellblocks = {}
        self.Cellblocknames = ["Cell Block A", "Cell Block B", "Cell Block C", "Cell Block D"]
        for Name in self.Cellblocknames: 
            self.Cellblocks[Name] = [250, 125, 250, 500, 1000, 'CB']
        
        # Utilityelements have the form 
        # {Name : [Price, Multipliers per amount of utilities owned, Property-type]}
        self.Utilities = {}
        self.Utilitynames = ["Alarm Company", "Postal Service", "Water Works", "Cable Company", "Electric Company", "Internet Service Provider", "Gas Company", "Trash Collector", "Telephone Company", "Sewage System", "Recycling Center", "Satellite Television Provider", "Compost Center", "Cell Phone Company"]
        for Name in self.Utilitynames: 
            self.Utilities[Name] = [150, 4, 10, 20, 30, 40, 60, 80, 100, 150, 200, 250, 300, 400, 500, 'U']
        
        # Stockelements have the form
        # {Name : [ Par Value, Dividents per amount of shares, Property-type]}
        self.Stocks = {"Motion Pictures" : [100, 10, 40, 90, 160, 250, 'S'], "Allied Steamships" : [110, 44, 99, 176, 275, 'S'], "National Utilities" : [120, 12, 48, 108, 192, 300, "S"], "General Radio" : [130, 13, 52, 117, 208, 325, 'S'], "United Railways" : [140, 14, 56, 126, 224, 350, 'S'], "American Motors" : [150, 15, 60, 135, 240, 375, 'S']}
        
        #Merging all properties in one dictionary
        self.allproperties = dict()
        self.dictionaries = [self.Airports, self.Cabcompanies, self.Cellblocks, self.Harbors, self.Monorails, self.Railroads, self.Titledeeds, self.Stocks, self.Utilities]
        for dictionary in self.dictionaries: 
            self.allproperties.update(dictionary)