#!/usr/bin/env python
# coding: utf-8

# # Activity 2 - Asking users for personal details - Solution

# ### Tasks
# 
# Write a Python script that explicitly asks the user for its name and its age.
# 
# Later on, the scripts should display a message, reading
# 
# Your name is ...... and your age is ...!, with blanks filled accordingly!

# ### You code below!

# In[ ]:


# 1. Ask user for his/her name
user_name = input("What is your name? ")

# 2. Ask user for his/her age
user_age = int(input("What is your age? "))

# 3. Create and format message to be displayed
message = "Your name is {}, and your age is {}.".format(user_name, user_age)
# mean_message = "Man, you're really old."

# 4. Print the message!
print(message)
# print(mean_message)


# In[ ]:




