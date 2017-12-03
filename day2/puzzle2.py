# coding: utf-8
f = open("puzzleinput","r")
lines = [[int(g) for g in l.replace("\n","").split("\t")] for l in f.readlines()]
def getDiff(line):
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            n1 = line[i]
            n2 = line[j]
            n1,n2 = max(n1,n2), min(n1,n2)
            #print(f"n1:{n1} n2:{n2}")
            if n1 % n2 == 0:
                return n1 // n2 
            
total = 0
for line in lines:
    n = getDiff(line)
    total += n
print(f"Checksum: {total}")
