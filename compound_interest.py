#!/usr/bin/env python
# coding: utf-8

# In[4]:


try:
    principal_amt = float(input("Enter principle amount:"))
    annual_rate = float(input("Enter annual interest rate(%):")) / 100
    compound_freq = float(input("Enter the compounding frequency per year:"))
    numberof_years = float(input("Enter number of years:"))
    final_amt = principal_amt*((1+(annual_rate/compound_freq))**(numberof_years*compound_freq))
    print (f"Final amount: {final_amt:.2f} ")
    comp_int = final_amt - principal_amt
    print (f"Compound interest: {comp_int:.2f} ")
except ValueError:
    print("Error: enter appropriate values")

