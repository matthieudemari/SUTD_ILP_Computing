#!/usr/bin/env python
# coding: utf-8

# # Our second task
# 
# **Task:** compute the area of a circle with radius 10.

# In[1]:


# This seems to make sense, but it will fail executing.
radius = 10
area = radius*radius*pi
print(area)


# The computer does not know what is the value of **pi**.
# 
# We can retrieve it from the Numpy library, using the **from ... import ...** instruction, as shown below.

# In[2]:


from numpy import pi
print(pi)


# In[3]:


from numpy import sqrt
print(sqrt(16))


# Running the code we had defined earlier should now work and give us an approximated value of the area of a circle with radius 10.

# In[4]:


# Now it should work!
radius = 10
area = radius*radius*pi
print(area)


# In[ ]:




