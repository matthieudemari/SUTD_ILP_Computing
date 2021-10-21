#!/usr/bin/env python
# coding: utf-8

# # Activity 1 - Guess the number game - Solution

# ### Tasks
# 
# Let us consider two integers
# - The first one, **true_number**, corresponds to a number that the user/player should guess. This is something we would normally hide from the player, but let us pretend for now!
# - The second one, **guessed_number**, corresponds to the number guessed by the user, and is acquired via input().
# 
# Both numbers will take values between 0 and 9, for simplicity.
# 
# Write some code, so that Python acquires a number from the user using input, and prints the following statements with appropriate True/False boolean values printed in the blanks.
# - "You have guessed the true number: ______"
# - "The true number is higher than your guess:  ______"
# - "The true number is lower than your guess: ______"

# ### Your code below!

# In[1]:


# 1. Choose a number to guess (for instance, 6)
true_number = 6


# In[2]:


# 2. Ask for user to guesss the number
guessed_number = int(input("Type your guess (integer between 0 and 9): "))


# In[3]:


print(true_number, guessed_number)


# In[4]:


# 3. Check if the user guessed the right number
right_number_bool = (true_number == guessed_number)
print("You have guessed the true number:", right_number_bool)
print("You have guessed the true number: {}".format(right_number_bool))

# 4. Check if the user's guess guessed_number is striclty lower than the true_number
lower_number_bool = (true_number > guessed_number)
print("The true number is higher than your guess:", lower_number_bool)

# 5. Check if the user's guess guessed_number is striclty higher than the true_number
higher_number_bool = (true_number < guessed_number)
print("The true number is lower than your guess:", higher_number_bool)


# In[ ]:




