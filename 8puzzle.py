import sys
import numpy
import copy
import heapq
import Queue
import sets

#what the matrix should end up looking like
goal = numpy.matrix('1 2 3; 4 5 6; 7 8 0')
actions = ["left","right","up","down"]

#custom class for nodes
class node:
    def __init__(self,state,cost,action=None,parent=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
#end definition of node class

#return new matrix based off of parent and perform action
def result(parent,action):
    temp_state = copy.deepcopy(parent)
    i = 0
    j = 0
    
    #move the blank spot left and return the state
    if action == "left":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i,j] == 0 and j != 0 :
                    temp = temp_state[i,j-1]
                    temp_state[i,j-1] = 0
                    temp_state[i,j] = temp
                    return temp_state

    #move the blank spot right and return the state
    elif action == "right":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i,j] == 0 and j != (numpy.size(temp_state,1)-1):
                    temp = temp_state[i,j+1]
                    temp_state[i,j+1] = 0
                    temp_state[i,j] = temp
                    return temp_state

    #move the blank spot up and return the state
    elif action == "up":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i,j] == 0 and i != 0:
                    temp = temp_state[i-1,j]
                    temp_state[i-1,j] = 0
                    temp_state[i,j] = temp
                    return temp_state

    #move the blank spot down and return the state
    elif action == "down":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i,j] == 0 and i != (numpy.size(temp_state,1)-1):
                    temp = temp_state[i+1,j]
                    temp_state[i+1,j] = 0
                    temp_state[i,j] = temp
                    return temp_state

    else:
        return -1
#end of matrix manipulation

#create the child node based off of parent and the action
def child_node(parent,action):
    c_state = result(parent.state,action)
    
    if c_state is -1:
        return -1
    
    cost = copy.deepcopy(parent.cost)+1
    return node(c_state,cost,action,parent)
#end of child node creation

#Uniform Cost Search function
def uniform_cost_search(problem):
    #node = a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    n = node(problem,0,None,None)
    #frontier = a heap queue ordered by PATH-COST, with node as the only element
    frontier = [] 
    heapq.heappush(frontier,(n.cost,copy.deepcopy(n)))
    #explored = an empty set
    explored = [] 
    notdone = 1
    iterations = 1
    #loop do
    while notdone:
        #if EMPTY?(frontier) then return failure
        if not frontier: 
            return -1
        #node =POP(frontier) /*chooses the lowest-cost node in frontier */
        n = heapq.heappop(frontier) # returns tuple, (priority,data node)
        #if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
        if numpy.array_equal(n[1].state,goal): 
            return n[1]
        explored.append(n[1].state) #add node.STATE to explored
        for i in range(len(actions)): #for each action in problem.ACTIONS(node.STATE) do
            if n[1].state is not None:
                child = child_node(n[1],actions[i])
            if child.state is not -1 and n[1].state is not None:
                in_explored = 0
                tmp_explored = []
                while explored: #if child.STATE is not in explored
                    explored_state = explored.pop()
                    tmp_explored.append(explored_state)
                    if numpy.array_equal(child.state,explored_state):
                        in_explored = 1
                explored = tmp_explored
                if not in_explored: #if child.STATE is not in frontier
                    copy_frontier = []
                    found = 0
                    while frontier:
                        frontier_tuple = heapq.heappop(frontier)
                        heapq.heappush(copy_frontier,frontier_tuple)
                        if numpy.array_equal(child.state,frontier_tuple[1].state):
                            found = 1
                    frontier = copy_frontier
                    if not found:
                        heapq.heappush(frontier,(child.cost, child)) #frontier = INSERT(child,frontier)
                    else: #else if child.STATE is in frontier with higher PATH-COST then replace that frontier node with child
                        copy_frontier = []
                        while frontier:
                            frontier_tuple = heapq.heappop(frontier)
                            heapq.heappush(copy_frontier,frontier_tuple)
                            if numpy.array_equal(child.state,frontier_tuple[1].state) and child.cost < frontier_tuple[1].cost:
                                heapq.heapush(copy_frontier,(child.cost,child))
                                print(child.cost, "<", frontier_tuple[1].cost)
                        frontier = copy_frontier
        iterations = iterations+1
#end of Uniform Cost Function

#misplaced tiles function
def misplaced_tiles_value(problem):
    same_counter = 0
    for i in range(numpy.size(problem,0)):
        for j in range(numpy.size(problem,1)):
            if problem[i,j] == goal[i,j]:
                same_counter = same_counter + 1
    return (9 - same_counter)

#misplaced tiles function


#A* with Misplaced Tile Heuristic function
def misplaced_tile_heuristic(problem):
    #node = a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    n = node(problem,0,None,None)
    num_mis_tiles = misplaced_tiles_value(n.state)
    smallest_value = (num_mis_tiles, n) #the small child from parent
    children = []           #heapq with children, organized by f_n
    explored_tree = []      #nodes that have been seen
    iteration = 1
    while not numpy.array_equal(smallest_value[1].state,goal):
        explored_tree.append((smallest_value[0],smallest_value[1].state)) #add node.STATE to explored
        n = smallest_value[1]
        for i in range(len(actions)):
            if n is not None:
                child = child_node(n,actions[i])
                if child.state is not None:
                    num_mis_tiles = misplaced_tiles_value(child.state) #find number of misplaced tiles
                    f_n = num_mis_tiles + child.cost    #add total cost
                    heapq.heappush(children,(f_n,child))
        in_explored = 0
        tmp_explored_tree = []
        child_tuple = (0,n)
        smallest_found = 0
        while children and not smallest_found:  #while children list is not empty and the smallest child has not been found yet
            tmp_explored_tree = []
            #print "in while loop"
            child_tuple = heapq.heappop(children)
            while explored_tree and not in_explored:    #while the explored tree is not empty and its not in explored set
                explored_tuple = explored_tree.pop()
                tmp_explored_tree.append(copy.deepcopy(explored_tuple))
                if numpy.array_equal(child_tuple[1].state,explored_tuple[1]):
                    in_explored = 1
            if in_explored:
                in_explored = 0
            else:
                smallest_value = child_tuple
                smallest_found = 1
            explored_tree = tmp_explored_tree
        iteration = iteration + 1
    return smallest_value[1]
#end of A* with Misplaced Tile Heuristic function

#Manhattan Distance Calculator
def manhattan_calculator(problem):
    goal_values = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)]
                    #1     2    3      4     5     6     7     8
    total_distance = 0
    for i in range(numpy.size(problem,0)):
        for j in range(numpy.size(problem,1)):
            if int(problem[i,j]) is not 0:
                compare_coord = goal_values[int(problem[i,j]-1)]
                total_distance = total_distance + abs(i-compare_coord[0]) + abs(j-compare_coord[1])
    return total_distance

#end manhattan distance calculator end

#A* with Manhattan Distance Heuristic function
def manhattan_distance_heuristic(problem):
    #node = a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    n = node(problem,0,None,None)
    total_distance = manhattan_calculator(n.state)
    smallest_value = (total_distance, n) #the small child from parent
    children = []           #heapq with children, organized by f_n
    explored_tree = []      #nodes that have been seen
    iteration = 1
    while not numpy.array_equal(smallest_value[1].state,goal):
        explored_tree.append((smallest_value[0],smallest_value[1].state)) #add node.STATE to explored
        n = smallest_value[1]
        for i in range(len(actions)):
            if n is not None:
                child = child_node(n,actions[i])
                if child.state is not None:
                    total_distance = manhattan_calculator(child.state) #find number of misplaced tiles
                    f_n = total_distance   #add total cost
                    heapq.heappush(children,(f_n,child))
        in_explored = 0
        tmp_explored_tree = []
        child_tuple = (0,n)
        smallest_found = 0
        while children and not smallest_found:  #while children list is not empty and the smallest child has not been found yet
            tmp_explored_tree = []
            #print "in while loop"
            child_tuple = heapq.heappop(children)
            while explored_tree and not in_explored:    #while the explored tree is not empty and its not in explored set
                explored_tuple = explored_tree.pop()
                tmp_explored_tree.append(copy.deepcopy(explored_tuple))
                if numpy.array_equal(child_tuple[1].state,explored_tuple[1]):
                    in_explored = 1
            if in_explored:
                in_explored = 0
            else:
                smallest_value = child_tuple
                smallest_found = 1
            explored_tree = tmp_explored_tree
        iteration = iteration + 1
    return smallest_value[1]


#end of A* with Manhatta Distance Heuristic function

def main():
    
    #default puzzle 1   1 2 3 4 x 6 7 5 8
    #row1 = [1,2,3]
    #row2 = [4,0,6]
    #row3 = [7,5,8]
    
    #default puzzle 2   1 6 2 4 3 8 7 x 5
    #row1 = [1,6,2]
    #row2 = [4,3,8]
    #row3 = [7,0,5]
    
    #default puzzle 3   2 1 3 4 7 6 5 8 x
    row1 = [2,1,3]
    row2 = [4,7,6]
    row3 = [5,8,0]
    
    #default puzzle 4   5 x 2 8 4 7 6 3 1
    #row1 = [5,0,2]
    #row2 = [8,4,7]
    #row3 = [6,3,1]
    
    #default puzzle 5   8 6 7 2 5 4 3 x 1
    #row1 = [8,6,7]
    #row2 = [2,5,4]
    #row3 = [3,0,1]

    
    error = 1
    
    print("Welcome to Paul's 8-puzzle solver")
    print( "Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.")
    
    #get only valid inputs from user 1 or 2
    while (error == 1):
        puzzleChoice = input()
        
        if (puzzleChoice == 1):
            error = 0

        elif (puzzleChoice == 2):
            error = 0

        else:
            print("Error: only 1 or 2 allowed")
            error = 1

    #custom puzzle chosen, parse in
    if(puzzleChoice == 2):
        print("Enter your puzzle, use a zero to represent the blank")
        print("Enter the first row, use spaces or tabs between numbers \t")
    
        row1 = raw_input().split()

        print("Enter the second row, use spaces or tabs between numbers \t")

        row2 = raw_input().split()
    
        print("Enter the third row, use spaces or tabs between numbers \t")

        row3 = raw_input().split()


    #choose heuristic to solve problem
    print "Enter your choice of algorithm \n"
    print "\t 1. Uniform Cost Search"
    print "\t 2. A* with the Misplaced Tile heuristic"
    print "\t 3. A* with the Manhattan distance heuristic"

    error = 1
    while (error == 1):
        heuristic_choice = input()
        
        if (heuristic_choice == 1):
            error = 0

        elif (heuristic_choice == 2):
            error = 0
        
        elif (heuristic_choice == 3):
            error = 0
        
        else:
            print("Error: only 1, 2, or 3 allowed")
            error = 1


    #create matrix template
    a = numpy.zeros(shape=(3,3))

    i = 0
    j = 0

    #fill in matrix with default or custom values
    for i in range(3):
        for j in range(3):
            if(i == 0):
                a[i,j] = int(row1[j])
            
            elif(i == 1):
                a[i,j] = int(row2[j])
            
            else:
                a[i,j] = int(row3[j])

    if heuristic_choice is 1:
        value = uniform_cost_search(a)

    elif heuristic_choice is 2:
        print "choice numero dos..."
        value = misplaced_tile_heuristic(a)

    elif heuristic_choice is 3:
        print "choice numero tree..."
        value = manhattan_distance_heuristic(a)

    if value == -1:
       print("No solution")

    else:
        printer = Queue.LifoQueue()
        while value.parent is not None:
            printer.put(value)
            value = value.parent
        s = "Start State: "
        print s, '\n', value.state
        while not printer.empty():
            tn = printer.get()
            print'\n', "Slide blank",tn.action
            print tn.state

main()
