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

from collections import deque
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

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    stack = util.Stack()
    visited = set()
    start = problem.getStartState()
    stack.push((start, [], 0)) # appending inital state to stack

    while not stack.isEmpty(): #checks to see if there are any more elements on the stack
        state_env = stack.pop()
        currState = state_env[0] #state
        paths = state_env[1] #path actions
        cost = state_env[2] #cost of traversing that path

        if problem.isGoalState(currState):
            return paths
        
        if currState not in visited: #checks cache for recurrence 
            visited.add(currState)
            children = problem.getSuccessors(currState) #gets all children of that node
            for next_step, next_path, next_cost in children:
                if next_step not in visited:
                    stack.push((next_step, paths + [next_path], cost + next_cost))
    return []    



    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    q = util.Queue()
    visited = set()
    start = problem.getStartState()
    q.push((start, [], 0)) # insert initial state to PQ

    while not q.isEmpty(): #checks to see if there are any more elements on the stack
        state_env = q.pop()
        currState = state_env[0] #state
        paths = state_env[1] #path actions
        cost = state_env[2] #cost of traversing that path

        if problem.isGoalState(currState):
            return paths
        
        if currState not in visited: #checks cache for recurrence 
            visited.add(currState)
            children = problem.getSuccessors(currState) #gets all children of that node
            for next_step, next_path, next_cost in children:
                if next_step not in visited:
                    q.push((next_step, paths + [next_path], cost + next_cost))
    return []

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    pq = util.PriorityQueue()
    visited = set()
    start = problem.getStartState()
    pq.push((start, [], 0), 0) # insert initial state to PQ

    while not pq.isEmpty(): #checks to see if there are any more elements on the stack
        state_env = pq.pop()
        currState = state_env[0] #state
        paths = state_env[1] #path actions
        cost = state_env[2] #cost of traversing that path

        if problem.isGoalState(currState):
            return paths
        
        if currState not in visited: #checks cache for recurrence 
            visited.add(currState)
            children = problem.getSuccessors(currState) #gets all children of that node
            for next_step, next_path, next_cost in children:
                if next_step not in visited:
                    pq.push((next_step, paths + [next_path], cost + next_cost), cost+next_cost)
    return []

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    visited = set()
    start = problem.getStartState()
    h = heuristic(start,problem) # heuristic
    pq.push((start, [],0),0+h) # insert initial state to PQ

    while pq: #checks to see if there are any more elements on the stack
        state_env = pq.pop()
        currState = state_env[0] #state
        paths = state_env[1] #path actions
        cost = state_env[2] #cost of traversing that path

        if problem.isGoalState(currState):
            return paths
        
        if currState not in visited: #checks cache for recurrence 
            visited.add(currState)
            children = problem.getSuccessors(currState) #gets all children of that node
            for next_step, next_path, next_cost in children:
                if next_step not in visited:
                    pq.push((next_step, paths + [next_path], cost + next_cost),cost+next_cost+heuristic(next_step,problem))
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
