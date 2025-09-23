#!/usr/bin/env python
# coding: utf-8

# In[223]:


try:
    print("=== Grade Calculator === ")
    print("Enter a score (0-100) to get your letter grade")
    user_in = int(input("Enter your score:"))
    assert 0 <= user_in <= 100 , "Score must be between 0 and 100"
    match user_in:
        case 90|91|92|93|94|95|96|97|98|99|100:
            print("A grade: Excellent work! Outstanding performance!")
        case user_in if user_in in range(80,90):
            print("B grade: Good job! Above average performance!")
        case user_in if 70 <= user_in < 80:
            print("C grade: Satisfactory. You’re doing okay!")
        case _:
            print("F grade: Needs improvement. Don't give up!")
except AssertionError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter a valid number ")

