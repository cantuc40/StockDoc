"""
File Name: stock.py
Author: Christian Cantu 
Purpose: This file contains the stock class along with it's attributes and methods.
It contains both accessors (functions that start with get) and mutators (functions that starts with set) 
"""

#stock class
class stock:
    #determines the total number of all cryptos in the whole program
    number_of_stocks = 0
    
    #Stock Constructor. All constructors have the self keyword, which determines the attributes
    def __init__(self, ticker, name, price, company_name):
        self.ticker = ticker                                #ticker name which appears on stock market (Ex. "GME")
        self.name = name                                    #name of stock
        self.price = price                                  #price of stock
        self.company_name = company_name                    #company who owns the stock
        self.price_changes = 0                              #difference of price minus previous price
        self.market_high = 0                                #the recorded high price of the stock for the day
        self.market_low = 0                                 #the recorded low price of the stock for the day
        self.number_invested = 0                            #how much user is invested
        self.total_invested = 0                             #the total amount of money invested (price * amount invested)
        stock.number_of_stocks += 1                         #increment the total number of stocks in the whole program by 1
        
    #return the name of the stock
    def getName(self):
        return self.name
    
    #return the ticker of the stock
    def getTicker(self):
        return self.ticker
    
    #return the price of the stock
    def getPrice(self):
        return self.price
    
    #return the market low price of the stock for today
    def getMarket_low(self):
        return self.market_low
    
    #return the market high price of the stock for today
    def getMarket_high(self):
        return self.market_high
    
    #return the changes between the current price and previous price of the stock
    def getPrice_Changes(self):
        return self.price_changes
    
    #return the number of stocks the user invested
    def get_numberInvested(self):
        return self.number_invested
    
    #return the company name who owns the stock
    def get_companyName(self):
        return self.company_name
    
    #change the name of the stock
    def setName(self, new_name):
        self.name = new_name
    
    #change the price of the stock and update total_invested
    def setPrice(self, new_price):
        self.price = new_price
        self.update_information()
        
    #Alter price changes of the stock
    def setPrice_Changes(self, new_price_change):
        self.price_changes = new_price_change
    
    #change the number of stocks invested and update total_invested
    def set_numberInvested(self, new_number_invested):
        self.number_invested = new_number_invested
        self.update_information()
    
    #total invested is updated
    def update_information(self):
        self.total_invested = self.price * self.number_invested
        
