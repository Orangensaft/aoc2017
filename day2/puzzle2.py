# coding: utf-8
f = open("puzzleinput","r")
lines = [[int(g) for g in l.replace("\n","").split("\t")] for l in f.readlines()]

def getDiff(line):
    for i in range(len(line)):
        for j in range(i+1,len(line)): #get each number pair from left to right
            n1 = line[i]
            n2 = line[j]
            n1,n2 = max(n1,n2), min(n1,n2) #make sure n1 is the bigger and n2 the smaller one
            #print(f"n1:{n1} n2:{n2}")
            if n1 % n2 == 0: #check if divisble
                return n1 // n2 
            
total = 0
for line in lines: #iterate over lines
    n = getDiff(line)
    total += n #sum the result of the divisibles
print(f"Checksum: {total}")
