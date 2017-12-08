# coding: utf-8
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
    
