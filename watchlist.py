"""
File Name: watchlist
Author: Christian Cantu 
Purpose: watchlist allows the actor (or user) to view every stocks and cryptos that he/she is interested
in.
"""



#Finished

#watchlist class
class watchlist:
    
    #Watchlist constructor (create arrays for cryptos and stocks) 
    def __init__(self):
        self.list_of_stocks_tracking = []       #array for stocks being tracked
        self.list_of_cryptos_tracking = []      #array for cryptos being tracked

        
    #Displays all cryptos and stocks being watched 
    def view_watchlist(self):
        
        self.run_function = 1
        while(self.run_function == 1):
            
            #View Stocks
            print("Stocks")
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{'ticker': <15}{'name': <15}{'price': <15}{'company': <15}{'market high': <15}{'market low': <15}{'number invested': <15}")
            print("---------------------------------------------------------------------------------------------------------")
            for i in range (len(self.list_of_stocks_tracking)):
                ticker = self.list_of_stocks_tracking[i].getTicker()
                name = self.list_of_stocks_tracking[i].getName()
                price = self.list_of_stocks_tracking[i].getPrice()
                company = self.list_of_stocks_tracking[i].get_companyName()
                market_high = self.list_of_stocks_tracking[i].getMarket_high()
                market_low = self.list_of_stocks_tracking[i].getMarket_low()
                number_invested = self.list_of_stocks_tracking[i].get_numberInvested()
                print(f"{ticker: <15}{name: <15}{price: <15}{company: <15}{market_high: <15}{market_low: <15}{number_invested: <15}")
            print("\n\n")
            
            
            #View Cryptos
            print("Cryptocurrencies")
            print("-----------------------------------------------------------------------------------------------")
            print(f"{'name': <40}{'price': <40}{'number_invested': <40}")
            print("-----------------------------------------------------------------------------------------------")
            for i in range (len(self.list_of_cryptos_tracking)):
                name = self.list_of_cryptos_tracking[i].getName()
                price = self.list_of_cryptos_tracking[i].getPrice()
                number_invested = self.list_of_cryptos_tracking[i].get_numberInvested()
                print(f"{name: <40}{price: <40}{number_invested: <40}")
            print("\n\n")
            self.run_function = int(input("Press 0 to return to the main market"))
            
            
            
        
       
    
    #Add stock to watchlist
    def add_stock(self, Stock):
        self.list_of_stocks_tracking.append(Stock)
        print("Stock Added")
    
    #Add cryptocurrency to watchlist
    def add_crypto(self, Crypto):
        self.list_of_cryptos_tracking.append(Crypto)
        print("Crypto Added")
