# coding: utf-8
def getValue(x,y,cells):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
    summ = 0
    for dx,dy in dirs:
        coord = x+dx,y+dy
        posVal = cells.get(coord,0)
        summ+=posVal
    return summ


def makeGen(maxNum):
    x, y = 0, 0
    cur = 1
    allDirs = [(1,0), (0,1), (-1,0),(0,-1)]
    cells = {(x,y):1}
    stepSize = 1
    stepCount = -1
    nextTurn = 1
    dirPtr = 3
    curVal = 1
    while curVal <= maxNum:
        if cur == nextTurn:
            dirPtr = (dirPtr+1)%4
            stepCount+=1 #we have take one more curve
            if stepCount == 2: #we have taken two curves -> increment steps
                stepSize+=1
                stepCount=0 #0 turns again
            nextTurn = cur+stepSize
        
        dx, dy  = allDirs[dirPtr]
        x,y = x+dx , y+dy
        curVal = getValue(x,y,cells)
        cells[(x,y)] = curVal
        cur+=1
    return curVal
query = input("Your puzzle input: ")
print(f"Answer: {makeGen(int(query))}")
