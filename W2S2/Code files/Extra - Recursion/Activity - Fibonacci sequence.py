#!/usr/bin/env python
# coding: utf-8

# # Activity 5 - Fibonacci sequence

# ### Problem statement
# 
# The Fibonacci sequence $ F $ is a mathematical curiosity.
# 
# ![Fibonacci-Sequence.jpg](attachment:Fibonacci-Sequence.jpg)
# 
# The **first** and **second elements** of the sequence are equal to 1, that is $ F(1) = 1 $ and $ F(2) = 1 $.
# 
# The $n$-th Fibonacci element, with $ n \geq 3 $, is defined as the **sum of its previous two elements**, that is $ \forall n \geq 3, F(n) = F(n-1) + F(n-2) $.

# ### Tasks
# 
# **Task 1:** Write a function **fibonacci_element_while()**, which:
# - receives a strictly positive integer *n*, as its sole parameter,
# - returns the value of the *n*-th Fibonacci element as its sole output value,
# - operates using a *while* loop.
#     
# **Task 2:** Also write a function **fibonacci_element_rec()** which:
# - receives a strictly positive integer *n*, as its sole parameter,
# - returns the value of the *n*-th Fibonacci element as its sole output value,
# - operates using *recursion*, and does not rely on a *for* loop.

# ### You code below!

# In[ ]:


def fibonacci_element_while(n):
    pass


# In[ ]:


def fibonacci_element_rec(n):
    pass


# ### Expected results

# In[ ]:


# This should print 1, because the first element of the Fibonacci sequence is 1 (while version).
print(fibonacci_element_while(1))


# In[ ]:


# This should print 1, because the first element of the Fibonacci sequence is 1 (recursion version).
print(fibonacci_element_rec(1))


# In[ ]:


# This should print 1, because the second element of the Fibonacci sequence is 1 (while version).
print(fibonacci_element_while(2))


# In[ ]:


# This should print 1, because the second element of the Fibonacci sequence is 1 (recursion version).
print(fibonacci_element_rec(2))


# In[ ]:


# This should print 3, because the fourth element of the Fibonacci sequence is 3 (while version).
print(fibonacci_element_while(4))


# In[ ]:


# This should print 3, because the fourth element of the Fibonacci sequence is 3 (for version).
print(fibonacci_element_rec(4))


# In[ ]:


# This should print 1, because the 12th element of the Fibonacci sequence is 144 (while version).
print(fibonacci_element_while(12))


# In[ ]:


# This should print 1, because the 12th element of the Fibonacci sequence is 144 (for version).
print(fibonacci_element_rec(12))


# In[ ]:




