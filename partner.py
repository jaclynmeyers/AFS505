"""
    Computational and Analytical Methods Class Project - Python Script for Game of Life
    Author: Kwabena (Kobby) Sarpong
    Programming language: Python 3
    Compatible OS: linux, windows
"""
# Importing required modules
from sys import argv
​
#Creating function that will display given number of rows and columns
def grid_creating(rows, columns):
    """
    This function creates grid given number of rows and columns
    rows (int): specifies number of rows
    columns (int): specifies number of columns
    """
    grid = [] #empty dictionary
    for i in range(rows):
        grid.append([0] * columns)
    return(grid)
​
​
​
​
# Creating a function to create the print grid for the game
def grid_printing(grid, rows, columns):
    """
    This function prints the grid for the game. 'x' represents cell is ON and '-' for OFF
    Parameters:
    grid: rows by columns matrix
    rows (int): specifies number of rows
    columns (int): specifies number of columns
    """
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 0:
                print('-', end = '')
            else:
                print('x', end = '')
        print("\n", end = '')
​
​
​
# Creating Function to Enforce the Rules of the Game
def game_rules(grid, rows, columns):
    '''
    This function is to help determine the neighbors of a cell, and also decide if a dead or alive (turned on or off).
    Parameters:
    grid: rows by columns matrix
    rows (int): specifies number of rows
    columns (int): specifies number of columns
    '''
    new_grid = grid_creating(rows, columns)
    #Defining cell neighbours
    for i in range(1, rows-1):
        for j in range(1, columns-1):
​
            # neighboring cells
            #northwest cell
            northwest = grid[i-1][j-1]
​
            # north cell
            north = grid[i-1][j]
​
            # northeast cell
            if columns == 80:
                northeast = grid[i-1][j]
            else:
                northeast = grid[i-1][j+1]
​
            # east cell
            if columns == 80:
                east = grid[i][j]
            else:
                east = grid[i][j+1]
​
            # southeast cell
            if columns >= 80:
                southeast = grid[i+1][j]
            else:
                southeast = grid[i+1][j+1]
            if rows >= 30:
                southeast = grid[i][j]
            else:
                southeast = grid[i+1][j+1]
​
            # south cell
            if rows >= 30:
                south = grid[i][j]
            else:
                south = grid[i+1][j]
​
            # southwest cell
            if rows >= 30:
                southwest = grid[i][j-1]
            else:
                southwest = grid[i+1][j-1]
​
            # west cell
            west = grid[i][j-1]
​
​
            total_neighbors = northwest + north + northeast + east + southeast + south + southwest + west
​
            # Specifying game rules
            if new_grid[i][j] == 1:
                if total_neighbors < 2:
                    new_grid[i][j] = 0
                elif (total_neighbors == 2) or (total_neighbors == 3):
                    pass
                elif total_neighbors > 3:
                    new_grid[i][j] = 0
            else:
                if total_neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid
​
# Creating function to put everything together and run the game.
def main ():
    """
    This functions puts everything together and run the game.
    """
    # unpacking variables using argument vector
    nTicks = argv[1]
    StartCells = argv[2:]
​
    # Specifying 2D grid
    rows = 30 #number of rows
    columns = 80 #number of columns
​
    grid = grid_creating(rows, columns)
​
​
    # set the starting cells specified by the user
    print(StartCells)
    i, j = StartCells[0].split(':')
    i = int(i)-1
    j = int(j)-1
    grid[i][j] = 1
​
    for i in range(int(nTicks)):
        grid_printing(grid, rows, columns)
        grid = game_rules(grid, rows, columns)
​
# calling function main
if __name__ == "__main__":
    main()
