#!/usr/bin/env python
# coding: utf-8

# In[8]:


while True:
    try:
        principal_amt = 0
        rateof_int = 0
        comp_freq = 0
        time_period = 0
        while principal_amt <= 0:
            principal_amt = float(input("Enter the principal amount:"))
            if principal_amt <= 0:
                print("Pricipal can't be less than or equal to Zero")

        while rateof_int <= 0:
            rateof_int = float(input("Enter the Rate of Interest:"))
            if rateof_int <= 0:
                print("Rate can't be less than or equal to Zero")
            rateof_int /= 100

        while comp_freq <= 0:
            comp_freq = int(input("Enter compounding frequency:"))
            if comp_freq <= 0:
                print("Compounding frequency can't be 0 or negative")

        while time_period <= 0:
            time_period = float(input("Enter time period:"))
            if time_period <= 0:
                print("Time period can't be 0 or negative")

        final_amt = principal_amt * pow((1 + (rateof_int / comp_freq)), (comp_freq * time_period))
        print(f"Final Amount is Rs.{final_amt:,.2f}")

    except ValueError:
        print("Error: Invalid input")
    restart = ""
    while restart not in ("Y", "N"):
        restart = input("Do you want to restart (Y/N)? ").strip().upper()
        if restart not in ("Y", "N"):
            print("Please enter Y or N only.")

    if restart == "N":
        print("Good Bye!")
        break

