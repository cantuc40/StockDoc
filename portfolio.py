"""
File Name: watchlist
Author: Christian Cantu 
Purpose: portfolio allows the actor (or user) to view every stocks and cryptos that he/she is currently invested
in.
"""

#class portfolio
class portfolio:
    
    #portfolio constructor (create arrays for cryptos and stocks)
    def __init__(self):
        self.list_of_stocks_invested = []           #array for stocks being invested
        self.list_of_cryptos_invested = []          #array for cryptos being invested
        
    #Displays all cryptos and stocks being invested.   
    def view_portfolio(self):
        
        self.run_function = 1
        while(self.run_function == 1):
            
            #Display stocks invested
            print("Stocks")
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{'ticker': <15}{'name': <15}{'price': <15}{'company': <15}{'market high': <15}{'market low': <15}{'number invested': <15}")
            print("---------------------------------------------------------------------------------------------------------")
            for i in range (len(self.list_of_stocks_invested)):
                ticker = self.list_of_stocks_invested[i].getTicker()
                name = self.list_of_stocks_invested[i].getName()
                price = self.list_of_stocks_invested[i].getPrice()
                company = self.list_of_stocks_invested[i].get_companyName()
                market_high = self.list_of_stocks_invested[i].getMarket_high()
                market_low = self.list_of_stocks_invested[i].getMarket_low()
                number_invested = self.list_of_stocks_invested[i].get_numberInvested()
                print(f"{ticker: <15}{name: <15}{price: <15}{company: <15}{market_high: <15}{market_low: <15}{number_invested: <15}")
            print("\n\n")
            
            #Display Cryptos invested
            print("Cryptocurrencies")
            print("-----------------------------------------------------------------------------------------------")
            print(f"{'name': <40}{'price': <40}{'number_invested': <40}")
            print("-----------------------------------------------------------------------------------------------")
            for i in range (len(self.list_of_cryptos_invested)):
                name = self.list_of_cryptos_invested[i].getName()
                price = self.list_of_cryptos_invested[i].getPrice()
                number_invested = self.list_of_cryptos_invested[i].get_numberInvested()
                print(f"{name: <40}{price: <40}{number_invested: <40}")
            print("\n\n")
            self.run_function = int(input("Press 0 to return to the main market"))
            
            
            
            
        
    
    #User is now tracking stock after purchase
    def add_stock(self, Stock, number_invested):
        self.list_of_stocks_invested.append(Stock)
        Stock.set_numberInvested(number_invested)
        print("Stock invested")
    #User is now tracking crypto after purchase
    def add_crypto(self, Crypto, number_invested):
        self.list_of_cryptos_invested.append(Crypto)
        Crypto.set_numberInvested(number_invested)
        print("Crypto invested")
