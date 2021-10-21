#!/usr/bin/env python
# coding: utf-8

# # Activity 7 - Guess the card game - Solution

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

# ### You code below!

# In[6]:


# Write you function below!
def guess_the_card(hidden_suit, hidden_value):
    
    # Acquire user input
    guessed_suit = int(input("Type a suit integer for your guess: "))
    guessed_value = int(input("Type a value integer for your guess: "))
    
    # Print (same card)
    bool1 = guessed_suit == hidden_suit and guessed_value == hidden_value
    print("Your guess is the same as the hidden card: {}.".format(bool1))
    
    # Print (same suit or value)
    bool2 = guessed_suit == hidden_suit or guessed_value == hidden_value
    print("You have correctly guessed the hidden card value or the hidden card suit: {}.".format(bool2))
    
    # Print (lower value)
    bool3 = hidden_value < guessed_value
    print("The hidden card value is lower than the one you guessed: {}.".format(bool3))


# In[7]:


# Let's try it!
guess_the_card(hidden_suit = 1, hidden_value = 12)


# In[ ]:




