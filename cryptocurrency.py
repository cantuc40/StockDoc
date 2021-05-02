"""
File Name: cryptocurrency.py
Author: Christian Cantu 
Purpose: This file contains the cryptocurrency class along with it's attributes and methods.
It contains both accessors (functions that start with get) and mutators (functions that starts with set) 
"""


#Cryptocurrency Class
class cryptocurrency:
    
    #determines the total number of all cryptos in the whole program
    number_of_cryptos = 0
    
    #Cryptocurrency Constructor. All constructors have the self keyword, which determines the attributes
    def __init__(self, name, price):
        self.name = name                        #name of crypto
        self.price = price                      #price of crypto
        self.price_changes = 0                  #difference of price minus previous price
        self.number_invested = 0                #how much user is invested 
        self.total_invested = 0                 #the total amount of money invested (price * amount invested)
        cryptocurrency.number_of_cryptos += 1   #increment the total number of cryptos in the whole program by 1 
        
    #return the name of the crypto
    def getName(self):
        return self.name
    
    #return the price of the crypto
    def getPrice(self):
        return self.price
    
    #return the number of cryptos invested
    def get_numberInvested(self):
        return self.number_invested
    
    #change the name of the crypto
    def setName(self, new_name):
        self.name = new_name
    
    #change the price of the crypto and update total_invested
    def setPrice(self, new_price):
        self.price = new_price
        update_information(self)
    
    #Alter price changes of the crypto    
    def setPrice_Changes(self, new_price_change):
        self.price_changes = new_price_change
    
    #change the number of cryptos invested and update total_invested
    def set_numberInvested(self, new_number_invested):
        self.number_invested = new_number_invested
        update_information(self)
    
    #total invested is updated
    def update_information(self):
        self.total_invested = self.price * self.number_invested