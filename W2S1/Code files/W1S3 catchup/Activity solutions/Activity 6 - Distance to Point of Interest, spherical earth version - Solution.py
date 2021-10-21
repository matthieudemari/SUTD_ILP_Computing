#!/usr/bin/env python
# coding: utf-8

# # Activity 6 - Distance to Point of Interest, spherical earth version - Solution

# ### Problem statement
# 
# As in activity 5, we will here compute the distance between the player's position and a point of interest (PoI) position.
# 
# ![distance_to_quest.jpg](attachment:distance_to_quest.jpg)
# 
# The difference here will consist of the map model: instead of assuming a flat map model, we will consider a spherical one.
# 
# If the map is spherical, then the location of an object (of either a player or a PoI), will be defined using a latitude coordinate and a longitude coordinate, as shown below.
# 
# ![main-qimg-bfeceeb3c25335e39db91a05a3c82897.png](attachment:main-qimg-bfeceeb3c25335e39db91a05a3c82897.png)
# 
# Let us assume that:
# - the user coordinates are **(l_p, L_p)**, with **l_p** the latitude coordinates of the player and **L_p** the longitude coordinates of the player;
# - the PoI coordinates are **(l_t, L_t)**, with **l_t** the latitude coordinates of the PoI and **L_t** the longitude coordinates of the PoI;
# 
# The distance *d*, in kilometers, between the player and the PoI is given by the following formula.
# 
# $$ d = 6371.01 \times arccos\left( sin(l_p) \times sin(l_t) + cos(l_p) \times cos(l_t) \times cos(L_t − L_p) \right) $$

# ### Tasks
# 
# Write a function **distance_to_poi()** which receives 4 input parameters (l_p, L_p, l_t, L_t) and returns the distance d, in meters, between the player's position (l_p, L_p) and the PoI position (l_t, L_t).
# 
# **Note:** You may find it useful to import a cos, sin and arccos function from the Numpy library.
# 
# **Important note:** l_p, L_p, l_t and L_t will be angles with values given in degrees, do not forget to convert them to radians, as in activity 3!
# 
# Also, we expect the distance to be rounded, with no decimals. This can be easily done with the Python round() function or even a conversion of your distance into integer type using int()!

# ### Your code below!

# In[1]:


# Importing a few things I need
from numpy import cos, sin, arccos, pi

# Define your function below!
def distance_to_poi(l_p, L_p, l_t, L_t):
    # Convert to radians
    l_p_as_rads = l_p*pi/180
    L_p_as_rads = L_p*pi/180
    l_t_as_rads = l_t*pi/180
    L_t_as_rads = L_t*pi/180
    
    # Compute distance using formula above
    d = 6371.01*arccos(sin(l_p_as_rads)*sin(l_t_as_rads)         + cos(l_p_as_rads)*cos(l_t_as_rads)*cos(L_t_as_rads - L_p_as_rads))
    
    # Rounding our result with int() and return
    #result = int(d)
    result = round(d)
    return result


# ### Expected solutions
# 
# If your function has been correctly designed, the following test cases should work.

# In[2]:


### Test cases!
# Test case 1: the distance between Paris (48.864716, 2.349014) and Singapore (1.290270, 103.851959)
# is 10736.655091969447 kilometers (rounded to 10736)
d1 = distance_to_poi(l_p = 48.864716, L_p = 2.349014, l_t = 1.290270, L_t = 103.851959)
print(d1)


# In[3]:


# Test case 2: the distance between Paris (48.864716, 2.349014) and Paris (48.864716, 2.349014) should be 0.
d2 = distance_to_poi(l_p = 48.864716, L_p = 2.349014, l_t = 48.864716, L_t = 2.349014)
print(d2)


# In[ ]:




