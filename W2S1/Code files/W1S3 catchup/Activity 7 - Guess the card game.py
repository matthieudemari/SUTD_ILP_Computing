#!/usr/bin/env python
# coding: utf-8

# # Activity 7 - Guess the card game

# ### Problem statement
# 
# We can define any card in a deck, by using two integers.
# - The first integer **suit_integer** takes the following values: 1 (for hearts), 2 (for diamonds), 3 (for spades), 4 (for clubs).
# - The second integer **value_integer** takes the following values: 1 (for ace), 2 (for 2), 3 (for 3), ..., 10 (for 10), 11 (for jack), 12 (for queen), 13 (for king).
# 
# In this configuration, the **queen of hearts** is defined as the combination of two variables **suit_integer = 1 and value_integer = 12**.
# 
# 
# Let us consider two cards
# - The first card, defined with the variables **hidden_suit and hidden_value**, corresponds to the card that the user/player must guess. (This is something we would normally hide from the player, but let us pretend for now!)
# - The second card, defined with the variables **guessed_suit and guessed_value**, corresponds to the card guessed by the user, and these values must be acquired via input().

# ### Tasks
# 
# Write a function **guess_the_card()**, which
# 1. Receives hidden_suit, hidden_value as the function inputs/parameters.
# 2. Acquires guessed_suit, guessed_value from the user, using input() twice.
# 3. Prints the following statements with appropriate True/False boolean values printed in the blanks.
#     - "Your guess is the same as the hidden card: ______."
#     - "You have correctly guessed the hidden card value or the hidden card suit: ______."
#     - "The hidden card value is lower than the one you guessed: ______."

# ### Your code below!

# In[ ]:


# Write you function below!
def guess_the_card(hidden_suit, hidden_value):
    
    # Acquire user input
    guessed_suit = None
    guessed_value = None
    
    # Print (same card)
    print(None)
    
    # Print (same suit or value)
    print(None)
    
    # Print (lower value)
    print(None)


# In[ ]:


# Let's try it, to check if it works properly!
# (test cases not given, figure some test cases out!)
guess_the_card(hidden_suit = 1, hidden_value = 12)


# In[ ]:




