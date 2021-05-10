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
        self.list_of_stocks_invested = []  #array for stocks invested
        self.list_cryptos_invested = []      #array for cryptos invseted     
        self.get_commission = commission        #commission amount
        self.stockbroker = name                 #user name for actor - broker 

# Shows the amount invested by the client
print ("The stocks the client ivested in: ")
    for i in range(len(self.list_of_stocks_invested)):
        print(self.list_of_stocks_invested[i], "\n")

#displays the crypto currency the cliented invested in
print ("The crypto currencies that the client invested in: ")
    for i in range(len(self.list_of_cryptos_ivested)):
        print(self.list_of_cryptos_invested[i], "\n")

# Calculates the commission from stocks and cryptos that client invested in
    def calculate_commission (self, stocks, cryptos): 
        self.commission_from_stocks = total_invested * commission_rate
        self.commission_from_cryptos = cryptos * comission_rate
        self.comission_total = commission_from_stocks + commission_from_cryptos 

print ("Your net commission amount : $", comission_total) #total commission recieved
    print ("Your comission is: ", #total)
