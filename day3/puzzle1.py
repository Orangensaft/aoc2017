# coding: utf-8
"""
General idea:
Just compute the next coordinates until we have reached high enough number.
We are always taking two turn until we are increasing the step size (number of steps until next turn)
Using that, the next coordinate can be computed easily
"""
def makeGen(end):
    x, y = 0, 0 #Current position
    cur = 1 #current number
    allDirs = [(1,0), (0,1), (-1,0),(0,-1)] #directions (right,up,left,down)
    stepSize = 1 #number of steps to take until next turn
    stepCount = -1 #number of turns taken
    nextTurn = 1 #next number to turn on
    dirPtr = 3 #current direction we are going to (pointer for allDirs)
    while cur != end:
        if cur == nextTurn: #we have to take a turn
            dirPtr = (dirPtr+1)%4 #next direction
            stepCount+=1 #we have taken one more turn
            if stepCount == 2: #we have taken two turn 
                stepSize+=1 #-> increment number of steps until next turn
                stepCount=0 # Reset turn counter
            nextTurn = cur+stepSize #Next number to turn on is the current one plus the number of steps until the next turn
        
        dx, dy  = allDirs[dirPtr] #get direction
        x,y = x+dx , y+dy #add direction to position -> move
        cur+=1 #increment current number
        #print(f"n:{cur} xy=({x},{y})")
    return x,y #we have reached the desired number -> return coords

query = input("Your puzzle input: ")
x,y = makeGen(int(query))
wayLen = abs(x) + abs(y)
print(f"Answer is: {wayLen}")
