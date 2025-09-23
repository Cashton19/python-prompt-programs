#!/usr/bin/env python
# coding: utf-8

# In[20]:


print("=== Day of the Week Determiner === \nEnter a number (1-7) where 1=Monday, 7=Sunday")
try:
    user_in = int(input("Enter day number:"))
    if user_in not in range(1,8):
        print("Error: Please enter a number between 1 and 7")
    else:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday" , "Saturday", "Sunday"]
        day_name = days[user_in - 1]
        print(f"Day {user_in}: {day_name}")
        if day_name in days[:5]:
            print("Type: Weekday")
        else:
            print("Type: Weekend")
        match user_in:
            case 1:
                print('Mood: "Start of work week"')
            case 2:
                print('Mood: "Getting into the groove"')
            case 3:
                print('Mood: "Hump day - halfway there!"')
            case 4:
                print('Mood: "Almost weekend" ')
            case 5:
                print('Mood: "TGIF - Weekend loading..."')
            case 6:
                print('Mood: "Relax and enjoy!"')
            case _:
                print('Mood: "Rest day"')
        print("Recommendation: Focus and be productive!") if user_in <= 5 else print("Recommendation: Take time to relax and recharge!")
except ValueError:
    print("Error: Please enter a valid number")

