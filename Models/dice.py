class Dice():
    def __init__(self):
        self.Regularediewhite = {1,2,3,4,5,6}
        self.Regularediegreen = {1,2,3,4,5,6}
        self.Regularedieblue = {1,2,3,4,5,6}
        self.Regularedieteal = {1,2,3,4,5,6}
        self.Speeddie = {1,2,3,'Mr. Monopoly', 'Mr. Monopoly', 'Bus'}
        self.Speedierdie = {4,5,6,'Mr. Monopoly', 'Mr. Monopoly', 'Bus'}
        self.Investmentdie_updown = {'Investment Up','Investment Up','Investment Up','Investment Up','Investment Down','Investment Down'}
        self.Investmentdie_amount = {100, 50,'15%','20%','30%','50%'}
        self.Schemedie = {'Pyramid', 'Dividends', 'Investment Down by 5%', 'Investment Up by 10%', 'Single Die', 'Mystery Card'}
        self.Mysterydie = {'Chance', 'Community Chest', 'Roll3!', 'Public Works','Travel Voucher', 'Global Event', 'Employee', 'Shady Business', 'Shenanigans', 'Wild'}
        self.Jaildie_Oddjob = {1,2,3,4,5, 'Odd Jobs card'}
        self.Jaildie_Inmate = {1,2,3,4,5, 'Inmate card'}
        self.dice = [self.Regularediewhite, self.Regularediewhite, self.Regularediegreen, self.Regularedieblue,self.Regularedieteal, self.Speeddie,self.Speedierdie,self.Investmentdie_updown,self.Investmentdie_amount,self.Schemedie, self.Mysterydie,self.Jaildie_Oddjob,self.Jaildie_Inmate]
    