from numpy.random import choice, seed
from dice import Dice
from hand import Hand
from turn import Turn

class Player():
    
    def __init__(self, max_turns):
        
        # Create an attribute current_turn, with value 0 for now
        self.current_turn = 0
        
        # Create an attribute max_turns, using the value passed to init
        self.max_turns = max_turns
        
        # Create an attribute list_scores, which starts as an empty list.
        self.list_scores = []
        
        # Create an attribute total_score, which starts as 0.
        self.total_score = 0
        
        # Create an attribute player_done, set to False for now.
        self.player_done = False
        
        
    def play_turns(self):
        
        #While the player is not done, keep on playing turns
        while(not self.player_done):
            # Increment turn counter in current_turn attribute
            self.current_turn += 1
            
            # Display separator for turns
            print("---------------------------------")
            print("TURN: ", self.current_turn)
            
            # Create a turn object
            turn = Turn()
            
            # Play the turn and get score at the end of the turn
            score = turn.play_turn()
            
            # Add score of turn to the list_scores for the player
            self.list_scores.append(score)
            
            # Check if player has completed all turns
            # and update player_done attribute
            self.player_done = self.current_turn == self.max_turns
            
        # After player is done sum score in list_scores
        # and update total_score attribute.
        self.total_score = sum(self.list_scores)
        
        # Final display
        print("---------------------------------\n")
        print("--- End of game ---")
        print("You scored {} points!".format(self.total_score))
        print("---------------------------------")