#!/usr/bin/env python
# coding: utf-8

# # Activity 6 - Distance to Point of Interest, spherical earth version

# ### Problem statement
# 
# As in activity 5, we will compute the distance between the player's position and a point of interest (PoI) position, but the difference will consist of the map model.
# 
# Instead of assuming a flat map model, we will consider a spherical one.
# 
# If the map is spherical, then the location of an object (my it be a player or a PoI), will be define using a latitude coordinate and a longitude coordinate, as shown below.
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
# **Note:** You may find it useful to import *cos*, *sin* and *arccos* functions from the Numpy library.
# 
# **Important note:** l_p, L_p, l_t and L_t will be angles with values given in degrees, do not forget to convert them to radians, as in activity 3!
# 
# Also, we expect the distance to be rounded, with no decimals. This can be easily done with the Python **round()** function or even a conversion of your distance into integer type using int()!

# ### Your code below!

# In[14]:


# Import a few things if needed


# Define your function below!
def distance_to_poi(l_p, L_p, l_t, L_t):
    # Convert angles to radians
    None
    # Calculate the distance
    d = None
    return d


# ### Expected solutions
# 
# If your function has been correctly designed, the following test cases should work.

# In[ ]:


### Test cases!
# Test case 1: the distance between Paris (48.864716, 2.349014) and Singapore (1.290270, 103.851959)
# is 10736-7 kilometers, after rounding.
d1 = distance_to_poi(l_p = 48.864716, L_p = 2.349014, l_t = 1.290270, L_t = 103.851959)
print(d1)


# In[26]:


# Test case 2: the distance between Paris (48.864716, 2.349014) and Paris (48.864716, 2.349014) should be 0.
d2 = distance_to_poi(l_p = 48.864716, L_p = 2.349014, l_t = 48.864716, L_t = 2.349014)
print(d2)


# In[ ]:




