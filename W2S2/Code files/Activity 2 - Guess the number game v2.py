#!/usr/bin/env python
# coding: utf-8

# # Activity 2 - Guess the number game v2

# ### Tasks
# 
# Remember the guess the number game from earlier?
# 
# Back then, we had defined a function **guess_the_number()**, which
# - received a hidden number that the user had to guess (passed as input *hidden_number*),
# - asked the user to input a number, via the input() method and would store it in a variable *guessed_number*,
# - and based on the two numbers would display two messages, reading:
#     - "You have found the hidden number: True/False."
#     - "Your number in guessed_number is lower than the hidden number: True/False."
#     
# The function is given below, you can try it, to check it works just fine.

# In[1]:


def guess_the_number(hidden_number):
    
    # 1. Ask the user for a number
    guessed_number = int(input("Guess the number! (values in 1-9): "))
    
    # 2. Check if the user found the right number
    right_number_boolean = (guessed_number == hidden_number)
    
    # 3 Check if the user's number is lower than the hidden number
    lower_number_boolean = (guessed_number <= hidden_number)
    
    # 4. Display messages
    print("Your have found the right number: {}".format(right_number_boolean))
    print("Your number is lower than the hidden number: {}".format(lower_number_boolean))


# In[4]:


# Try it, to see that it works! The number to guess is 5!
guess_the_number(hidden_number = 5)


# Your task is to write a second version (v2!) of this **guess_the_number()** function, which will be called *guess_the_number_v2()*.
# 
# It will have the following additional features:
# - The game will keep on asking the user to input() values, until the right number is found.
# - It will display the message "Your have found the right number!", once the user has found the right number.
# - When that happens, the function also displays "It only took you ... tries!" with the blank filled with the number of times the user had to type a number via input() before finding the right one.
# - Once the number has been found, the function no longer asks the user for inputs and stops.
# - While the user has not found the right number, the game will display either "Your number is lower than the hidden number." (if the last number entered by the user is lower than the hidden number) or "Your number is higher than the hidden number." (if the last number entered by the user is higher than the hidden number).
# 
# You may reuse and modify the code given below!

# ### Your code below!

# In[57]:


def guess_the_number_v2(hidden_number):
    
    # Modify the code below!
    # 1. Ask the user for a number
    guessed_number = int(input("Guess the number! (values in 1-9): "))
    
    # 2. Check if the user found the right number
    right_number_boolean = (guessed_number == hidden_number)
    
    # 3 Check if the user's number is lower than the hidden number
    lower_number_boolean = (guessed_number <= hidden_number)
    
    # 4. Display messages
    print("Your have found the right number: {}".format(right_number_boolean))
    print("Your number is lower than the hidden number: {}".format(lower_number_boolean))


# ### Expected results
# 
# You will have to come up with your own ideas to test your v2 function works as intended!

# In[67]:


hidden_number = 5
guess_the_number_v2(hidden_number)


# In[ ]:




