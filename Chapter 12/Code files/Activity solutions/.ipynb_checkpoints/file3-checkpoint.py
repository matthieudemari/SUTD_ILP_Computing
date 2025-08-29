# This imports a graphical library called matplotlib
import numpy as np
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

It now contains the check_valid_coordinates() function from activity 2 as well!
"""


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

