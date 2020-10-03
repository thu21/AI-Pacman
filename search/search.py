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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    stack=util.Stack()
    visited=[]
    path=[]
    start=problem.getStartState() 

    if problem.isGoalState(start):
        return []
    # push the start section into  empty list   
   
    stack.push((start,[]),0) 
   # print (start)

    while not stack.isEmpty():
      
        xy,path=stack.pop()
        # print 'path ', path

        #  add xy to the top of visited
        visited.append(xy)
       # print'visited',visited

        if problem.isGoalState(xy):  
          #  print (path)
            return path
            
        successor = problem.getSuccessors(xy)
       # print 'successor',successor

        if successor:
            for elem in successor:
               if elem[0] not in visited:
              #   print elem[0]
              #   print elem[1]
                 newPath=path+[elem[1]]
               #  print 'ww',newPath
                 stack.push((elem[0],newPath))
                
                 

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queueXY = util.Queue()

    visited = [] # Visited states
    path = [] # Every state keeps it's path from the starting state
    start=problem.getStartState()
    # Check if initial state is goal state #
    if problem.isGoalState(start):
        return []

    # Start from the beginning and find a solution, path is empty list #
    queueXY.push((start,[]))

    while not queueXY.isEmpty():

        # Get informations of current state #
        xy,path = queueXY.pop() 
        visited.append(xy)
        #print 'vis',visited
        #print path
        # Terminate condition: reach goal #
        if problem.isGoalState(xy):
            return path

        # Get successors of current state #
        succ = problem.getSuccessors(xy)
        #print 'succ',succ

        if succ:
            for elem in succ:
                if elem[0] not in visited :
                    #print elem[0]
                    #print elem[1]
                    newPath = path + [elem[1]] 
                    queueXY.push((elem[0],newPath))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
 
  
    queueXY = PriorityQueue.PriorityQueue()

    visited = [] # Visited states
    path = [] # Every state keeps it's path from the starting state
    start=problem.getStartState()
   
    if problem.isGoalState(start):
        return []
                                      #
    queueXY.push((start,[]),0)

    while not queueXY.isEmpty(): 

        # Get informations of current state #
        xy,path = queueXY.pop() # Take position and path
        visited.append(xy)

        if problem.isGoalState(xy):
            return path

        # Get successors of current state #
        succ = problem.getSuccessors(xy)

        if succ:
            for elem in succ:
                if elem[0] not in visited and (elem[0] not in (state[2][0] for state in queueXY.heap)):

                    #    Like previous algorithms: we should check in this point if successor
                    #    is a goal state so as to follow lectures code

                    newPath = path + [elem[1]]
                    pri = problem.getCostOfActions(newPath)

                    queueXY.push((elem[0],newPath),pri)

                # State is in queue. Check if current path is cheaper from the previous one #
                elif elem[0] not in visited and (elem[0] in (state[2][0] for state in queueXY.heap)):
                    for state in queueXY.heap:
                        if state[2][0] == elem[0]:
                            oldPri = problem.getCostOfActions(state[2][1])

                    newPri = problem.getCostOfActions(path + [elem[1]])

                    # State is cheaper with his hew father -> update and fix parent #
                    if oldPri > newPri:
                        newPath = path + [elem[1]]
                        queueXY.update((elem[0],newPath),newPri)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

from util import PriorityQueue
class MyPriorityQueueWithFunction(PriorityQueue):
  
    def  __init__(self, problem, priorityFunction):
        "priorityFunction (elem) -> priority"
        self.priorityFunction = priorityFunction      # store the priority function
        PriorityQueue.__init__(self)        # super-class initializer
        self.problem = problem
    def push(self, elem, heuristic):
        "Adds an elem to the queue with priority from the priority function"
        PriorityQueue.push(self, elem, self.priorityFunction(self.problem,elem,heuristic))

# Calculate f(n) = g(n) + h(n) #
def f(problem,state,heuristic):

    return problem.getCostOfActions(state[1]) + heuristic(state[0],problem)

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # queueXY: ((x,y),[path]) #
    queueXY = MyPriorityQueueWithFunction(problem,f)

    path = [] # Every state keeps it's path from the starting state
    visited = [] # Visited states


    # Check if initial state is goal state #
    if problem.isGoalState(problem.getStartState()):
        return []

    # Add initial state. Path is an empty list #
    element = (problem.getStartState(),[])

    queueXY.push(element,heuristic)

    while(True):

        # Terminate condition: can't find solution #
        if queueXY.isEmpty():
            return []

        # Get informations of current state #
        xy,path = queueXY.pop() # Take position and path

       # print 'path',path
        # State is already been visited. A path with lower cost has previously
        # been found. Overpass this state
        if xy in visited:
            continue

        visited.append(xy)
       # print 'visited',visited
        # Terminate condition: reach goal #
        if problem.isGoalState(xy):
            return path

        # Get successors of current state #
        succ = problem.getSuccessors(xy)
       # print 'succ',succ
        # Add new states in queue and fix their path #
        if succ:
            for elem in succ:
                if elem[0] not in visited:

                    # Like previous algorithms: we should check in this point if successor
                    # is a goal state so as to follow lectures code

                    newPath = path + [elem[1]] # Fix new path
                    element = (elem[0],newPath)
                    queueXY.push(element,heuristic)
                   

# Editor:
# Sdi1500129
# Petropoulakis Panagiotis

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
