#!/usr/bin/env python
# coding: utf-8

# # Activity 2 - Guess the number game v2 - solution

# ### Tasks
# 
# Remember the guess the number game from earlier?
# 
# Back then, we had defined a function **guess_the_number()**, which
# - received a hidden number that the user had to guess (passed as input *hidden_number*),
# - asked the user to input a number, via the input() method and would store it in a variable *guessed_number*,
# - and based on the two numbers would display two messages, reading:
#     - "You have found the hidden number: True/False."
#     - "Your number in guessed_number is lower than the hidden number: True/False."
#     
# The function is given below, you can try it, to check it works just fine.

# In[3]:


def guess_the_number(hidden_number):
    
    # 1. Ask the user for a number
    guessed_number = int(input("Guess the number! (values in 1-9): "))
    
    # 2. Check if the user found the right number
    right_number_boolean = (guessed_number == hidden_number)
    
    # 3 Check if the user's number is lower than the hidden number
    lower_number_boolean = (guessed_number <= hidden_number)
    
    # 4. Display messages
    print("Your have found the right number: {}".format(right_number_boolean))
    print("Your number is lower than the hidden number: {}".format(lower_number_boolean))


# In[4]:


# Try it, to see that it works! The number to guess is 5!
guess_the_number(hidden_number = 5)


# Your task is to write a second version (v2!) of this **guess_the_number()** function, which will be called *guess_the_number_v2()*.
# 
# It will have the following additional features:
# - The game will keep on asking the user to input() values, until the right number is found.
# - It will display the message "Your have found the right number!", once the user has found the right number.
# - When that happens, the function also displays "It only took you ... tries!" with the blank filled with the number of time the user had to type a number via input() before finding the right one.
# - Once the number has been found, the function no longer asks the user for inputs and stops.
# - While the user has not found the right number, the game will display either "Your number is lower than the hidden number." (if the last number entered by the user is lower than the hidden number) or "Your number is higher than the hidden number." (if the last number entered by the user is higher than the hidden number).
# 
# You may reuse and modify the code given below!

# ### Your code below!

# In[7]:


def guess_the_number_v2(hidden_number):
    
    # At the beginning, the user has not found the number to guess.
    # Initialize right_number_boolean as False.
    right_number_boolean = False
    # Initialize the number of tries as 0
    number_of_tries = 0
    
    # While the right number has not been found...
    while(not right_number_boolean):
        # 1. Ask the user for a number
        guessed_number = int(input("Guess the number! (values in 1-9): "))
        
        # 2. Increase the number of tries by 1
        number_of_tries += 1
    
        # 3. Check if the user found the right number
        right_number_boolean = (guessed_number == hidden_number)
        
        # 4.a. If the user has found the right number...
        if(right_number_boolean):
            # Display a congratulations message
            print("Your have found the right number")
            # Print the number of tries
            print("It only took you {} tries!".format(number_of_tries))
        
        # 4.b. If the user did not find the right number...
        else:
            # Check if the user's number is lower than the hidden number
            lower_number_boolean = (guessed_number <= hidden_number)
            # If the number is lower, let the user know.
            if(lower_number_boolean):
                print("Your number is lower than the hidden number.")
            # Otherwise the number is higher, and we let the user know.
            else:
                print("Your number is higher than the hidden number.")


# In[9]:


def guess_the_number_v2bis(hidden_number):
    
    # At the beginning, the user has not found the number to guess.
    # Initialize the number of tries as 0
    number_of_tries = 0
    
    # While the right number has not been found...
    while(True):
        # 1. Ask the user for a number
        guessed_number = int(input("Guess the number! (values in 1-9): "))
        
        # 2. Increase the number of tries by 1
        number_of_tries += 1
    
        # 3. Check if the user found the right number
        right_number_boolean = (guessed_number == hidden_number)
        
        # 4.a. If the user has found the right number...
        if(right_number_boolean):
            # Display a congratulations message
            print("Your have found the right number")
            # Print the number of tries
            print("It only took you {} tries!".format(number_of_tries))
            # Break the while loop, to stop asking the user for inputs!
            break
        
        # 4.b. If the user did not find the right number...
        else:
            # Check if the user's number is lower than the hidden number
            lower_number_boolean = (guessed_number <= hidden_number)
            # If the number is lower, let the user know.
            if(lower_number_boolean):
                print("Your number is lower than the hidden number.")
            # Otherwise the number is higher, and we let the user know.
            else:
                print("Your number is higher than the hidden number.")


# ### Expected results
# 
# You will have to come up with your own ideas to test your v2 function works as intended!

# In[10]:


hidden_number = 5
guess_the_number_v2(hidden_number)


# ### Another design, with an infinite loop and a break

# In[12]:


def guess_the_number_v2bis(hidden_number):
    
    # At the beginning, the user has not found the number to guess.
    # Initialize the number of tries as 0
    number_of_tries = 0
    
    # While the right number has not been found...
    while(True):
        # 1. Ask the user for a number
        guessed_number = int(input("Guess the number! (values in 1-9): "))
        
        # 2. Increase the number of tries by 1
        number_of_tries += 1
    
        # 3. Check if the user found the right number
        right_number_boolean = (guessed_number == hidden_number)
        
        # 4.a. If the user has found the right number...
        if(right_number_boolean):
            # Display a congratulations message
            print("Your have found the right number")
            # Print the number of tries
            print("It only took you {} tries!".format(number_of_tries))
            # Break the while loop, to stop asking the user for inputs!
            break
        
        # 4.b. If the user did not find the right number...
        else:
            # Check if the user's number is lower than the hidden number
            lower_number_boolean = (guessed_number <= hidden_number)
            # If the number is lower, let the user know.
            if(lower_number_boolean):
                print("Your number is lower than the hidden number.")
            # Otherwise the number is higher, and we let the user know.
            else:
                print("Your number is higher than the hidden number.")


# ### It also works fine
# 
# But it uses an infinite loop, which is not recommended.

# In[13]:


hidden_number = 5
guess_the_number_v2bis(hidden_number)


# In[ ]:




