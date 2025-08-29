# This imports a graphical library called matplotlib
import numpy as np
from copy import deepcopy
from numpy import array as np_array
from matplotlib import pyplot as plt


"""
IMPORTANT README!

Hello this is Matt!
A quick word about this file...

Below is a complicated display_board() function.
You should not bother about the code, as it uses a library, called matplotlib, which
I have not introduced (and probably will not discuss during this Summer School!).

Just know that
- it is a nice library, which can be used to display figures!
- the display_board() function will display any tic-tac-toe board you give to it, as long as
it respects the right format (3x3 numpy array, [0, 1, 2] values for elements).

Do not bother trying to read or understand the code for now, it is
not necessary for the exercise!

Just know this function is available if you want to import it, and use it in your code! 
"""


"""
ADDITIONAL NOTE

It now contains both the check_valid_coordinates() function from activity 2
and the take_action() function from activity 3!

It also contains the function is_over(), which checks if the board admits a
winner and returns the index of the winning player if any (player 1 has circles, 2 has crosses).
If the board is full and it has no clear winners, it returns -1.
Otherwise it returns 0.
"""


def is_over(board):
    """
    This function receives a tic tac toe board and returns:
    - the value 1 if the circles have won,
    - the value 2 if the crosses have won,
    - the value 0 if there is no clear winner yet, and there are empty cells left in the board,
    - the value -1 if the board is full and there is no winner.
    """
    
    # Check first horizontal line
    if board[0, 0] == board[1, 0] and board[0, 0] == board[2, 0] and board[0, 0] in [1, 2]:
        return board[0, 0]
    
    # Check second horizontal line
    if board[0, 1] == board[1, 1] and board[0, 1] == board[2, 1] and board[0, 1] in [1, 2]:
        return board[0, 1]
    
    # Check third horizontal line
    if board[0, 2] == board[1, 2] and board[0, 2] == board[2, 2] and board[0, 2] in [1, 2]:
        return board[0, 2]
    
    # Check first vertical line
    if board[0, 0] == board[0, 1] and board[0, 0] == board[0, 2] and board[0, 0] in [1, 2]:
        return board[0, 0]
    
    # Check second vertical line
    if board[1, 0] == board[1, 1] and board[1, 0] == board[1, 2] and board[1, 0] in [1, 2]:
        return board[1, 0]
    
    # Check third vertical line
    if board[2, 0] == board[2, 1] and board[2, 0] == board[2, 2] and board[2, 0] in [1, 2]:
        return board[2, 0]
    
    # Check first diagonal line
    if board[0, 0] == board[1, 1] and board[1, 1] == board[2, 2] and board[1, 1] in [1, 2]:
        return board[1, 1]
    
    # Check second diagonal line
    if board[2, 0] == board[1, 1] and board[0, 2] == board[1, 1] and board[1, 1] in [1, 2]:
        return board[1, 1]
    
    # Check for full board with no winner
    if all([board[i,j] in [1,2] for i in [0,1,2] for j in [0,1,2]]):
        return -1
    
    # Otherwise
    return 0


def take_action(board, x_coord, y_coord, is_circle):
    """
    A possible solution for activity 3.
    """
    
    # 0. Initialize the new_board as a copy of the current one
    new_board = deepcopy(board)
    
    # 1. Display previous board
    print("Displaying previous board.")
    display_board(board)
    
    # 2. Check valid coordinates
    is_valid = check_valid_coordinates(board, x_coord, y_coord)
    
    if is_valid:
        # 3 Take action
        if is_circle:
            # - If circle's turn, add a cirle (1)
            new_board[x_coord, y_coord] = 1
        else:
            # - Otherwise, add a cross (2)
            new_board[x_coord, y_coord] = 2

        # 4. Display new board
        print("Displaying new board after action {}.".format([x_coord, y_coord]))
        display_board(new_board)
        
    # 5. Return new board
    return new_board


def check_valid_coordinates(board, x_coord, y_coord):
    """
    A possible solution for activity 2.
    """
    
    # 1. Check if coordinates are acceptable
    # - x_coord should have a 0, 1, or 2 value.
    bool1 = (x_coord in [0, 1, 2])
    # - y_coord should have a 0, 1, or 2 value.
    bool2 = (y_coord in [0, 1, 2])
    # If coordinates are within the board, check the board is empty
    if(bool1 and bool2):
        is_valid = (board[x_coord, y_coord] == 0)
    else:
        is_valid = False
    
    # 2. If invalid, let the user know
    if not is_valid:
        err_str = "Coordinates for given action are invalid!"
        err_str2 = "(You passed x_coord = {} and y_coord = {})".format(x_coord, y_coord)
        print(err_str + err_str2)
        
    return is_valid



def display_board(board):
    """
    Display a graphical tic tac toe board, for any given 3x3 numpy array board.
    If board is not a 3x3 numpy array, it will print an error message and not display anything.
    """
    
    # 1. Check for board type.
    correct_type = False
    try:
        bool1 = type(board).__module__ == np.__name__
        bool2 = (board.shape == (3,3))
        bool3 = all([board[i,j] in [0,1,2] for i in range(3) for j in range(3)])
        correct_type = all([bool1, bool2, bool3])
    except:
        correct_type = False
        
    # 2. If incorrect board, print error message.
    if not correct_type:
        err_str1 = "Error: incorrect board format detected. \n"
        err_str2 = "Your board should be 3x3 numpy array containing [0,1,2] values only."
        print(err_str1 + err_str2)
    
    # 3. Otherwise, display.
    else:
        # Initialize a figure
        plt.subplots(figsize = (5, 5))
        
        # Initialize coordinates placements
        placements = {(0,0): [0.5, 2.5], \
                      (0,1): [1.5, 2.5], \
                      (0,2): [2.5, 2.5], \
                      (1,0): [0.5, 1.5], \
                      (1,1): [1.5, 1.5], \
                      (1,2): [2.5, 1.5], \
                      (2,0): [0.5, 0.5], \
                      (2,1): [1.5, 0.5], \
                      (2,2): [2.5, 0.5]}
        
        # Initialize plot
        plt.plot()
        
        # Linewidth for plots
        lw = 6
        
        # Angles list for circle plots
        number_angles = 100
        angles_list = [i/(number_angles - 1)*2*np.pi for i in range(number_angles)]
        
        # Size factor for circles and crosses
        size_fac = 0.25
        
        # Plot separation bars
        plt.plot([1, 1], [0, 3], c = 'k', linewidth = lw)
        plt.plot([2, 2], [0, 3], c = 'k', linewidth = lw)
        plt.plot([0, 3], [1, 1], c = 'k', linewidth = lw)
        plt.plot([0, 3], [2, 2], c = 'k', linewidth = lw)
        
        # Browse through elements and plot accordingly
        for index1, line in enumerate(board):
            for index2, element in enumerate(line):
                # Tuple for placement
                tuple_placement = (index1, index2)
                place_coord = placements[tuple_placement]
                
                # Plot text coordinates
                plt.text(place_coord[0], place_coord[1] - 0.38, str([index1, index2]), \
                         ha = "center", va = "center")
                
                # Plot circles
                if element == 1:
                    x = [place_coord[0] + size_fac*np.cos(angle) for angle in angles_list]
                    y = [place_coord[1] + size_fac*np.sin(angle) for angle in angles_list]
                    plt.plot(x, y, c = 'r', linewidth = lw)
                # Plot crosses
                elif element == 2:
                    plt.plot([place_coord[0] - size_fac, place_coord[0] + size_fac], \
                             [place_coord[1] + size_fac, place_coord[1] - size_fac], \
                             c = 'b', linewidth = lw)
                    plt.plot([place_coord[0] + size_fac, place_coord[0] - size_fac], \
                             [place_coord[1] + size_fac, place_coord[1] - size_fac], \
                             c = 'b', linewidth = lw)
        
        # Remove x-axis and y-axis ticks
        plt.axis('off')
        
        # Show
        plt.show()

