"""
File Name: watchlist
Author: Christian Cantu 
Purpose: portfolio allows the actor (or user) to view every stocks and cryptos that he/she is currently invested
in.
"""

#class portfolio
class portfolio:
    
    #portfolio constructor (create arrays for cryptos and stocks)
    def __init__(self, name):
        self.list_of_stocks_invested = []           #array for stocks being invested
        self.list_of_cryptos_invested = []          #array for cryptos being invested
        self.username = name                        #user name for actor
        
    #Displays all cryptos and stocks being invested    
    def view_watchlist(self):
        
        #display stocks being invested
        for i in range(len(self.list_of_stocks_invested)):
            print(self.list_of_stocks_invested[i], "\n")
        
        #display cryptos being invested    
        for i in range(len(self.list_of_cryptos_invested)):
            print(self.list_of_cryptos_invested[i])
    