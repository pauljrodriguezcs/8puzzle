import sys
import numpy

class node:
    def __init__(self,state,cost,action=None,parent=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

def result(parent,action):
    
    temp_state = parent.state
    
    if action == "left":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i][j] == 0 and j != 0 :
                    temp = temp_state[i][j-1]
                    temp_state[i][j-1] = 0
                    temp_state[i][j] = temp
                    return temp_state

    elif action == "right":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i][j] == 0 and j != (numpy.size(temp_state,1)-1):
                    temp = temp_state[i][j+1]
                    temp_state[i][j+1] = 0
                    temp_state[i][j] = temp
                    return temp_state

    elif action == "up":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i][j] == 0 and i != 0:
                    temp = temp_state[i-1][j]
                    temp_state[i-1][j] = 0
                    temp_state[i][j] = temp
                    return temp_state

    elif action == "down":
        for i in range(numpy.size(temp_state,0)):
            for j in range(numpy.size(temp_state,1)):
                if temp_state[i][j] == 0 and i != (numpy.size(temp_state,1)-1):
                    temp = temp_state[i+1][j]
                    temp_state[i+1][j] = 0
                    temp_state[i][j] = temp
                    return temp_state


def child_node(parent_node,action):
    c_state = result(parent_node,action)
    cost = parent_node.cost+1
    
    print(c_state)
    print(parent_node.state)

    return node(c_state,cost,action,parent_node)


#def uniform_cost_search(m):






def main():
    row1 = [1,2,3]
    row2 = [4,5,6]
    row3 = [7,0,8]
    
    goal = numpy.matrix('1 2 3; 4 5 6; 7 8 0')
    
    error = 1
    
    print("Welcome to Paul's 8-puzzle solver")
    print( "Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.")
    
    while (error == 1):
        puzzleChoice = input()
        
        if (puzzleChoice == 1):
            error = 0

        elif (puzzleChoice == 2):
            error = 0

        else:
            print("Error: only 1 or 2 allowed")
            error = 1
    
    if(puzzleChoice == 2):
        print("Enter your puzzle, use a zero to represent the blank")
        print("Enter the first row, use spaces or tabs between numbers \t")
    
        row1 = raw_input().split()

        print("Enter the second row, use spaces or tabs between numbers \t")

        row2 = raw_input().split()
    
        print("Enter the third row, use spaces or tabs between numbers \t")

        row3 = raw_input().split()


    a = numpy.zeros(shape=(3,3))

    i = 0
    j = 0

    for i in range(3):
        for j in range(3):
            if(i == 0):
                a[i,j] = int(row1[j])
            
            elif(i == 1):
                a[i,j] = int(row2[j])
            
            else:
                a[i,j] = int(row3[j])

    print(a)

    n = node(a,0,None,None)
    print(n.state,n.cost,n.action,n.parent)

    m = child_node(n,"left")
    print(m.state,m.cost,m.action,m.parent.state)

main()
