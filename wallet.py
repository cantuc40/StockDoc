"""
File Name: wallet
Author: Christian Cantu 
Purpose: Stores the users currency for purchasing stocks and cryptos
in.
"""

class wallet:
    
    def __init__(self):
        self.funds = 0
        
    def getFunds(self):
        return self.funds
        
    def deposit(self, amount_of_cash):
        self.funds += amount_of_cash
        
    def deduct(self, amount_of_money):
        self.funds -= amount_of_money
