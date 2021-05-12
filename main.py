from list_of_stocks_and_cryptos import *
from user_profile import * 
from displays import *
import os

user1 = user_profile("Christian Cantu", "cantuc40", "1234 5")
stockbroker1 = stockbroker("stockbrokername")
mainframe = interface(total_stocks_in_market, total_cryptos_in_market)



#Uncomment the line of code below if your using windows
#clear = 'cls'
#Uncomment the line of code below if your using MacOS or Linux
clear = 'clear'







def main():

        
    os.system(clear) #clears screen
    program = 1
    while(program == 1):
        selection = 0
        mainframe.display()
        print("\n")
        print("1. Buy Stock")
        print("2. Buy Crypto")
        print("3. Watch Stock")
        print("4. Watch Crypto")
        print("5. Display Portfolio")
        print("6. Display Watchlist")
        print("7. Deposit Funds")
        selection = int(input("Select a number 1-7\n"))
       
        
       
        
       
        
        #User buys a Stock 
        if (selection == 1):
            os.system(clear) #clears screen
            found = False
            for i in range (len(total_stocks_in_market)):                   
                name = total_stocks_in_market[i].getName() 
                print(name)    
            stock_selection = str(input("Type the name of the Stock you would like to buy\n"))
            os.system(clear) #clears screen
            for i in range(len(total_stocks_in_market)):
                name = total_stocks_in_market[i].getName()
                if(name == stock_selection):
                    mainframe.display_stock(total_stocks_in_market[i], user1)
                if(found == True):
                    break
            os.system(clear) #clears screen
    



        #User buys a Crypto
        elif (selection == 2):
            os.system(clear) #clears screen
            found = False
            for i in range (len(total_cryptos_in_market)):
                name = total_cryptos_in_market[i].getName() 
                print(name)    
            crypto_selection = str(input("Type the name of the Cryptocurrency you would like to buy\n"))
            os.system(clear) #clears screen
            for i in range(len(total_cryptos_in_market)):
                name = total_cryptos_in_market[i].getName()
                if(name == crypto_selection):
                    mainframe.display_crypto(total_cryptos_in_market[i], user1)
                if(found == True):
                    break
            os.system(clear) #clears screen
            
        
        
        
        #User watches a Stock
        elif (selection == 3):
            os.system(clear) #clears screen
            found = False
            for i in range (len(total_stocks_in_market)):
                name = total_stocks_in_market[i].getName() 
                print(name)    
            stock_selection = str(input("Type the name of the Stock you would like to watch\n"))
            os.system(clear) #clears screen
            for i in range(len(total_stocks_in_market)):
                name = total_stocks_in_market[i].getName()
                if(name == stock_selection):
                    user1.watchlist.add_stock(total_stocks_in_market[i])
                if(found == True):
                    break
            os.system(clear) #clears screen
            
            
            
            
            
        #User watches a crypto
        elif (selection == 4):
            os.system(clear) #clears screen
            found = False
            for i in range (len(total_cryptos_in_market)):
                name = total_cryptos_in_market[i].getName() 
                print(name)    
            stock_selection = str(input("Type the name of the Crypto you would like to watch\n"))
            os.system(clear) #clears screen
            for i in range(len(total_cryptos_in_market)):
                name = total_cryptos_in_market[i].getName()
                if(name == stock_selection):
                    user1.watchlist.add_crypto(total_cryptos_in_market[i])
                if(found == True):
                    break
            os.system(clear) #clears screen
      
            
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        #Display portfolio
        elif (selection == 5):
            os.system(clear) #clears screen
            user1.portfolio.view_portfolio()
            os.system(clear) #clears screen
        
        #Display watchlist    
        elif (selection == 6):
            os.system(clear) #clears screen
            user1.watchlist.view_watchlist()
            os.system(clear) #clears screen
                
        elif (selection == 7):
            os.system(clear) #clears screen   
            funds = float(input("How much would you like to deposit?\n"))
            user1.wallet.deposit(funds)
            input("funds have been added to your wallet")
            os.system(clear) #clears screen
        


main()
