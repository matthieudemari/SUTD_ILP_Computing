#!/usr/bin/env python
# coding: utf-8

# # Activity 5 - Distance to Point of Interest, flat earth version - Solution

# ### Problem statement
# 
# In several video games, you can track the position of a point of interest and display the distance between the current player's position, defined as **(x_p, y_p)**; and the point of interest (PoI) located at the position **(x_t, y_t)**.
# 
# An example, is shown below, with multiple points of interests being tracked at a given time.
# 
# ![distance_to_quest.jpg](attachment:distance_to_quest.jpg)
# 
# In this activity, we will assume that the map, in which the player evolves, is flat. Given the current player's position **(x_p, y_p)** and the position of a given PoI **(x_t, y_t)**, the distance **d**, in meters, between the player and the PoI is:
# 
# $$ d = \sqrt{(x_p - x_t)^2 + (y_p - y_t)^2} $$

# ### Tasks
# 
# Write a function **distance_to_poi()** which receives 4 input parameters (x_p, y_p, x_t, y_t) and returns the distance d, in meters, between the player's position (x_p, y_p) and the PoI position (x_t, y_t).
# 
# **Note:** You may find it useful to import a *sqrt()* function from either the math or Numpy package. Or you can use the fact that $ \sqrt{x} = x^{0.5}$

# ### Your code below!

# In[1]:


# Define your function below!
def distance_to_poi(x_p, y_p, x_t, y_t):
    d = ((x_p - x_t)**2+(y_p - y_t)**2)**0.5
    print(d)
    return d


# In[2]:


# Define your function below! (Using sqrt from numpy)
from numpy import sqrt
def distance_to_poi(x_p, y_p, x_t, y_t):
    d = sqrt((x_p - x_t)**2+(y_p - y_t)**2)
    return d


# ### Expected solutions
# 
# If your function has been correctly designed, the following test cases should work.

# In[3]:


# Test cases!
# This should return 64.03124237432849
print(distance_to_poi(x_p = 0, y_p = 0, x_t = 40, y_t = 50))


# In[4]:


# This should return 0
print(distance_to_poi(x_p = 40, y_p = 50, x_t = 40, y_t = 50))


# In[5]:


# This should return 172.04650534085255
print(distance_to_poi(x_p = -100, y_p = -50, x_t = 40, y_t = 50))


# In[ ]:




