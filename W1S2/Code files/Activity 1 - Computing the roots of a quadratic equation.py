#!/usr/bin/env python
# coding: utf-8

# # Activity 1 - Computing the roots of a quadratic equation

# ### Problem statement
# 
# Consider the following quadratic equation
# 
# $$ a x^2 + b x + c = 0 $$
# 
# In this activity, the coefficients $ a $, $ b $, $ c $ will have the following values $ a = 2 $, $ b = -2 $ and $ c = -24 $.

# ### Tasks
# 
# 1. Assign the values of a, b, c to variables
# 
# 2. & 3. Compute the discriminant $ delta $ and print it on screen to check it is strictly positive.
# 
# 4. & 5. Compute the roots $ x1 $ and $ x2 $ and print them on screen.

# ### Reminder
# 
# As a reminder, the discriminant $ delta $ for a quadratic equation is defined as
# 
# $$ delta  = b^2 - 4 a c $$
# 
# **When the discriminant is strictly positive**, the roots $ x1 $ and $ x2 $ are defined as
# 
# $$ x1 = \frac{-b + \sqrt{delta}}{2 a} $$
# 
# $$ x2 = \frac{-b - \sqrt{delta}}{2 a} $$

# ### Expected solutions
# 
# You should compute and print a value of $ delta = 196 $.
# 
# The two roots you should compute and print will have the values $ x1 = 4.0 $ and $ x2 = -3.0 $.

# ### Note
# 
# The square root of a number $ x $ is strictly equivalent to the number $ x $ being exponentiated to $ 0.5 $

# In[9]:


x = 16
print(x**0.5)


# Equivalently, you can also import the sqrt (Square Root) function from numpy!

# In[ ]:


from numpy import sqrt
x = 16
print(sqrt(x))


# ### You code below!

# In[ ]:


# 1. Define the coefficients (a,b,c) of the quadratic equation
a = 
b = 
c = 

# 2. Compute the discriminant delta
delta = 

# 3.Print delta to check it is strictly positive
print()

# 4. Compute the two roots (x1, x2)
x1 = 
x2 = 

# 5. Print the value of the roots x1 and x2 you just calculated!
print()
print()


# In[ ]:




