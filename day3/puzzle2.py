# coding: utf-8
"""
General idea:
Generate the coordinates the same as in part one.
Save the value of the current coordinate in a dictionary (coord -> value)
To compute a new value we can use the dictionary to get the neighbour values
"""

#Function to get value of given coordinate
def getValue(x,y,cells):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)] #Neighbour directions
    summ = 0
    for dx,dy in dirs:
        coord = x+dx,y+dy #neighbour to check
        posVal = cells.get(coord,0) #get value of him
        summ+=posVal
    return summ


def makeGen(maxNum):
    x, y = 0, 0
    cur = 1
    allDirs = [(1,0), (0,1), (-1,0),(0,-1)]
    cells = {(x,y):1} #value of first cell is 1
    stepSize = 1
    stepCount = -1
    nextTurn = 1
    dirPtr = 3
    curVal = 1
    while curVal <= maxNum: #break as soon as we have a value bigger than the requested one
        if cur == nextTurn:
            dirPtr = (dirPtr+1)%4
            stepCount+=1 #we have take one more curve
            if stepCount == 2: #we have taken two curves -> increment steps
                stepSize+=1
                stepCount=0 #0 turns again
            nextTurn = cur+stepSize
        
        dx, dy  = allDirs[dirPtr]
        x,y = x+dx , y+dy
        curVal = getValue(x,y,cells) #get value for current cell
        cells[(x,y)] = curVal #save value with current coordinate
        cur+=1
    return curVal

query = input("Your puzzle input: ")
print(f"Answer: {makeGen(int(query))}")
