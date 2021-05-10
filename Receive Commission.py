""" 
Emre Yilmaz CS 3324 
Group 6 

Author Sebastian Maya
"""

from portfolio import* 
from stocks import* 
from cryptocurrency import* 

#Main class 
class stockbroker: 

    comission_rate = float (0.10) #The commission rate for using Stock Doc is 10%

# Creates a view of stocks and cryrpots from the perspective of the broker
    def user_profile (self, name): 
        self.show_list_of_stocks_invested = []
        self.display_cryptos_invested = []
        self.get_commission = commission
        self.stockbroker = name

# Calculates the commission from stocks and cryptos that client invested in
    def calculate_commission (self, stocks, cryptos): 
        self.commission_from_stocks = stocks * commission_rate
        self.commission_from_cryptos = cryptos * comission_rate

#Displays the comission based on the calculations
    def display_comission_from_stocks = stocks

    print ("Your comission is: ", #total)