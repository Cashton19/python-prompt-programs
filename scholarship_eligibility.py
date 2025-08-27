#!/usr/bin/env python
# coding: utf-8

# In[21]:


try:
    GPA = round(float(input("Enter your GPA:")), 1) 
    assert GPA <= 4.0, "GPA can't be more than 4.0"
    assert 0 <= GPA, "GPA can't be negative"
    fam_income = float(input("Enter your family income:"))
    assert fam_income <= 99999999, "Income can't be this big" 
    assert fam_income >= 9999, "Income can't be this low"
    com_service = float(input("Enter number of hours served in community service:"))
    assert com_service <= 50, "Community services won't exceed 50hrs"
    if GPA >= 3.5:
        if fam_income <= 49999:
            if com_service >= 40:
                print("You are eligible.")
            else:
                print("You are not eligible due to less service hours")
        else:
            print(f"if {fam_income:,.2f}RS is your family income")
            print("You are not eligible due to high family income.")
    else:
        print("You are not eligible due to low GPA.")
except AssertionError as e:
    print("Error:", e)
except ValueError:
    print("Error: Enter valid input.")

