#!/usr/bin/env python
# coding: utf-8

# In[9]:


weath_cond = input("Enter the weather(sunny,rainy,snowy,cloudy,windy):").strip().upper()
if weath_cond == "":
    print("Type something....")
elif weath_cond.isalpha() == False:
    print("Enter Valid Input")
else:
    if weath_cond == "SUNNY":
        suggestion = "Wear light clothing and sunglasses!"
    elif weath_cond == "RAINY":
        suggestion = "Take an umbrella and wear a raincoat!"
    elif weath_cond == "SNOWY":
        suggestion = "Wear warm clothes and boots!"
    elif weath_cond == "CLOUDY":
        suggestion = "A light jacket might be useful!"
    elif weath_cond == "WINDY":
        suggestion = "Wear a windbreaker or jacket!"
    else:
        suggestion = "Unknown weather conditions."
    print(f"Weather: {weath_cond}\nSuggestion: {suggestion}")

