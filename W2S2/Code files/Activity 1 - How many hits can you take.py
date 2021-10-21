#!/usr/bin/env python
# coding: utf-8

# # Activity 1 - How many hits can you take

# ### Tasks
# 
# Your main character currently has a number of lifepoints, defined with the variable *lifepoints_number*.
# 
# Your mentor in the game gives you the following challenge: he will hit you, for a given number of times $ n $.
# - The first hit will make you lose one lifepoint,
# - the second, two lifepoints,
# - the third, three lifepoints,
# - and so on.
# - If you take too many hits and your lifepoints fall below zero, you fail the challenge.
# - Assuming you survive after all $ n $ hits (i.e. your lifepoints are still strictly positive after all $ n $ hits), he will give you $ n^2 $ coins.
# 
# Write a function **maximal_coins_number()**, which
# - receives your current number of lifepoints, i.e. the variable *lifepoints_number*,
# - and returns the maximal number of coins you can hope to obtain from the challenge
# - as well the number of lifepoints that will be remaining after all $ n $ hits were delivered.

# ### Your code below!

# In[ ]:


def maximal_coins_number(lifepoints_number):
    number_of_coins = None
    remaining_lifepoints_number = None
    return number_of_coins, remaining_lifepoints_number


# ### Expected results
# 
# If your function has been correctly designed, the following test cases should work.

# In[ ]:


# If lifepoints are 1, you cannot take any hits, so 0 coins, and your lifetotal remain 1.
number_of_coins, remaining_lifepoints_number = maximal_coins_number(lifepoints_number = 1)
print(number_of_coins)
print(remaining_lifepoints_number)


# In[ ]:


# If lifepoints are 11, you can take 4 hits, so 16 coins, and your lifetotal remaining after all hits is 1.
number_of_coins, remaining_lifepoints_number = maximal_coins_number(lifepoints_number = 11)
print(number_of_coins)
print(remaining_lifepoints_number)


# In[ ]:


# If lifepoints are 1000, you can take 44 hits, so 1936 coins, and your lifetotal remaining after all hits is 10.
number_of_coins, remaining_lifepoints_number = maximal_coins_number(lifepoints_number = 1000)
print(number_of_coins)
print(remaining_lifepoints_number)


# In[ ]:





# In[ ]:




