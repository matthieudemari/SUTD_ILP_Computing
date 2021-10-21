#!/usr/bin/env python
# coding: utf-8

# # Activity 3 - What color is the square? - Solution

# ### Problem statement
# 
# We would like to write a program that will:
# - ask the user to input a row_number (between 1 and 8), as an integer *row_number*,
# - ask the user to input a column number (between 1 and 8), as an integer *column_number*,
# - display if the square in coordinate *(row_number, column_number)* is black.
# 
# More specifically, we expect the program to display the following message *\"The square at coordinates (..., ...) is black: ...\"*, with the blanks (...) filled accordingly with the coordinates typed by the user and a True/False boolean.
# 
# The grid with black and white squares is given below.
# 
# ![chess_board.jpg](attachment:chess_board.jpg)

# ### Tasks
# 
# We expect you to write three subfunctions:
# - one to get the *row_number* via input(),
# - one to get the *column_number* via input(),
# - one to check if the square is black and display the message accordingly.
# 
# Finally, all subfunctions should be assembled in a main() function.

# **Task:** Write a function **get_row_number()**, which asks the user to input a *row_number* as an integer between 1 and 8. This function takes no inputs and should return *row_number* as an int type variable.

# In[5]:


def get_row_number():
    row_number = int(input("Type a row number (integer value between 1 and 8): "))
    return row_number


# **Task:** Write a function **get_column_number()**, which asks the user to input a *column_number* as an integer between 1 and 8. This function takes no inputs and should return *column_number* as an int type variable.

# In[6]:


def get_column_number():
    column_number = int(input("Type a column number (integer value between 1 and 8): "))
    return column_number


# **Task:** Write a function **display_if_black_square()**, which displays the following message *\"The square at coordinates (..., ...) is black: ...\"*, with the blanks (...) filled accordingly with the coordinates typed by the user and a True/False boolean. It receives two inputs, *row_number* and *column_number*, and returns nothing.

# In[7]:


def display_if_black_square(row_number, column_number):
    is_black = (row_number + column_number) % 2 == 0
    print("The square at coordinates ({}, {}) is black: {}".format(row_number, column_number, is_black))


# **Task:** Assemble all subfunctions in a **main()** function!

# In[8]:


def main():
    # 1. Get row_number
    row_number = get_row_number()
    
    # 2. Get column_number
    column_number = get_column_number()
    
    # 3. Check square color and display!
    display_if_black_square(row_number, column_number)


# **Finally:** Execute your main to check if it works!

# In[9]:


main()


# ### Expected results
# 
# A few test cases for you to try:
# - The square at coordinates (4,5) is white.
# - The square at coordinates (2,2) is black.
# - The square at coordinates (4,6) is black.
# - The square at coordinates (3,5) is black.

# In[ ]:




