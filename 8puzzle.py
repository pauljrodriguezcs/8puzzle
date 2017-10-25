import sys
import numpy

#class node:
#    def __init__(self,state,parent=None,action,cost):
#        self.state = state
#        self.parent = parent
#        self.action = action
#        self.cost = cost

def result(state,action):
    if action == "left":
        for i in range(numpy.size(state,0)):
            for j in range(numpy.size(state,1)):
                if state[i][j] == 0 and j != 0 :
                    temp = state[i][j-1]
                    state[i][j-1] = 0
                    state[i][j] = temp

    elif action == "right":
        for i in range(numpy.size(state,0)):
            for j in range(numpy.size(state,1)):
                if state[i][j] == 0 and j != (numpy.size(state,1)-1):
                    temp = state[i][j+1]
                    state[i][j+1] = 0
                    state[i][j] = temp
                    break

    elif action == "up":
        for i in range(numpy.size(state,0)):
            for j in range(numpy.size(state,1)):
                if state[i][j] == 0 and i != 0:
                    temp = state[i-1][j]
                    state[i-1][j] = 0
                    state[i][j] = temp
    elif action == "down":
        break_flag = 0

        for i in range(numpy.size(state,0)):
            for j in range(numpy.size(state,1)):
                if state[i][j] == 0 and i != (numpy.size(state,1)-1):
                    temp = state[i+1][j]
                    state[i+1][j] = 0
                    state[i][j] = temp
                    break_flag = 1
                    break
            if break_flag == 1:
                break


#def child_node(problem,parent,action):
    
#    state =
    
    
    
    
    
#    return node(state,parent,action,cost)





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


main()
