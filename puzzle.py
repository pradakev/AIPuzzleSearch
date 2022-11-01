from copy import copy, deepcopy
class Puzzle:
    """
    PUZZLE -
    A class representing a 2D puzzle. This puzzle is made up of a 2D list.
    It contains object variables useful to solving the puzzle, such as
    the location of the zero, state depth, heuristic information, and
    creating the solution puzzle as well.
    """
    """
    Constructor that initializes an n x n puzzle
    within a 2D list.
    """

    def __init__(self, n):
        # Validating n dimension for Puzzle
        if n < 2:
            n = 2
        # N = Puzzle Dimension
        self.n = n
        # Puzzle grid itself
        self.grid = []
        # Create a standard grid of N dimensions
        self.createGrid()
        # Variable to store zero / blank's location
        self.zeroLocation = (n - 1, n - 1)
        # Puzzle of N dimension solved
        self.solutionGrid = []

        self.cost = 0
        self.depth = 0

        # Heuristic Information
        self.misplacedTileH = 0
        self.manhattanDistH = 0
        # A Dictionary used to map a value to where
        # it should be in a solved 2D list, with respect to
        # it's coordinates. EX) For key 1, value returned should be
        # i = 0, j = 0 (Value is a tuple of i, j )
        self.solutionDict = {}
        self.createSolution()

    """
    MISPLACED TILE HEURISTIC - 
    Function to calculate current state's heuristic value.
    Goes through puzzle and counts how many tiles are out of place.
    Then it records it within the misplacedTileH object variable.
    """

    def misplacedTileHeuristic(self):
        number = 1
        misplaces = 0
        # Don't do anything if ZERO is found
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] != 0:
                    if self.grid[i][j] != number:
                        misplaces += 1
                number += 1
        if self.grid[self.n - 1][self.n - 1] == 0:
            misplaces -= 1
        if misplaces == -1:
            misplaces = 0
        self.misplacedTileH = misplaces

    """
    MANHATTAN DISTANCE HEURISTIC - 
    Function to calculate current state's heuristic value.
    Goes through puzzle and checks which tiles are out of place.
    At each misplaced tile, it checks against the coordinates of 
    where that tile should be, subtracts the coordinate values, and
    that is the manhattan distance. It then sums all of the misplaced
    tiles together into object variable manhattanDistH.
    """

    def manhattanDHeuristic(self):
        self.manhattanDistH = 0
        for i in range(self.n):
            for j in range(self.n):
                # Get the current value at i, j
                gridVal = self.grid[i][j]
                # Get the solution value at i, j
                a, b = self.solutionDict[gridVal]
                # Get the abs difference between a, b and i, j
                # This will result in the misplaced tile distances
                rowDistance = abs(a - i)
                colDistance = abs(b - j)
                self.manhattanDistH += rowDistance + colDistance

    """
    EQUALS - 
    Overloaded operator defined when checking if a Puzzle exists
    within another structure. Specifically, used to make "in" work.
    EX) if puzzle1 in puzzleExpansions
    - in uses __eq__ to check if puzzle1 is inside puzzleExpansions
    """

    def __eq__(self, other):
        if self.grid == other.grid:
            return True
        else:
            return False

    """
    INITIAL STATE - 
    When the user inputs a user-created grid,
    this initializes it and returns the Puzzle object.
    Used in companion with the GeneralSearchAlgorithm.
    """

    def initialState(self):
        return self

    """
    FIND ZERO LOCATION - 
    Find Zero within grid. Returns a tuple with i, j.
    """

    def findZeroLocation(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    return i, j

    """
    INITIALIZE USER GRID - 
    This function takes in a 2D list of integers, and converts it
    into a Puzzle Object.
    """

    def initUserGrid(self, newGrid):
        self.grid = deepcopy(newGrid)
        self.n = len(newGrid)
        self.zeroLocation = self.findZeroLocation()
        self.createSolution()
        self.misplacedTileHeuristic()
        self.manhattanDHeuristic()

    """
    PRINT ZERO LOCATION -
    Print's zero's location, as a tuple.
    """

    def printZeroLocation(self):
        print(self.zeroLocation)

    """
    CREATE GRID -
    Creates the standard grid for the Puzzle.
    """

    def createGrid(self):
        self.grid = [[0] * self.n for i in range(self.n)]
        counter = 1
        for i in range(self.n):
            for j in range(self.n):
                self.grid[i][j] = counter
                counter += 1
        self.grid[self.n - 1][self.n - 1] = 0

    """
    CREATE SOLUTION - 
    Creates the solution grid for the puzzle.
    Also:
    I'll make a dictionary that will use the number
    as the key, and the coordinates as its value. This way,
    I can return coordinates where a number should be 
    for the Manhattan Distance Heuristic
    """

    def createSolution(self):
        self.solutionGrid = [[0] * self.n for i in range(self.n)]
        counter = 1
        for i in range(self.n):
            for j in range(self.n):
                self.solutionGrid[i][j] = counter
                counter += 1
        self.solutionGrid[self.n - 1][self.n - 1] = 0

        # Setup for MDH processing
        for i in range(self.n):
            for j in range(self.n):
                self.solutionDict[self.solutionGrid[i][j]] = (i, j)

    """
    STRING PRINT -
    Overloading the print() operator for Puzzle objects. Here, 
    a 2D list is printed and returned as a string. Useful for debugging.
    """

    def __str__(self):
        return str(self.grid)

    """
    PRINT GRID -
    Standard Puzzle printer without overloading print().
    """
    def printGrid(self):
        for row in self.grid:
            print(row)

    """
    PRINT SOLUTION - 
    Prints the solution grid.
    """
    def printSolution(self):
        print("=" * self.n * 2)
        for i in range(self.n):
            for j in range(self.n):
                print(self.solutionGrid[i][j], end=" ")
            print()
        print("=" * self.n * 2)

    """
    GOAL STATE -
    Checks the current grid state against the goal state.
    """
    def goalState(self):
        if self.grid == self.solutionGrid:
            return True
        else:
            return False

    """
    OPERATORS
    In a puzzle, the possible operators are moving the pieces
    into the zero piece. Here, return puzzles that are possible
    after the current grid.
    """
    """
    Returns a list of possible puzzle objects after operators
    """

    def operators(self):
        possiblePuzzles = []
        i, j = self.zeroLocation
        if self.moveDown():
            newPuzzle = deepcopy(self.grid)
            value = newPuzzle[i - 1][j]
            newPuzzle[i][j] = value
            newPuzzle[i - 1][j] = 0
            downPuzzle = Puzzle(2)
            downPuzzle.initUserGrid(newPuzzle)
            downPuzzle.cost = 1
            downPuzzle.depth = self.depth + downPuzzle.cost
            possiblePuzzles.append(downPuzzle)
        if self.moveUp():
            newPuzzle = deepcopy(self.grid)
            value = newPuzzle[i + 1][j]
            newPuzzle[i][j] = value
            newPuzzle[i + 1][j] = 0
            downPuzzle = Puzzle(2)
            downPuzzle.initUserGrid(newPuzzle)
            downPuzzle.cost = 1
            downPuzzle.depth = self.depth + downPuzzle.cost
            possiblePuzzles.append(downPuzzle)
        if self.moveLeft():
            newPuzzle = deepcopy(self.grid)
            value = newPuzzle[i][j + 1]
            newPuzzle[i][j] = value
            newPuzzle[i][j + 1] = 0
            downPuzzle = Puzzle(2)
            downPuzzle.initUserGrid(newPuzzle)
            downPuzzle.cost = 1
            downPuzzle.depth = self.depth + downPuzzle.cost
            possiblePuzzles.append(downPuzzle)
        if self.moveRight():
            newPuzzle = deepcopy(self.grid)
            value = newPuzzle[i][j - 1]
            newPuzzle[i][j] = value
            newPuzzle[i][j - 1] = 0
            downPuzzle = Puzzle(2)
            downPuzzle.initUserGrid(newPuzzle)
            downPuzzle.cost = 1
            downPuzzle.depth = self.depth + downPuzzle.cost
            possiblePuzzles.append(downPuzzle)
        return possiblePuzzles

    def moveDown(self):
        i, j = self.zeroLocation
        if i == 0:
            return False
        else:
            return True

    def moveUp(self):
        i, j = self.zeroLocation
        if i == (self.n - 1):
            return False
        else:
            return True

    def moveLeft(self):
        i, j = self.zeroLocation
        if j == (self.n - 1):
            return False
        else:
            return True

    def moveRight(self):
        i, j = self.zeroLocation
        if j == 0:
            return False
        else:
            return True

    """
    LESS THAN - 
    Operator overloading of the less than operator. This is used in 
    conjunction with the standard sort() function for the AStar comparisons.
    """
    def __lt__(self, other):
        if self.depth < other.depth:
            return self
        else:
            return other
