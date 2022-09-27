#!/usr/bin/env python
# coding: utf-8

# # Activity 1+ - How many hits can you take (extra challenge) - solution

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

# ### Extra challenge requirements:
# - **No if/while:** you should not use an **if** or a **while** statement in your function *maximal_coins_number()*.
# 
# **Hint:** The following result may help... For any number $ n $, integer, strictly positive, we have:
# 
# $$ 1 + 2 + ... + n = \frac{n(n+1)}{2} $$

# ### The intuition
# 
# Let us denote the number of lifepoints as l.
# 
# Basically, we want to find the largest value of $ n $ such that:
# 
# $$ \frac{n(n+1)}{2} < l $$
# 
# Or in other words $ n $ such that:
# 
# $$ n^2 + n < 2l$$
# 
# This requires to solve a quadratic equation, which only admits one positive root, $ n_1 $, defined as:
# 
# $$ n_1 = \frac{-1 + \sqrt{1 + 8l}}{2} $$
# 
# And the floor-rounded value of $ n_1 $, which can be obtained by converting $ n_1 $ into an int(), will give the maximal number of hits you can take before your lifepoints falling below zero.
# 
# Once we have this quantity, the rest is easy!

# ### Your code below!

# In[1]:


def maximal_coins_number(lifepoints_number):
    #maximal_number_of_hits = int((-1 + ((1 + 8*lifepoints_number)**(0.5)))/2)
    maximal_number_of_hits = int((-1 + ((8*lifepoints_number)**(0.5)))/2)
    number_of_coins = maximal_number_of_hits*maximal_number_of_hits
    remaining_lifepoints_number = int(lifepoints_number - maximal_number_of_hits*(maximal_number_of_hits + 1)/2)
    return number_of_coins, remaining_lifepoints_number


# ### Expected results
# 
# If your function has been correctly designed, the following test cases should work.

# In[2]:


# If lifepoints are 1, you cannot take any hits, so 0 coins, and your lifetotal remain 1.
number_of_coins, remaining_lifepoints_number = maximal_coins_number(lifepoints_number = 1)
print(number_of_coins)
print(remaining_lifepoints_number)


# In[3]:


# If lifepoints are 11, you can take 4 hits, so 16 coins, and your lifetotal remaining after all hits is 1.
number_of_coins, remaining_lifepoints_number = maximal_coins_number(lifepoints_number = 11)
print(number_of_coins)
print(remaining_lifepoints_number)


# In[4]:


# If lifepoints are 1000, you can take 44 hits, so 1936 coins, and your lifetotal remaining after all hits is 10.
number_of_coins, remaining_lifepoints_number = maximal_coins_number(lifepoints_number = 1000)
print(number_of_coins)
print(remaining_lifepoints_number)


# In[ ]:




