# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:19:13 2021

@author: revan
"""

import pickle
import os
os.system('cls')



total_spend = pickle.load(open("spend_data.dat", "rb"))
Balance = pickle.load(open("balance_data.dat", "rb"))
expense = pickle.load(open("expense,dat", "rb"))

print("\n\n\n\n                          month expense                           ")

lenn = len(total_spend)

total_amt = pickle.load(open("budget.dat","rb"))


def intial_load_out(lenn, expense, total_spend, Balance):
    
    
    for _ in range(0,lenn):
        print()
        print("Expense = ", expense[_])
        print("total spend = ",total_spend[_])
        print("Balance = ",Balance[_])

intial_load_out(lenn, expense, total_spend, Balance)

total = 0

while(1):
    x = int(input("Expense = "))
    if x==0:
        break
    
    total = total +x
    total_amt = total_amt - x
    print ("total spend =",total)
    print("Balance = ",total_amt)
    total_spend.append(total)
    Balance.append(total_amt)
    


#name = pickle.load(open("names.dat","rb")
#pickle.dump(names, open("names.dat","wb"))
pickle.dump(expense, open("expense,dat", "wb"))
pickle.dump(total_spend, open("spend_data.dat", "wb"))
pickle.dump(Balance, open("balance_data.dat", "wb"))
    
    
    
    
