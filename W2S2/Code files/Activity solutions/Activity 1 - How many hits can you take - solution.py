#!/usr/bin/env python
# coding: utf-8

# # Activity 1- How many hits can you take - solution

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

# In[1]:


def maximal_coins_number(lifepoints_number):
    
    # Count the number of hits you can take before our lifepoints fall below zero.
    # To keep trakc of this number, create a variable counter and initialize it as zero.
    counter = 0
    
    # We will use a while loop to calculate the maximal number of hits we can take before
    # your lifepoints fall below zero
    while(lifepoints_number > 0):
        # Increase the number of hits taken by one
        counter += 1
        print("Counter (during loop): ", counter)
        # The n-th hit hits for n, remove the points from your current lifepoints
        lifepoints_number -= counter
        print("Lifepoints (during loop): ", lifepoints_number)
    
    # We exit the loop, when we get to the point we have taken one more hit than we could take.
    # Our lifepoints_number at this point is negative.
    print("Counter (after loop): ", counter)
    print("Lifepoints (after loop): ", lifepoints_number)
    
    # The maximal number of hits we can take without our lifepoints going below 0 is then counter - 1.
    maximal_number_of_hits = counter - 1
    print("Maximal number of hits: ", maximal_number_of_hits)
    # And the lifepoints we will get after taking maximal_number_of_hits is then our current lifepoints_number
    # which is negative, plus the damage value of the last hit, which is the current value of counter.
    lifepoints_number += counter
    print("Remaining lifepoints after max. number of hits: ", lifepoints_number)
    # The number of coins is then given by maximal_number_of_hits squared
    number_of_coins = maximal_number_of_hits*maximal_number_of_hits
    print("Number of coints: ", number_of_coins)
    
    # Finally, we return the variables we need
    return number_of_coins, lifepoints_number


# In[7]:


def maximal_coins_number(lifepoints_number):
    
    # Count the number of hits you can take before our lifepoints fall below zero.
    # To keep trakc of this number, create a variable counter and initialize it as zero.
    counter = 0
    
    # We will use a while loop to calculate the maximal number of hits we can take before
    # your lifepoints fall below zero
    while(lifepoints_number > 0):
        # Increase the number of hits taken by one
        counter += 1
        #print("Counter (during loop): ", counter)
        # The n-th hit hits for n, remove the points from your current lifepoints
        lifepoints_number -= counter
        #print("Lifepoints (during loop): ", lifepoints_number)
    
    # We exit the loop, when we get to the point we have taken one more hit than we could take.
    # Our lifepoints_number at this point is negative.
    #print("Counter (after loop): ", counter)
    #print("Lifepoints (after loop): ", lifepoints_number)
    
    # The maximal number of hits we can take without our lifepoints going below 0 is then counter - 1.
    maximal_number_of_hits = counter - 1
    #print("Maximal number of hits: ", maximal_number_of_hits)
    # And the lifepoints we will get after taking maximal_number_of_hits is then our current lifepoints_number
    # which is negative, plus the damage value of the last hit, which is the current value of counter.
    lifepoints_number += counter
    #print("Remaining lifepoints after max. number of hits: ", lifepoints_number)
    # The number of coins is then given by maximal_number_of_hits squared
    number_of_coins = maximal_number_of_hits*maximal_number_of_hits
    #print("Number of coints: ", number_of_coins)
    
    # Finally, we return the variables we need
    return number_of_coins, lifepoints_number


# In[7]:


def maximal_coins_number(lifepoints_number):
    
    # Initialize the counter to 0
    counter = 0
    
    while(lifepoints_number - (counter + 1)> 0):
        counter = counter + 1
        # counter += 1
        lifepoints_number = lifepoints_number - counter
        # lifepoints_number -= counter
        #print(counter, lifepoints_number)
    
    number_of_coins = counter*counter
    remaining_lifepoints_number = lifepoints_number
    return number_of_coins, remaining_lifepoints_number


# In[7]:


def maximal_coins_number(lifepoints_number):
    
    # Initialize the counter to 0
    counter = 0
    
    while(True):
        counter = counter + 1
        # counter += 1
        lifepoints_number = lifepoints_number - counter
        # lifepoints_number -= counter
        print(counter, lifepoints_number)
        if(lifepoints_number - (counter + 1) <= 0):
            break
    
    number_of_coins = counter*counter
    remaining_lifepoints_number = lifepoints_number
    return number_of_coins, remaining_lifepoints_number


# ### Expected results
# 
# If your function has been correctly designed, the following test cases should work.

# In[8]:


# If lifepoints are 1, you cannot take any hits, so 0 coins, and your lifetotal remain 1.
number_of_coins, lifepoints_number = maximal_coins_number(lifepoints_number = 1)
print(number_of_coins)
print(lifepoints_number)


# In[2]:


# If lifepoints are 11, you can take 4 hits, so 16 coins, and your lifetotal remaining after all hits is 1.
number_of_coins, lifepoints_number = maximal_coins_number(lifepoints_number = 11)
print(number_of_coins)
print(lifepoints_number)


# In[14]:


# If lifepoints are 1000, you can take 44 hits, so 1936 coins, and your lifetotal remaining after all hits is 10.
number_of_coins, lifepoints_number = maximal_coins_number(lifepoints_number = 1000)
print(number_of_coins)
print(lifepoints_number)


# In[ ]:




