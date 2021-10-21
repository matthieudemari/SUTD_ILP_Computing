#!/usr/bin/env python
# coding: utf-8

# # Activity 3 - Race and class check

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

# In[ ]:


a_first_string = "Hello"
a_second_string = "Hello"
print(a_first_string == a_second_string)


# In[ ]:


a_third_string = "World"
print(a_first_string == a_third_string)


# In[ ]:


a_fourth_string = "hello"
print(a_first_string == a_fourth_string)


# ### Your code below!

# In[ ]:


def character_creation(user_race, user_class):
    
    # Your code!
    print(None)


# ### Expected results
# 
# If your function has been correctly designed, the following test cases should work.

# In[ ]:


# This should print "You cannot play a character that is both Dwarf and Mage.".
character_creation("Dwarf", "Mage")


# In[ ]:


# This should print "You cannot play a character that is both Dwarf and Priest.".
character_creation("Dwarf", "Priest")


# In[ ]:


# This should print "You cannot play a character that is both Elf and Warrior.".
character_creation("Elf", "Warrior")


# In[ ]:


# This should print "You cannot play a character that is both Elf and Necromancer.".
character_creation("Elf", "Necromancer")


# In[ ]:


# This should print "You cannot play a character that is both Orc and Warrior.".
character_creation("Orc", "Warrior")


# In[ ]:


# This should print "Your character is both Elf and Mage.".
character_creation("Elf", "Mage")


# In[ ]:


# This should print "Your character is both Human and Hunter.".
character_creation("Human", "Hunter")


# In[ ]:


# This should print "Your character is both Dwarf and Warrior.".
character_creation("Dwarf", "Warrior")


# In[ ]:





# In[ ]:




