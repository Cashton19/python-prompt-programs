#!/usr/bin/env python
# coding: utf-8

# In[3]:


weath_cond = input("Enter weather conditions:").lower().strip()
print(f"Weather: {weath_cond.upper()}")
match weath_cond:
    case "":
        print("Error: Enter Something")
    case "sunny":
        print("Suggestion: Wear light clothing and sunglasses!")
    case "rainy":
        print("Suggestion: Take an umbrella and wear a raincoat!")
    case "snowy":
        print("Suggestion: Wear warm clothes and boots!")
    case "cloudy":
        print("Suggestion: A light jacket might be useful!")
    case "windy":
        print("Suggestion: Wear a windbreaker or jacket!")
    case _:
        print("Suggestion: Unknown weather conditions.")

