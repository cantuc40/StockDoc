""" 
File Name: list_of_stocks_and_cryptos 
Author: Christian Cantu  
Purpose: This file allows the user to initialize any number of stocks and cryptocurrencies without 
having to type in everything in the main function  
 
 
""" 
 
#Import classes from stock, cryptocurrency, portfolio, and watchlist files 
from stock import * 
from cryptocurrency import * 
from portfolio import * 
from watchlist import * 
from Recieve_Commission import *  
 
#initialize everything for the stock market 
total_stocks_in_market = [] 
total_cryptos_in_market = [] 
 
 
     
#Type here to initialize stocks.  
#Use the following template to initialize: stock_name = stock(ticker, name, price, company_name) 
AMC = stock("AMC", "AMC", 12.32, "AMC Corp") 
gamestop = stock("GME", "Gamestop", 342.32, "Gamestop Corp.") 
tesla = stock("TSLA", "Tesla", 500, "Tesla Corp.") 
 
 
 
 
     
     
#Type here to initialize cryptos.  
#Use the following template to initialize: crypto_name = cryptocurrency(name, price) 
dogecoin = cryptocurrency("Dogecoin", 0.01) 
bitcoin = cryptocurrency("Bitcoin", 59392.32) 
etherium = cryptocurrency("Etherium", 2943.43) 
bitcoin_cash = cryptocurrency("Bitcoin Cash", 420.69) 
     
 
#appending every stock/crypto in their appropriate array (Need a better way of appending without retyping the names of 
#of each array) 
total_stocks_in_market.append(AMC) 
total_stocks_in_market.append(gamestop) 
total_stocks_in_market.append(tesla) 
total_cryptos_in_market.append(dogecoin) 
total_cryptos_in_market.append(bitcoin) 
total_cryptos_in_market.append(etherium) 
total_cryptos_in_market.append(bitcoin_cash) 
 
 
