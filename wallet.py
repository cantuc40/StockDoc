# -*- coding: utf-8 -*-


class wallet:
    
    def __init__(self):
        self.funds = 0
        
        
    def deposit(self, amount_of_cash):
        self.funds += amount_of_cash
        
    def deduct(self, amount_of_money):
        self.funds -= amount_of_money