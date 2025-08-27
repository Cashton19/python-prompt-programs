#!/usr/bin/env python
# coding: utf-8

# In[5]:


from datetime import datetime
try:
    name = input("Enter your name:")
    birth_date = input("Enter your date of birth(dd/mm/yyyy):").strip().replace(" ","")
    dob = datetime.strptime(birth_date, "%d/%m/%Y")
    today = datetime.now()
    age = today.year - dob.year - ((today.month,today.date) < (dob.month,dob.date))
    print(f"Hey {name} you are {age} years old.")
except ValueError:
    print("Error: Enter valid date format")


# In[ ]:




