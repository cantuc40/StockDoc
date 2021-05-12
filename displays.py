"""
File Name: wallet
Author: Christian Cantu 
Purpose: Displays all data for the stock market
in.
"""

#Import files
from stock import *
from cryptocurrency import *
from list_of_stocks_and_cryptos import *

class interface:
    
    def __init__(self, Stocks, Cryptos):
        self.total_stocks = Stocks
        self.total_cryptos = Cryptos

    #Prints out the main stock market
    def display(self):
        
        #Display Stock
        print("Stocks")
        print("---------------------------------------------------------------------------------------------------------")
        #print("f{'ticker': <40} {'name': <40} {'price': <40} {'company': <40} {'market low': <40} {'number invested': <40} {'total invested': <40}")
        print(f"{'ticker': <15}{'name': <15}{'price': <15}{'company': <15}{'market high': <15}{'market low': <15}{'number invested': <15}")
        print("---------------------------------------------------------------------------------------------------------")
        for i in range (len(self.total_stocks)):
            ticker = self.total_stocks[i].getTicker()
            name = self.total_stocks[i].getName()
            price = self.total_stocks[i].getPrice()
            company = self.total_stocks[i].get_companyName()
            market_high = self.total_stocks[i].getMarket_high()
            market_low = self.total_stocks[i].getMarket_low()
            number_invested = self.total_stocks[i].get_numberInvested()
            
            print(f"{ticker: <15}{name: <15}{price: <15}{company: <15}{market_high: <15}{market_low: <15}{number_invested: <15}")
        print("\n\n")

        #Display Cryptos
        print("Cryptocurrencies")
        print("-----------------------------------------------------------------------------------------------")
        #print("name \t\t\t\t", "price \t\t\t\t\t", "number invested \t\t")
        print(f"{'name': <40}{'price': <40}{'number_invested': <40}")
        print("-----------------------------------------------------------------------------------------------")
        for i in range (len(self.total_cryptos)):
            name = self.total_cryptos[i].getName()
            price = self.total_cryptos[i].getPrice()
            number_invested = self.total_cryptos[i].get_numberInvested()
            #print(name, "\t\t\t", price, "\t\t\t\t\t", number_invested)
            print(f"{name: <40}{price: <40}{number_invested: <40}")

        
    #Display individual stock information    
    def display_stock(self, Stock, user1):
        
        self.status = 1
        while (self.status == 1):
            
            #Get stock Info
            self.ticker = Stock.getTicker()
            self.name = Stock.getName()
            self.price = Stock.getPrice()
            self.company = Stock.get_companyName()
            self.market_high = Stock.getMarket_high()
            self.market_low = Stock.getMarket_low()
            self.number_invested = Stock.get_numberInvested()
            print("Ticker:" , self.ticker)
            print("Name:" , self.name)
            print("Price:" , self.price)
            print("Company Name:" , self.company)
            print("Market High:" , self.market_high)
            print("Market Low:" , self.market_low)
            print("Amount Invested:" , self.number_invested)
            
            #Ask user for amount
            self.input_amount = int(input("Enter the amount of stocks you would like to buy\n"))
            self.wallet = user1.wallet.getFunds()
            self.total = self.input_amount * self.price
            
            #calculate total
            print("Price : ", self.price)
            print("Current Wallet : ", self.wallet)
            print("Amount : ", self.input_amount)
            print("Total: ", self.total)
            
            #Confirm purchase
            confirm = int(input("Confirm purchase? Type 1 for yes, 0 for no"))
            if(confirm == 1):
                if (self.wallet >= self.total):
                    user1.wallet.deduct(self.total)
                    user1.portfolio.add_stock(Stock, self.input_amount)
                    print("Purchase Complete")
                else:
                    print("Insufficient funds")            
            self.status = int(input("Press 0 to exit the screen\n"))
        
    #Display individual crypto information    
    def display_crypto(self, Crypto, user1):
        self.status = 1
        while (self.status == 1):
            
            #Get Crypto Info
            self.name = Crypto.getName()
            self.price = Crypto.getPrice()
            self.number_invested = Crypto.get_numberInvested()
            print("Name:" , self.name)
            print("Price:" , self.price)
            print("Amount Invested:" , self.number_invested)
            
            #Ask user for amount
            self.input_amount = int(input("Enter the amount of cryptos you would like to buy\n"))
            self.wallet = user1.wallet.getFunds()
            self.total = self.input_amount * self.price
            
            #calculate total
            print("Price : ", self.price)
            print("Current Wallet : ", self.wallet)
            print("Amount : ", self.input_amount)
            print("Total: ", self.total)
            
            #Confirm purchase
            confirm = int(input("Confirm purchase? Type 1 for yes, 0 for no"))
            if(confirm == 1):
                if (self.wallet >= self.total):
                    user1.wallet.deduct(self.total)
                    user1.portfolio.add_crypto(Crypto, self.input_amount)
                    print("Purchase Complete")
                else:
                    print("Insufficient funds")
            self.status = int(input("Press 0 to exit the screen\n"))
        

        


    #Unused method
    #def display_portfolio(self, user):
     #   self.exit_portfolio = 0
      #  while (self.exit_portfolio == 0):
       #     for i in range (len(user.portfolio.list_of_stocks_invested)):
        #        print(user.portfolio.list_of_stocks_invested[i])
         #   self.wallet = user.wallet.getFunds()
          #  print("Current Wallet: ", self.wallet)
           # self.exit_portfolio = int(input("press 1 to exit portfolio"))
    
    #Unused method
    #def display_watchlist(self, user):
     #   self.exit_watchlist = 0
      #  while (self.exit_watchlist == 0):
       #     for i in range (len(user.watchlist.list_of_stocks_tracking)):
        #        print(user.watchlist.list_of_stocks_tracking[i])
         #   self.wallet = user.wallet.getFunds()
          #  print("Current Wallet: ", self.wallet)
           # self.exit_watchlist = int(input("press 1 to exit watchlist"))
       
      
        
