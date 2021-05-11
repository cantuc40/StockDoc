#!/usr/bin/env python
# coding: utf-8


# File name: Invest capital
#Author: Carlos Huerta-Enciso

# Purpose: The user has the option to add funds into a Stock Doc! virtual wallet
# via a debit/credit card. 
# the funds can be used to buy or sell shares and/or crpytocurrency 
answer = ""
while (answer!="YES" and answer!="NO"):
  answer = input("Do you want to add funds to your wallet? (Yes or No)").upper()
if answer == "YES":
  print("Success! You now have:$ ")
elif answer == "NO":
    print("Transaction cancelled.")



amount = 100 #Example amount
thousands_separator = "."
fractional_separator = ","

#Set currency to American, and have it in two decimal places.
currency = "${:,.2f}".format(amount) 
print(currency)

