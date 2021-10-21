#!/usr/bin/env python
# coding: utf-8

# # Activity 2 - Ballistics of an angry bird - Solution

# ### Problem statement
# 
# In the angry bird game, the player has to launch birds at structures from a slingshot. The player gets to decide on an **initial angle theta (in degrees)** and **an initial speed for the bird alpha (in $m/s$)**.
# 
# After releasing, the angry bird goes flying into a parabolic curve, as shown in the figure below.
# 
# ![0fc3279812ce5b77fd4bdb92a5d975cd.png](attachment:0fc3279812ce5b77fd4bdb92a5d975cd.png)
# 
# Using Physics, you can compute the **distance d**, in **meters**, at which the bird will land as
# 
# $$ d = \frac{\alpha^2 sin(2 \theta)}{g}, $$
# 
# with **g** the **acceleration due to gravity**, which we will here set to $ 9.8 m.s^{-2}$.

# ### Tasks
# 
# Write a function, **compute_landing_point()**, which receives the initial angle value *theta* and the initial speed value *alpha*, and returns the distance *d* at which the angry bird will be landing.
# 
# **Note:** if needed, you can import the *sin* function from the Numpy library.
# 
# **Important note:** the angles *theta* will be given in degrees, but most cosine functions in Python require the angle to be in radians. Remember to convert your angles from degrees to radians before using the cosine function! (the conversion ratio is $ 180° = \pi $)

# ### Your code below!

# In[1]:


# 1. If needed import a sine (sin) function from numpy
from numpy import sin, pi

# 2. Define your function compute_landing_point()
def compute_landing_point(theta, alpha):
    # Below, we define the gravity constant g to be 9.8
    g = 9.8
    
    # Now, define the distance d, as a fucntion of g, theta and alpha.
    # Do not forget to convert your angles in radians!
    theta_as_radians = theta*pi/180
    d = alpha**2*sin(2*theta*pi/180)/g
    return d


# ### Expected solutions
# 
# If your function has been correctly designed, the following test cases should work.

# In[2]:


### Some test cases!
# This should return 0
print(compute_landing_point(theta = 0, alpha = 100))


# In[3]:


# This should return 0
print(compute_landing_point(theta = 45, alpha = 0))


# In[4]:


# This should return 1020.408163265306
print(compute_landing_point(theta = 45, alpha = 100))


# In[5]:


# This should return 883.699391616774
print(compute_landing_point(theta = 60, alpha = 100))


# In[ ]:




