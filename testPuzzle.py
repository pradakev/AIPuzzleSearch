from puzzle import Puzzle

"""
TEST PUZZLE -
This driver tests the Puzzle class with generated objects.
"""

def main():
    # Test Standard Initialization
    puzzleA = Puzzle(4)
    puzzleA.printGrid()
    puzzleA.printSolution()
    print(puzzleA.goalState())

    # Test User Created Grid
    userGrid = [[1, 3, 4], [2, 5, 6], [8, 7, 0]]
    puzzleA.initUserGrid(userGrid)
    puzzleA.printGrid()
    puzzleA.printSolution()
    print(puzzleA)
    print('=' * 8)
    possiblePuzzles = puzzleA.operators()
    for i in possiblePuzzles:
        i.printGrid()

main()
