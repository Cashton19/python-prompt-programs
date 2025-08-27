#!/usr/bin/env python
# coding: utf-8

# In[8]:


try:
    items = int(input("Enter number of items:"))
    assert items >= 0, "Items can't be negative"
    complete_dozens = items // 12
    remainder = items % 12
    print(f"Number of dozens: {complete_dozens}")
    print(f"Remaining items: {remainder}")
except AssertionError as e:
    print("Error:", e)
except ValueError:
    print("Error: Enter valid input.")


# In[ ]:




