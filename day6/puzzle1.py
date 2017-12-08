# coding: utf-8
def findNextBank(banks):
    indx = 0
    max_elem = banks[0]
    for i in range(len(banks)):
        if banks[i] > max_elem:
            max_elem = banks[i]
            indx = i
    return indx

def redistribute(banks,idx):
    num = banks[idx]
    banks[idx] = 0
    while num>0:
        idx = (idx+1)%len(banks)
        banks[idx] += 1
        num -= 1

def cycle(banks):
    idx = findNextBank(banks)
    redistribute(banks,idx)
    return ".".join([str(i) for i in banks])

with open("input.txt","r") as f:
    banks = [int(l) for l in f.readline().split("\t")]
    
bank_counter = []
bank_counter.append(".".join([str(i) for i in banks]))
step = 0
while True:
    afterCycle = cycle(banks)
    step+=1
    if afterCycle in bank_counter:
        break
    else:
        bank_counter.append(afterCycle)
        
print(f"Steps: {step}")
