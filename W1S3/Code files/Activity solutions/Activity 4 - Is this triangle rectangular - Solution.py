#!/usr/bin/env python
# coding: utf-8

# # Activity 4 - Is this triangle rectangular - Solution

# ### Problem statement
# 
# Consider a triangle with three sides, denoted **a**, **b** and **c**. For the sake of simplicity, we will assume that **c** is the largest distance among all three values.
# 
# As you know from mathematics, a triangle is rectangular if and only if, the Pythagorean property holds, that is
# 
# $$ a^2 + b^2 = c^2 $$

# ### Tasks
# 
# Write a function, is_triangle_rectangular(), which receives all three values a, b, c as inputs and returns a boolean set to True if the triangle is indeed rectangular and False otherwise.
# 
# If the values **(a,b,c)** passed are such that **c** is not the largest side, then the function should return False.

# ### Your code below!

# In[1]:


# Define your function is_triangle_rectangular() as described above.
def is_triangle_rectangular(a, b, c):
    return a**2 + b**2 == c**2


# ### Expected solutions
# 
# If your function has been correctly designed, the following test cases should work.

# In[2]:


### Some test cases
# This should return True
print(is_triangle_rectangular(a = 3, b = 4, c = 5))


# In[3]:


# This should return False
print(is_triangle_rectangular(a = 4, b = 4, c = 6))


# In[4]:


# This should return False
print(is_triangle_rectangular(a = 3, b = 5, c = 4))


# In[5]:


# This should return True
print(is_triangle_rectangular(a = 0, b = 0, c = 0))


# In[ ]:




