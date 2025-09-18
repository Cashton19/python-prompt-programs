#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True:
    try:
        season = int(input("Enter Month (1-12):"))
        assert 1 <= season <= 12, "Enter the number ranging between 1-12 only"
        match season:
            case 12 | 1 | 2:
                print(f"Month {season} corresponds to: Winter")
            case 3 | 4 | 5:
                print(f"Month {season} corresponds to: Spring")
            case 6 | 7 | 8:
                print(f"Month {season} corresponds to: Summer")
            case _:
                print(f"Month {season} corresponds to: Fall")
    except AssertionError as e:
        print("Error:", e)
    except ValueError:
        print("Error: Invalid Input")
    restart = ""
    while restart not in ("Y" , "N"):
        restart = input("Do you want restart??(y/n):").strip().upper()
        if restart not in ["Y" , "N"]:
            print("Please enter only 'y' or 'n' ")
    if restart == "N":
        break

