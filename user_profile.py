"""
File Name: user_profile
Author: Christian Cantu 
Purpose: Stores the user information such as portfolio, wallet and watchlist
in.
"""

#import portfolio, watchlist, and wallet classes
from portfolio import *
from watchlist import *
from wallet import *

class user_profile:
    
    #Class constructor
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.portfolio = portfolio()
        self.watchlist = watchlist()
        self.wallet = wallet()
        
    # Return name    
    def getName(self):
        return self.name
    
    #return username
    def getUsername(self):
        return self.username
    
        
    
