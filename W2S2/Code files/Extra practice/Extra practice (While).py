#!/usr/bin/env python
# coding: utf-8

# # 1. Approximate pi (while loop edition)
# 
# The value of pi, when calculated by a computer, is always approximated as
# 
# $$ \pi = 3 + \frac{4}{2 \times 3 \times 4} - \frac{4}{4 \times 5 \times 6} + \frac{4}{6 \times 7 \times 8} - \frac{4}{8 \times 9 \times 10} + ... $$
# 
# Notice how it alternates the plus and minus signs.
# 
# Write a function that receives an integer n and returns the approximated value of pi, with n terms computed in the sum above.
# 
# When $ n = 1 $, it returns $ 3 $. when $ n = 2 $, it returns the result of $ 3 + \frac{4}{2 \times 3 \times 4} $, etc.
# 
# It should use a while loop.

# In[ ]:





# ## 2. Approximate exponential
# 
# Following the same logic, write a function that receives an integer n and returns the approximate quantity of the function exp(x) by summing 
# 
# $$ exp(x) = 1 + \frac{x}{1} + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + ... + \frac{x^n}{n!} $$
# 
# Compare the performance of your function with the one from numpy!

# In[ ]:





# ## 3. More approximations?
# 
# Following the same logic you can look online for the summation formulas that can be used to approximate other functions such as cos, sin, log, etc.
# 
# Implementing those and comparing them with the numpy version is a good practice!

# In[ ]:




