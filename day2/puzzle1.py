# coding: utf-8
f = open("puzzleinput","r")
lines = [l.replace("\n","").split("\t") for l in f.readlines()]
total = 0
for line in lines:
    l_min = int(min(line,key=lambda x: int(x)))
    l_max = int(max(line,key=lambda x: int(x)))
    diff = l_max-l_min
    total += diff
    
print(f"Checksum: {total}")
