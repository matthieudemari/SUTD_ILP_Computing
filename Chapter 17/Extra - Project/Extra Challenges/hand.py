from numpy.random import choice, seed
from dice import Dice

class Hand():
    
    def __init__(self):
        # Create an attribute number_dice,
        # corresponding to the number of dice that the hand contains.
        # In our case, taht will be 5.
        self.number_dice = 5
        
        # Create an attribute list_dice,
        # which contains self.number_dice Dice() objects.
        self.list_dice = [Dice() for _ in range(self.number_dice)]
        
        # Call the method get_rolls() to generate an attribute dice_values
        # which will consist of list of the values obtained after rolling all
        # the dice once.
        self.get_rolls()
        
        # Define an attribute maximal_rolls set to 3
        # And an attribute current_roll set to 1.
        self.maximal_rolls = 3
        self.current_roll = 1
        
    def get_rolls(self):
        # This method simply initializes/updates an attribute dice_values,
        # which contains the five dice_value attributes contained in 
        # each of the five Dice() objects in the list_dice attribute.
        self.dice_values = [dice.dice_value for dice in self.list_dice]
        
    
    def reroll_list(self, dice_reroll_list):
        # This method will reroll the dice objects in self.list_dice
        # For instance, if dice_reroll_list = [0, 2, 4], we will reroll the
        # first, third and fifth dice in the list_dice attribute.
        # The non-specified indexes will not be re-rolled.
        # It should also increment the current_roll attribute by 1.
        
        for i in dice_reroll_list:
            # Reroll dice with index i.
            # Do so for each index value in dice_list.
            self.list_dice[i].roll()
            
        # Update rolls values in dice_values by calling the get_rolls() method
        self.get_rolls()
        
        # Increment roll
        self.current_roll += 1
        
        
    def get_dict(self):
        # This method returns a dictionary whose keys will be the values of dices
        # seen in the dice_values attribute, and the matching values of the keys
        # will correspond to the number of times said value appears in dice_values.
        values_dict = {}
        for value in self.dice_values:
            if value in values_dict.keys():
                values_dict[value] += 1
            else:
                values_dict[value] = 1
        return values_dict
    
    
    def has_single_pair(self):
        # This method should return True if the values in the
        # dice_values attribute contains a single pair.
        # This means that it returns True if dice_values = [1, 1, 3, 4, 5]
        # And False, otherwise.
        # Note that we expect a False if dice_values = [1, 1, 2, 2, 4] or
        # [1, 1, 2, 2, 2] or [1, 1, 1, 2, 4] or [1, 2, 3, 4, 5].
        # It should also return te value of the pair in question.
        # In the case of [1, 1, 3, 4, 5], it should therefore return 1.
        # If the boolean from before is False, it returns None instead.
        values_dict = self.get_dict()
        number_of_pairs = 0
        number_of_triplets = 0
        for value, freq in values_dict.items():
            if freq == 2:
                number_of_pairs += 1
                pair_value = value
            if freq == 3:
                number_of_triplets += 1
        decision = number_of_pairs == 1 and number_of_triplets == 0
        pair_value = pair_value if decision else None 
        return decision, pair_value
    
    
    def has_two_pairs(self):
        # This method should return True if the values in the
        # dice_values attribute contains exactly two pairs.
        # This means that it returns True if dice_values = [1, 1, 3, 3, 5]
        # And False, otherwise.
        # Note that we expect a False if dice_values = [1, 1, 1, 1, 5] or
        # [1, 1, 2, 2, 2] or [1, 1, 1, 1, 1] or [1, 2, 3, 4, 5].
        # It should also return te values of the pairs in question in a list.
        # In the case of [1, 1, 3, 3, 5], it should therefore return [1, 3].
        # If the boolean from before is False, it returns None instead.
        values_dict = self.get_dict()
        number_of_pairs = 0
        pair_values = []
        for value, freq in values_dict.items():
            if freq == 2:
                number_of_pairs += 1
                pair_values.append(value)
        decision = number_of_pairs == 2
        pair_values = pair_values if decision else None
        return decision, pair_values
    
    def has_triplet(self):
        # This method should return True if the values in the
        # dice_values attribute contains exactly one triplet.
        # This means that it returns True if dice_values = [1, 1, 1, 3, 5]
        # And False, otherwise.
        # Note that we expect a False if dice_values = [1, 1, 1, 1, 5] or
        # [1, 1, 2, 2, 2] or [1, 1, 1, 1, 1] or [1, 2, 3, 4, 5].
        values_dict = self.get_dict()
        number_of_pairs = 0
        number_of_triplets = 0
        for value, freq in values_dict.items():
            if freq == 2:
                number_of_pairs += 1
            if freq == 3:
                number_of_triplets += 1
                triplet_value = value
        decision = number_of_pairs == 0 and number_of_triplets == 1
        return decision
    
    
    def has_quadruplet(self):
        # This method should return True if the values in the
        # dice_values attribute contains exactly one quadruplet.
        # This means that it returns True if dice_values = [1, 1, 1, 1, 5]
        # And False, otherwise.
        # Note that we expect a False if dice_values = [1, 1, 1, 1, 1] or
        # [1, 2, 3, 4, 5].
        values_dict = self.get_dict()
        number_of_quadruplets = 0
        for value, freq in values_dict.items():
            if freq == 4:
                number_of_quadruplets += 1
        decision = number_of_quadruplets == 1
        return decision
    
    
    def has_yahtzee(self):
        # This method should return True if the values in the
        # dice_values all have identical values
        # This means that it returns True if dice_values = [1, 1, 1, 1, 1]
        # And False, otherwise.
        values_dict = self.get_dict()
        number_of_yahtzee = 0
        for value, freq in values_dict.items():
            if freq == 5:
                number_of_yahtzee += 1
        decision = number_of_yahtzee == 1
        return decision
    
    def has_full(self):
        # This method should return True if the values in the
        # dice_values attribute contains exactly a full house.
        # That is, exactly one triplet and one pair
        # This means that it returns True if dice_values = [1, 1, 1, 3, 3]
        # And False, otherwise.
        # Note that we expect a False if dice_values = [1, 1, 1, 1, 5]
        # or [1, 1, 1, 1, 1] or [1, 2, 3, 4, 5].
        values_dict = self.get_dict()
        number_of_pairs = 0
        number_of_triplets = 0
        for value, freq in values_dict.items():
            if freq == 2:
                number_of_pairs += 1
            if freq == 3:
                number_of_triplets += 1
        decision = number_of_pairs == 1 and number_of_triplets == 1
        return decision
    
    def has_straight(self):
        # This method should return True if the values in the
        # dice_values attribute contains exactly a straight.
        # That is [1, 2, 3, 4, 5] or [2, 3, 4, 5, 6].
        # It returns False otherwise.
        # Note that the dice list might not be ordered.
        values = list(sorted(self.dice_values))
        return values == [1, 2, 3, 4, 5] or values == [2, 3, 4, 5, 6]
    
    
    def get_score(self):
        
        # Define a list of possible scores.
        # We will append score calculations
        # based on whether or not combinations appear.
        # Later we will get the score for said hand,
        # by looking for the maximal value among valid combinations.
        possible_scores = []
        
        # Single pair
        decision, value = self.has_single_pair()
        if decision:
            possible_scores.append(2*value)
        
        # Two pairs
        decision, value = self.has_two_pairs()
        if decision:
            possible_scores.append(5 + 2*value[0] + 2*value[1])
        
        # Triplet
        decision = self.has_triplet()
        if decision:
            possible_scores.append(10 + sum(self.dice_values))
        
        # Quadruplet
        decision = self.has_quadruplet()
        if decision:
            possible_scores.append(40 + sum(self.dice_values))
        
        # Yahtzee
        decision = self.has_yahtzee()
        if decision:
            possible_scores.append(50 + sum(self.dice_values))
        
        # Full
        decision = self.has_full()
        if decision:
            possible_scores.append(30 + sum(self.dice_values))
        
        # Straight
        decision = self.has_straight()
        if decision:
            possible_scores.append(40)
        
        # Nothing
        possible_scores.append(0)
        
        # Find maximal score
        score = max(possible_scores)
        return score
    
    
    def is_over(self):
        # This method should return True if the current_roll
        # is equal to the maximal_rolls, indicating the user has used
        # all his/her chances of rerolling.
        # It returns False otherwise
        return self.current_roll == self.maximal_rolls 