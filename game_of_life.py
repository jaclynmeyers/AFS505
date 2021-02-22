""" python script that creates the game of life using - as dead cells and X as live cells

    module:: project01
    :platform: Mac, Unix, Windows
    :synopsis: This is the game of life simulation where cells are determined dead or alive
    based on the number of alive cells that neighbor them.
    module author: JACLYN MEYERS <jaclyn.j.meyers@gmail.com>
    """

from sys import argv

def print_grid(grid, nrows, ncol):
    """ This defines the function to print the grid that the game will run on.

    :param grid: This displays the matrix that the game of life simulation will run on.
    :type: A matrix of n rows and n columns.
    :param nrows: This defines the number of rows in the matrix.
    :type: An integer.
    :param ncol: This defines the number of columns in the matrix.
    :type: An integer.
    """

    # This allows it to go through every row i and column n to determine if the cell
    # grid[i][j]= 0 to be dead or alive
    for i in range(nrows):
        for j in range(ncol):

            # If the grid = 0 then the cell is dead
            if grid[i][j] == 0:
                print('-', end ='')
            else:
                print('X', end ='')
        print ("\n", end ='')
    print ("\n", end ='')


def create_grid(nrows, ncol):
    """ This function creates the crid that print_grid function will print out.
    :param nrows: This defines the number of rows in the matrix.
    :type: An integer.
    :param ncol: This defines the number of columns in the matrix.
    :type: An integer.
    """

    # This will create a blank grid that will then return the grid based on the nrows and ncols
    grid = []
    for i in range(nrows):
        grid.append([0]*ncol)
    return(grid)

def apply_rules(grid, nrows, ncol):
    """ This function establishes how to determine what a neighbor cell is.

    This will allow the game to know what a neighbor cell is considered. It will
    also apply the rules of the game to turn cells on and off based on their neighbors.

    :param grid: This displays the matrix that the game of life simulation will run on.
    :type: A matrix of n rows and n columns.
    :param nrows: This defines the number of rows in the matrix.
    :type: An integer.
    :param ncol: This defines the number of columns in the matrix.
    :type: An integer.
    """

    # The new grid will print with the rules applied without over writing the old new_grid.
    #This allows the game to work because the new grid is based off of the previous grid.
    new_grid = create_grid(nrows, ncol)

    # This allows us to define neighor cells based on their proximity.
    for i in range(nrows):
        for j in range(ncol):

            # West cell
            w = grid[i][j-1]
            # Nort West cell
            nw = grid[i-1][j-1]
            #North cell
            n = grid[i-1][j]

            #North East cell
            if j+1 >= ncol:
                ne = grid[i-1][0]
            else:
                ne = grid[i-1][j+1]

            # South West cell
            if i+1 >= nrows:
                sw = grid[0][j-1]
            else:
                sw = grid[i+1][j-1]

            # South cell
            if i+1 >= nrows:
                s = grid[0][j]
            else:
                s = grid[i+1][j]

            # East cell
            if j+1>= ncol:
                e = grid[i][0]
            else:
                e = grid[i][j+1]

            # South East cell
            if i+1 >= nrows and j+1>= ncol:
                se = grid[0][0]
            if i+1 >= nrows and j+1< ncol:
                se = grid[0][j+1]
            if i+1< nrows and j+1>= ncol:
                se = grid[i+1][0]
            if i+1< nrows and j+1< ncol:
                se = grid[i+1][j+1]

            # Neighbors is all the surrounding cells
            neighbors = nw + n + ne + w + sw + s + se + e

            # This will return the new grid with the new on/off cells that is
            #based off of the neighbors in the previous grid
            new_grid[i][j] = grid[i][j]
            if new_grid[i][j] == 1:

                #counts the cells around it to determine if it should be alive
                # or dead
                if neighbors < 2:
                    new_grid[i][j] = 0
                elif neighbors == 2 or neighbors == 3:
                    pass
                elif neighbors > 3:
                    new_grid[i][j] = 0
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

def main():
    """The function does all of the actions in the script.

    This function will act as the main function that the game will run through.
    It will have it itterate through all of the n_ticks given the certain start_cells
    in the command line. This uses the previous functions to complete the simulation.

    :param argv:  This function receives as input the argv object provided by
     the sys module which contains the list of command-line arguments.
    :type argv:  A list
    :param n_ticks: The first argument that is put in the command line for the number
    of times the simulation will run.
    :type: An integer
    :param start_cells: This is the second argument given on the command line that
    dictates which cells start as alive
    :type: A list
    """

    # command line arguments: n_ticks, start_cells(variable number of cells)
    # argv[1] for this simulation in 50
    n_ticks = argv[1]
    # The cells that start as alive are given in the command line as argv[2]
    start_cells = argv[2:]


    # This gives the dimensions of the grid and the new grid.
    # The grid will be a matrix of 30 rows and 80 columns.
    nrows = 30
    ncol = 80

    grid = create_grid(nrows, ncol)

    # This allows the start cells specified by the user in the command line to
    # correctly match the cells in the matrix
    # The matrix uses ordinal numbers so the first cell is cell 0
    for start_cell in start_cells:
        i, j = start_cell.split(':')
        i = int(i) -1
        j = int(j) -1
        grid[i][j] = 1

    # This allows the rules to iterate through the steps for n_ticks number of times
    for i in range(int(n_ticks)):
        print_grid(grid, nrows, ncol);
        # This will aplly the rules to the grid
        grid = apply_rules(grid, nrows, ncol)


if __name__ == "__main__":
    main()
