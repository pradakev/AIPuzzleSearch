from puzzle import Puzzle
class AStar:
    """
    ASTAR -
    A class representing the queueing function that will be used
    for the General Search Algorithm. Functions will include the
    Uniform Cost Search, Misplaced Tile, and Manhattan Distance algorithms.
    """
    def __init__(self, heuristic):
        self.heuristic = heuristic

    """
    UNIFORM COST SEARCH -
    Nodes are sorted by depth cost only. Done by taking the 
    current nodes on the queue, nodes expanded, and sorting
    by lowest depth using the lambda function. 
    """
    def UniformCostSearch(self, nodes, nodeExpansion, visited):
        self.nodes = nodes
        self.nodeExpansion = nodeExpansion
        self.visited = visited
        self.checkRepetitions()
        # UCS Should return the list with the lowest value
        # to the right of the the queue. (Descending order)
        newNodesList = self.nodeExpansion + self.nodes
        # Cite key=lambda sort here
        # Lambda is used here to sort by Puzzle object's depth variable.
        # x stores the variable. Since we need descending, we set reverse=True.
        newNodesList = sorted(newNodesList, key=lambda x: x.depth, reverse=True)
        DEBUG = False
        if DEBUG:
            print("&" * 8)
            for i in range(len(newNodesList)):
                newNodesList[i].printGrid()
            print("&" * 8)
        return newNodesList

    """
    ASTAR WITH MISPLACTED TILE HEURISTIC - 
    Nodes are sorted by depth cost summed with the misplaced tile h(n).
    """
    def AStarMTH(self, nodes, nodeExpansion, visited):
        self.nodes = nodes
        self.nodeExpansion = nodeExpansion
        self.visited = visited
        self.checkRepetitions()
        # MTH Should return the list with the lowest value
        # to the right of the the queue.
        newNodesList = self.nodeExpansion + self.nodes
        # Cite key=lambda sort here
        # Lambda is used here to sort by Puzzle object's depth variable summed
        # with Puzzle's misplaced tile Heuristic.
        # x stores the variable. Since we need descending, we set reverse=True.
        newNodesList = sorted(newNodesList, key=lambda x:
        x.depth + x.misplacedTileH, reverse=True)
        DEBUG = False
        if DEBUG:
            print("&" * 8)
            for i in range(len(newNodesList)):
                newNodesList[i].printGrid()
            print("&" * 8)
        return newNodesList

    """
    ASTAR WITH MANHATTAN DISTANCE HEURISTIC - 
    Nodes are sorted by depth cost summed with manhattan distance h(n)
    """
    def AStarMDH(self, nodes, nodeExpansion, visited):
        self.nodes = nodes
        self.nodeExpansion = nodeExpansion
        self.visited = visited
        self.checkRepetitions()
        # UCS Should return the list with the lowest value
        # to the right of the the queue.
        newNodesList = self.nodeExpansion + self.nodes
        # Cite key=lambda sort here
        newNodesList = sorted(newNodesList, key=lambda x:
        x.depth + x.manhattanDistH, reverse=True)
        DEBUG = False
        if DEBUG:
            print("&" * 8)
            for i in range(len(newNodesList)):
                newNodesList[i].printGrid()
            print("&" * 8)
        return newNodesList

    """
    CHECK REPETITIONS - 
    Each algorithm must check for any repetitions that the node expansion
    may have created. This function utilizes the overloaded operator
    __lt__ in Puzzle in order to check if a Puzzle node is in another
    data structure.
    """
    def checkRepetitions(self):
        repetitions = []
        for node in self.nodeExpansion:
            if node in self.nodes or node in self.visited:
                self.nodeExpansion.remove(node)






