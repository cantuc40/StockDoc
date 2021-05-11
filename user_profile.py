# -*- coding: utf-8 -*-




#import list_of_stocks_and_cryptos
from portfolio import *
from watchlist import *
from wallet import *

class user_profile:
    
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.portfolio = portfolio()
        self.watchlist = watchlist()
        self.wallet = wallet()
        
        
    def getName(self):
        return self.name
    
    def getUsername(self):
        return self.username
        
    
