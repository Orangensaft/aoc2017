# coding: utf-8
def makeGen(end):
    x, y = 0, 0
    cur = 1
    allDirs = [(1,0), (0,1), (-1,0),(0,-1)]
    stepSize = 1
    stepCount = -1
    nextTurn = 1
    dirPtr = 3
    while cur != end:
        if cur == nextTurn:
            dirPtr = (dirPtr+1)%4
            stepCount+=1 #we have take one more curve
            if stepCount == 2: #we have taken two curves -> increment steps
                stepSize+=1
                stepCount=0 #0 turns again
            nextTurn = cur+stepSize
        
        dx, dy  = allDirs[dirPtr]
        x,y = x+dx , y+dy
        cur+=1
        #print(f"n:{cur} xy=({x},{y})")
    return x,y
query = input("Your puzzle input: ")
x,y = makeGen(int(query))
wayLen = abs(x) + abs(y)
print(f"Answer is: {wayLen}")
