# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    # we need to use a Stack
    frontier = util.Stack()
    # every element in the frontier is a tuple (state, path, cost)
    current = (problem.getStartState(), [], 0)
    # initialize the first element in the frontier
    frontier.push(current)
    # create a set for nodes already expanded
    expanded = set()
    
    while not frontier.isEmpty():
        # get the node from the stack
        node, path, cost = frontier.pop()
        # if is the goal return path        
        if problem.isGoalState(node):
            return path
        
        # if it has not been expanded before :
        if not node in expanded:
            expanded.add(node)
            # if it is not the goal state, check all the successors states
            for next_node, direction, step_cost in problem.getSuccessors(node):
                # create a new element in the frontier
                new_path = path + [direction]
                new_cost = cost + step_cost
                frontier.push((next_node, new_path, new_cost))
    return []
        

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    "*** YOUR CODE HERE ***"
    
    # we need to use a Queue
    frontier = util.Queue()
    # every element in frontier is in the form (state, path, cost)
    current = (problem.getStartState(), [], 0)
    # initialize the first element in the frontier
    frontier.push(current)
    # create a set for nodes already expanded
    expanded = []
    
    while not frontier.isEmpty():
        # get the node from the stack
        node, path, cost = frontier.pop()
        # if is the goal return path        
        if problem.isGoalState(node):
            return path
        
        # if it has not been expanded before :
        if not node in expanded:
            expanded.append(node)
            # if it is not the goal state, check all the successors states
            for next_state, direction, step_cost in problem.getSuccessors(node):
                # create a new element in the frontier
                new_path = path + [direction]
                new_cost = cost + step_cost
                frontier.push((next_state, new_path, new_cost))
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    "*** YOUR CODE HERE ***"
    
    # we need to use a priority Queue
    frontier = util.PriorityQueue()
    # every element in frontier is in the form ((state, path, cost), cost)

    # initialize the first element in the frontier
    frontier.push((problem.getStartState(), [], 0),0)
    # create a set for nodes already expanded
    expanded = set()
    
    while not frontier.isEmpty():
        # get the node from the stack
        node, path, cost = frontier.pop()
        # if is the goal return path
        if problem.isGoalState(node):
            return path
        
        # if it has not been expanded before :
        if not node in expanded:
            expanded.add(node)
            # if it is not the goal state, check all the successors states
            for next_node, direction, step_cost  in problem.getSuccessors(node):
                # create a new element in the frontier
                new_path = path + [direction]
                new_cost = cost + step_cost
                frontier.push((next_node, new_path, new_cost), new_cost)
    return []
    
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # we need to use a priority Queue
    frontier = util.PriorityQueue()
    # every element in frontier is in the form ((state, path, cost), cost)
    # initialize the first element in the frontier
    frontier.push((problem.getStartState(), [], 0),0)
    # create a set for nodes already expanded
    expanded = list()
    
    while not frontier.isEmpty():
        # get the node from the stack
        node, path, cost = frontier.pop()
        # if is the goal return path
        if problem.isGoalState(node):
            return path
        # if it has not been expanded before :
        if not node in expanded:
            expanded.append(node)
            
            for next_node, direction, step_cost  in problem.getSuccessors(node):
                new_path = path + [direction]
                new_cost = cost + step_cost
                new_f = cost + heuristic(next_node, problem)
                # create a new element in the frontier
                frontier.push((next_node, new_path, new_cost), new_f)
    return []    
    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
