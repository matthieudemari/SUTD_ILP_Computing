from numpy.random import choice, seed
from dice import Dice
from hand import Hand

class Turn():
    
    def __init__(self):
        
        # Create a Hand object and assign it to an atribute hand.
        self.hand = Hand()
        
        # Create an attribute end_turn, set to False for now.
        self.end_turn = False
        
    
    def display_hand(self):
        print("Hand: ", self.hand.dice_values)
        
    
    def get_reroll_list(self):
        
        # Write a function, which asks the user for which dice it wants to reroll,
        # in the form of an input().
        # It produces a list dice_reroll_list as a result.
        # Input
        self.display_hand()
        message = "Write the dice indexes you wish to reroll, separate with commas."
        message += "\nFor instance 0, 1, 3.\n"
        message = "If you wish to stop and not reroll, enter nothing in this input.\n"
        user_input = input(message)
        if user_input == "":
            # If no input, return empty list.
            return []
        else:
            # Otherwise, separate entries with split and create list.
            user_input = user_input.split(",")
            dice_reroll_list = []
            for entry in user_input:
                dice_reroll_list.append(int(entry.strip()))
            return dice_reroll_list
        
        
    def go_for_reroll(self):
        
        # Ask user for reroll list, with the get_reroll_list method.
        dice_reroll_list = self.get_reroll_list()
        
        # If reroll list is empty, stop and set attribute end_turn to True.
        if dice_reroll_list == []:
            self.end_turn = True
        else:
            # Otherwise, reroll and then update the end_turn attribute by checking
            # if the user has exhausted all its attempts with the is_over method
            # from the Hand() object in the attribute.
            self.hand.reroll_list(dice_reroll_list)
            self.end_turn = self.hand.is_over()
            
            
    def get_score(self):
        # Reuse the get_score() method from the hand attribute
        # to get score at the end of turn
        self.display_hand()
        return self.hand.get_score()
    
    
    def play_turn(self):
        
        # While the user wants to play, keep on asking for rerolls
        while(not self.end_turn):
            self.go_for_reroll()
        
        # After we are done, get the score of the turn, display and return
        score = self.get_score()
        print("You scored {} points on this turn".format(score))
        return score