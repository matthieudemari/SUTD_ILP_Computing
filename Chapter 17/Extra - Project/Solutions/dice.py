from numpy.random import choice, seed

class Dice():
    
    def __init__(self):
        # Create an attribute dice_value,
        # which will contain an integer between 1 and 6.
        # This will correspond to the face value,
        # obtained on the last roll of the dice.
        # At the beginning, initialize it as 1.
        self.dice_value = 1
        
        # Create an attribute dice_values,
        # which will contain a list will all the integers between 1 and 6.
        # This will correspond to the face values,
        # that the dice can take.
        self.dice_values = [i for i  in range(1, 7)]
        
        # Roll the dice for the first time, by calling the roll method!
        self.roll()
        
        
    def roll(self):
        # This method should change the attribute dice_value,
        # to a random value chosen among the integers in the
        # dice_values attribute.
        # You may use the choice function from numpy.random,
        # as demonstrated earlier.
        self.dice_value = choice(self.dice_values)
        
        
    def test_rolls(self, n):
        # This method expects an integer value n (strictly positive)
        # abd should return a list of the values taken by the dice
        # after n successive rolls.
        list_values = []
        for _ in range(n):
            self.roll()
            list_values.append(self.dice_value)
        return list_values
    
    
    def balance_test(self):
        # Roll 10000 times and get list of rolls.
        n = 10000
        list_values = self.test_rolls(n)
        
        # Calculate reference value
        reference = 1/6*100
        
        # Break down results into a dictionnary
        balance_results = {i:100*list_values.count(i)/n \
                           for i in self.dice_values}
        return reference, balance_results