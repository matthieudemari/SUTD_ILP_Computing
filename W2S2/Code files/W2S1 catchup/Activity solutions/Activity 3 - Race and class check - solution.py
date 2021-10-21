#!/usr/bin/env python
# coding: utf-8

# # Activity 3 - Race and class check - solution

# ### Tasks
# 
# In several games, especially Role-Playing Games (RPGs), you may create your own character at the beginning of the game, by selecting attributes, such as a race (Human, Elf, Dwarf, etc.) and a class (Warrior, Mage, Priest, etc.).
# 
# ![wow_char.jpg](attachment:wow_char.jpg)

# Write a function **character_creation()**, according to the following requirements.
# - The function will receive two parameters: *user_race* (corresponding to the user's chosen race, as a string, e.g. "Human") and *user_class* (corresponding to the user's chosen class, as a string, e.g. "Warrior").
# - For simplicity, we consider that only three races are available: Human, Elf, and Dwarf.
# - For simplicity, we consider that only four classes are available: Warrior, Hunter, Mage and Priest.
# - Humans can play all classes.
# - Elves cannot be warriors.
# - Dwarves cannot be mages or priests.
# - The function should not return anything.
# - It should print "You cannot play a character that is ...{race} and ...{class}.", with blanks filled accordingly, if the combination of user_race and user_class is not acceptable.
# - Not acceptable here means that its race and/or class is not among the ones listed above, or the combination is not acceptable, as listed above.
# - Otherwise, it should print "Your character's race is ...{race} and your character's class is ...{class}.", with blanks filled accordingly.

# ### A note on the == operator for strings
# 
# You may use the boolean operator == on strings objects. It returns True if both strings are identical, and False otherwise. Do note, that it is case sensitive!

# In[1]:


a_first_string = "Hello"
a_second_string = "Hello"
print(a_first_string == a_second_string)


# In[2]:


a_third_string = "World"
print(a_first_string == a_third_string)


# In[3]:


a_fourth_string = "hello"
print(a_first_string == a_fourth_string)


# ### Your code below!

# In[4]:


# Option #1
def character_creation(user_race, user_class):
    
    # Check the user selected a valid race and class combination
    if(user_race == "Human"):
        if(user_class == "Warrior" or user_class == "Hunter" or user_class == "Mage" or user_class == "Priest"):
            valid_race_class_combination = True
        else:
            valid_race_class_combination = False
    elif(user_race == "Elf"):
        if(user_class == "Hunter" or user_class == "Mage" or user_class == "Priest"):
            valid_race_class_combination = True
        else:
            valid_race_class_combination = False
    elif(user_race == "Dwarf"):
        if(user_class == "Warrior" or user_class == "Hunter"):
            valid_race_class_combination = True
        else:
            valid_race_class_combination = False
    else:
        valid_race_class_combination = False
        
    # The value in the boolean valid_race_class_combination
    # will now be set to True, if it is a valid combination,
    # and False otherwise.
    # We can then print a message according to this boolean.
    if(valid_race_class_combination):
        print("Your character's race is {} and your character's class is {}.".format(user_race, user_class))
    else:
        print("You cannot play a character that is both {} and {}.".format(user_race, user_class))


# In[1]:


# Option #2
def character_creation(user_race, user_class):
    
    # Check the user selected a valid race and class combination
    if(user_race == "Human"):
        if(user_class == "Warrior" or user_class == "Hunter" or user_class == "Mage" or user_class == "Priest"):
            print("Your character's race is {} and your character's class is {}.".format(user_race, user_class))
        else:
            print("You cannot play a character that is both {} and {}.".format(user_race, user_class))
    elif(user_race == "Elf"):
        if(user_class == "Hunter" or user_class == "Mage" or user_class == "Priest"):
            print("Your character's race is {} and your character's class is {}.".format(user_race, user_class))
        else:
            print("You cannot play a character that is both {} and {}.".format(user_race, user_class))
    elif(user_race == "Dwarf"):
        if(user_class == "Warrior" or user_class == "Hunter"):
            print("Your character's race is {} and your character's class is {}.".format(user_race, user_class))
        else:
            print("You cannot play a character that is both {} and {}.".format(user_race, user_class))
    else:
        print("You cannot play a character that is both {} and {}.".format(user_race, user_class))


# In[5]:


# Option #3
def character_creation(user_race, user_class):
    
    # Check the user selected a valid race and class combination
    if(user_race == "Human"):
        valid_race_class_combination = user_class == "Warrior" or user_class == "Hunter"             or user_class == "Mage" or user_class == "Priest"
    elif(user_race == "Elf"):
        valid_race_class_combination = user_class == "Hunter" or user_class == "Mage" or user_class == "Priest"
    elif(user_race == "Dwarf"):
        valid_race_class_combination = user_class == "Warrior" or user_class == "Hunter"
    else:
        valid_race_class_combination = False
        
    # The value in the boolean valid_race_class_combination
    # will now be set to True, if it is a valid combination,
    # and False otherwise.
    # We can then print our message accordingly.
    if(valid_race_class_combination):
        print("Your character's race is {} and your character's class is {}.".format(user_race, user_class))
    else:
        print("You cannot play a character that is both {} and {}.".format(user_race, user_class))


# In[ ]:


# Option #4 (best one in my opinion)

def print_valid():
    print("Valid combination!")
    
def print_invalid():
    print("Invalid combination!")
    
def check_human(user_class):
    if user_class == "Warrior" or user_class == "Hunter" or user_class == "Mage" or user_class == "Priest":
        print_valid()
    else:
        print_invalid()
        
def check_elf(user_class):
    if user_class == "Hunter" or user_class == "Mage" or user_class == "Priest":
        print_valid()
    else:
        print_invalid()
        
def check_dwarf(user_class):
    if user_class == "Warrior" or user_class == "Hunter":
        print_valid()
    else:
        print_invalid()
        
def character_creation(user_race, user_class):
    if(user_race == "Human"):
        check_human(user_class)
    elif(user_race == "Elf"):
        check_elf(user_class)
    elif(user_race == "Dwarf"):
        check_dwarf(user_class)
    else:
        print_invalid()


# ### Expected results
# 
# If your function has been correctly designed, the following test cases should work.

# In[45]:


# This should print "You cannot play a character that is both Dwarf and Mage.".
character_creation("Dwarf", "Mage")


# In[46]:


# This should print "You cannot play a character that is both Dwarf and Priest.".
character_creation("Dwarf", "Priest")


# In[47]:


# This should print "You cannot play a character that is both Elf and Warrior.".
character_creation("Elf", "Warrior")


# In[48]:


# This should print "You cannot play a character that is both Elf and Necromancer.".
character_creation("Elf", "Necromancer")


# In[49]:


# This should print "You cannot play a character that is both Orc and Warrior.".
character_creation("Orc", "Warrior")


# In[50]:


# This should print "Your character is both Elf and Mage.".
character_creation("Elf", "Mage")


# In[51]:


# This should print "Your character is both Human and Hunter.".
character_creation("Human", "Hunter")


# In[52]:


# This should print "Your character is both Dwarf and Warrior.".
character_creation("Dwarf", "Warrior")


# In[ ]:




