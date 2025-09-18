#!/usr/bin/env python
# coding: utf-8

# In[5]:


while True:
    try:
        stat_code = int(input("Status Code:"))
        match stat_code:
            case 200:
                msg = "OK - Request successful"
            case 404:
                msg = "Not Found - Resource doesn't exist"
            case 403:
                msg = "Client Error (403)"
            case stat_code if 500 <= stat_code < 600:
                msg = f"Server Error ({stat_code})"
            case stat_code if 400 <= stat_code < 500:
                msg = f"Client Error ({stat_code})"
            case _:
                msg = f"Unknown status code: {stat_code}"
        print(f"Response: {msg}")
    except ValueError:
        print("Error: Invalid Input")
    restart = ""
    while restart not in ["Y","N"]:
        restart = input("Do you want to restart???(Y/N):").strip().upper()
        if restart == "":
            print("Error: Enter Something")
        elif restart not in ["Y", "N"]:
            print("Error: Enter only Y or N")
    if restart == "N":
        break

