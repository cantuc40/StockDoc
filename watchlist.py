"""
File Name: watchlist
Author: Christian Cantu 
Purpose: watchlist allows the actor (or user) to view every stocks and cryptos that he/she is interested
in.
"""

#watchlist class
class watchlist:
    
    #Watchlist constructor (create arrays for cryptos and stocks) 
    def __init__(self, name):
        self.list_of_stocks_tracking = []       #array for stocks being tracked
        self.list_of_cryptos_tracking = []      #array for cryptos being tracked
        self.username = name                    #user name for actor
        
    #Displays all cryptos and stocks being watched 
    def view_watchlist(self):
        
        #display stocks being tracked
        for i in range(len(self.list_of_stocks_tracking)):
            print(self.list_of_stocks_tracking[i], "\n")
        
        #display cryptos being tracked
        for i in range(len(self.list_of_cryptos_tracking)):
            print(self.list_of_cryptos_tracking[i])
            