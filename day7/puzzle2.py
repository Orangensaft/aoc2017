# coding: utf-8
# %load puzzle2.py
def splitEntry(e):
    if e.count(" -> "):
        source, targets = e.split(" -> ")
    else:
        source = e
        targets = []
    sourceName, sourceWeight = source.split(" (")
    sourceWeight = sourceWeight.replace(")","")
    if len(targets) > 0:
        targets = targets.split(", ")
    return sourceName, sourceWeight, targets

def findUnbalancedOne(startNode):
     nexts = pointsTo[startNode]
     counter = {}
     nodeWeight = {}
     for n in nexts:
         w = updateWeight(n)
         count = counter.get(w,0)
         counter[w] = count+1
         nodeWeight[w] = n #can be overwritten, no problem
     unBalanced = None
     for key in counter:
         if counter[key] == 1:
             unBalanced = nodeWeight[key]
             break
     return unBalanced

def updateWeight(node):
     nodeWeight = weights[node] + sum([updateWeight(n) for n in pointsTo[node]])
     return nodeWeight

f = open("input.txt","r")
lines = [l.replace("\n","") for l in f.readlines()]
pointsTo = {}
pointedBy = {}
weights = {}
for line in lines:
    name, weight, outNodes = splitEntry(line)
    weights[name] = int(weight)
    pointsTo[name] = outNodes
    for node in outNodes:
        pointedBy[node] = name
        
for node in weights:
    if node not in pointedBy:
        print(f"Base: {node}")
        break
start = node
    
curNode = start
while curNode is not None:
    lastNode = curNode
    curNode = findUnbalancedOne(curNode)
    
def getWeights(node):
    parent = pointedBy[node]
    ws = [updateWeight(n) for n in pointsTo[parent]]
    diff = max(ws)-min(ws)
    return diff
rightWeight = weights[lastNode] - getWeights(lastNode)
print(f"Correct weight: {rightWeight}")
