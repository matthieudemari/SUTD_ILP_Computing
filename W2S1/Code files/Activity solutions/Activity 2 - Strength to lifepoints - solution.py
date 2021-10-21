#!/usr/bin/env python
# coding: utf-8

# # Activity 2 - Strength to lifepoints - solution

# ### Tasks
# 
# In several games, the main character might have attributes such as strength points and lifepoints (or hitpoints, HP). In some games, the stronger the hero is, the more lifepoints it is going to get. In this exercise, we investigate how to convert strength points into lifepoints.
# 
# Write a function **strength_to_lifepoints()**, according to the following requirements.
# - This function receives a single parameter, *strength_points*, which corresponds to the number of strength points our main character has, and - for simplicity - will only take integer values.
# - This function returns a single output, *lifepoints*, which corresponds to the number of lifepoints our main character will have, based on its strength points.
# - Our main character has a base number of 50 lifepoints (that means it has 50 lifepoints, by default, if its strength is zero).
# - For each strength point, our hero will gain 10 extra lifepoints.
# - If the main character has at least 50 strength points, it gains a one-time bonus of 100 lifepoints, on top of the lifepoints it already has.
# - Finally, if the main character has at least 100 **strength** points, it gains another one-time bonus of 50% extra lifepoints, on top of all the lifepoints it already has.

# ### Your code below!

# In[6]:


def strength_to_lifepoints(strength_points):
    
    # Base lifepoints is 50
    if(strength_points <= 0):
        lifepoints = 50
    
    # For each strength point, add 10 lifepoints
    elif(strength_points > 0 and strength_points < 50)
        lifepoints = 50 + strength_points*10
    
    # If the strength is at least 50, add an extra 100 lifepoints
    elif(strength_points >= 50 and strength_points < 100):
        lifepoints = 50 + strength_points*10 + 100
        
    elif(strength_points >= 100):
        lifepoints = (50 + strength_points*10 + 100)*1.5
    
    # Do not forget to return!
    # It should not be indented (not part of the if blocks).
    return lifepoints


# In[6]:


def strength_to_lifepoints(strength_points):
    
    # Base lifepoints is 50
    lifepoints = 50
    
    # For each strength point, add 10 lifepoints
    lifepoints += strength_points*10
    
    # If the strength is at least 50, add an extra 100 lifepoints
    if(strength_points >= 50):
        lifepoints += 100
        # If on top of that it has at least 100 strength, add 25%
        # Note how we included the second if, inside the first one.
        # Why is that a good idea?
        if(strength_points >= 100):
            lifepoints *= 1.50
    
    # Do not foreget to return!
    # It should not be indented (not part of the if blocks).
    return lifepoints


# ### Expected results
# 
# If your function has been correctly designed, the following test cases should work.

# In[7]:


# This should print 300
print(strength_to_lifepoints(25))


# In[8]:


# This should print 750
print(strength_to_lifepoints(60))


# In[10]:


# This should print 1875 (it is okay if it has a float format)
print(strength_to_lifepoints(110))


# In[ ]:




