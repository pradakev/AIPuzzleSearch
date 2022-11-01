from puzzle import Puzzle
from AStar import AStar
import time
"""
SLIDING PUZZLES - 

This file is the MAIN DRIVER for the Puzzle Solver program.
Here, the user will choose to either create their own puzzle of 
custom dimensions, or a ready-made 3x3 puzzle of varying difficulty.
The puzzle is then solved by the algorithm of choice. 
"""

def main():
    # Ready-made puzzles, varying in difficulty from
    # 1 through 8.
    userGrid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    userGrid2 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    userGrid3 = [[1, 2, 3], [5, 0, 6], [4, 7, 8]]
    userGrid4 = [[1, 3, 6], [5, 0, 2], [4, 7, 8]]
    userGrid5 = [[1, 3, 6], [5, 0, 7], [4, 8, 2]]
    userGrid6 = [[1, 6, 7], [5, 0, 3], [4, 8, 2]]
    userGrid7 = [[7, 1, 2], [4, 8, 5], [6, 3, 0]]
    userGrid8 = [[0, 7, 2], [4, 6, 1], [3, 5, 8]]

    # Abstract puzzle I made
    userGrid = [[4, 1, 3], [7, 2, 6], [0, 5, 8]]

    """
    Interface for Puzzle Solver
    """
    print("Thanks for choosing to play the Sliding Puzzle Solver!")
    puzzleSelect = input("Select 1 to create your own puzzle, 2 "
                         "to choose a ready-made 8-puzzle! ")

    """
    Create your own puzzle
    """
    if puzzleSelect == "1":
        # Create an n x n puzzle
        n = int(input("Puzzles are N x N. Input your dimension: "))
        # Create a 2D Array Puzzle
        userGrid = [[0] * n for i in range(n)]
        print("Enter your puzzle, using a zero to represent the open tile."
              "Enter your numbers separated by a space.")

        # Initialize 2D Array
        for i in range(n):
            print("Input numbers for row", i + 1)
            # iRow = input of row
            iRow = input()
            iRow = iRow.split()
            if len(iRow) != n:
                print("Error. Incorrect amount of numbers")
                exit(0)

            # Right now, I have a list of characters which represent
            # numbers. I'm going to convert these char's to ints
            # using the map function cited below:

            # Use the map function to return a map object
            # (which is an iterator) of the results after applying the
            # given function to each item of a given iterable (list, tuple etc.)
            # geeksforgeeks.com/python-map-function()
            iRow = list(map(int, iRow))
            userGrid[i] = iRow

        # Create Puzzle Grid Object
        onePuzzle = Puzzle(n)
        onePuzzle.initUserGrid(userGrid)
        print("Here's the solution for this grid: ")
        onePuzzle.printSolution()

    # Choose a ready-made puzzle
    elif puzzleSelect == "2":
        # Default grids
        print("Default puzzles are 3x3.")
        difficultyPuzzle = int(input("Choose a difficulty from 1-8: "))
        onePuzzle = Puzzle(3)
        if difficultyPuzzle == 1:
            onePuzzle.initUserGrid(userGrid1)
        elif difficultyPuzzle == 2:
            onePuzzle.initUserGrid(userGrid2)
        elif difficultyPuzzle == 3:
            onePuzzle.initUserGrid(userGrid3)
        elif difficultyPuzzle == 4:
            onePuzzle.initUserGrid(userGrid4)
        elif difficultyPuzzle == 5:
            onePuzzle.initUserGrid(userGrid5)
        elif difficultyPuzzle == 6:
            onePuzzle.initUserGrid(userGrid6)
        elif difficultyPuzzle == 7:
            onePuzzle.initUserGrid(userGrid7)
        elif difficultyPuzzle == 8:
            onePuzzle.initUserGrid(userGrid8)
    else:
        print("Error.")
        exit(0)

    """
    Choose Puzzle Algorithm & Solve Puzzle
    """
    print("Puzzle has been successfully selected.")
    algorithm = int(input("Select Algorithm: (1) Uniform Cost Search, (2) "
                          "Misplaced Tile Heuristic, (3) Manhattan Distance "
                          "Heuristic: "))
    if algorithm == 1:
        start = time.time()
        generalSearch(onePuzzle, AStar("UCS").UniformCostSearch)
        print("%.2f seconds elapsed" % (time.time() - start))
    elif algorithm == 2:
        start = time.time()
        generalSearch(onePuzzle, AStar("MTH").AStarMTH)
        print("%.2f seconds elapsed" % (time.time() - start))
    elif algorithm == 3:
        start = time.time()
        generalSearch(onePuzzle, AStar("MDH").AStarMDH)
        print("%.2f seconds elapsed" % (time.time() - start))
    else:
        print("Error. Invalid Input!")
        exit(0)


"""
General Search Algorithm - 
Takes input of a problem, as well as the queueFunction
that will be used to solve it. In this case, problem
will be a Puzzle object, and queueFunction will be an
AStar object function.
"""


def generalSearch(problem, queueFunction):
    # Nodes = MakeQueue(MakeNode(problem.initialState))
    nodes = [problem.initialState()]
    # Visited list to keep track of nodes already explored
    visited = []
    # Traceback Data
    nodesExpanded = 0
    solutionDepth = 0
    maxQueueSize = 0

    while True:
        if not nodes:
            # Return Failure
            return False
        else:
            node = nodes.pop()
            print("The best state to expand - ")
            print("G(n) = ", node.depth)
            print("Misplaced Tile H(n) = ", node.misplacedTileH)
            print("Manhattan Distance H(n) = ", node.manhattanDistH)

            node.printGrid()
            visited.append(node)
        if node.goalState():
            print("Goal State!")
            solutionDepth = node.depth
            print("Solution depth was ", solutionDepth)
            print("Number of nodes expanded: ", nodesExpanded)
            print("Max queue size: ", maxQueueSize)
            return node
        else:
            # Work on expand ( different for each function)
            nodesExpanded += len(node.operators())
            nodes = queueFunction(nodes, node.operators(), visited)
            maxQueueSize = max(maxQueueSize, len(nodes))

main()
