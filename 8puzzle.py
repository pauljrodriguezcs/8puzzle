import sys
import numpy
import copy

#what the matrix should end up looking like
goal = numpy.matrix('1 2 3; 4 5 6; 7 8 0')

#custom class for nodes
class node:
    def __init__(self,state,cost,action=None,parent=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

#return new matrix based off of parent and perform action
def result(parent,action):
    temp_state = copy.deepcopy(parent)
    
    #move the blank spot left and return the state
    if action == "left":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i][j] == 0 and j != 0 :
                    temp = temp_state[i][j-1]
                    temp_state[i][j-1] = 0
                    temp_state[i][j] = temp
                    return temp_state

    #move the blank spot right and return the state
    elif action == "right":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i][j] == 0 and j != (numpy.size(temp_state,1)-1):
                    temp = temp_state[i][j+1]
                    temp_state[i][j+1] = 0
                    temp_state[i][j] = temp
                    return temp_state

    #move the blank spot up and return the state
    elif action == "up":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i][j] == 0 and i != 0:
                    temp = temp_state[i-1][j]
                    temp_state[i-1][j] = 0
                    temp_state[i][j] = temp
                    return temp_state

    #move the blank spot down and return the state
    elif action == "down":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i][j] == 0 and i != (numpy.size(temp_state,1)-1):
                    temp = temp_state[i+1][j]
                    temp_state[i+1][j] = 0
                    temp_state[i][j] = temp
                    return temp_state

#create the child node based off of parent and the action
def child_node(parent,action):
    c_state = result(parent.state,action)
    cost = parent.cost+1

    return node(c_state,cost,action,parent.state)



def uniform_cost_search(problem):







def main():
    
    #default puzzle
    row1 = [1,2,3]
    row2 = [4,5,6]
    row3 = [7,0,8]
    
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
    #
    #
    #       FILL ME !!!!!!!!!
    #
    #

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

    value = uniform_cost_search(a)

main()
