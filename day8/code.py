from collections import defaultdict
registers = defaultdict(lambda : 0)
highestVal = None
highestRegister = None

compOps = {
    "<" : lambda x, y : x < y,
    ">" : lambda x, y : x > y,
    "<=" : lambda x, y : x <= y,
    ">=" : lambda x, y : x >= y,
    "==" : lambda x, y : x == y,
    "!=" : lambda x, y : x != y,
}

registerOps = {
    "inc" : 1,
    "dec" : -1
}

def evalComp(compTarget,compOp,compVal):
    val1 = int(registers[compTarget])
    val2 = int(compVal)
    return compOps[compOp](val1,val2)

def evalLine(line):
    global highestVal
    global highestRegister
    #c inc -20 if c == 10
    target, op, val, _, compTarget, compOp, compVal = line.split(" ")

    if evalComp(compTarget, compOp, compVal):
        newVal = registers[target] + registerOps[op] * int(val)

        #START PUZZLE 2
        if highestVal is None or newVal > highestVal:
            highestVal = newVal
            highestRegister = target
        #END PUZZLE 2

        registers[target] = newVal

def getMax():
    maxVal = None
    maxRegister = None
    for register in registers:
        if maxVal is None or registers[register] > maxVal:
            maxVal = registers[register]
            maxRegister = register
    return maxRegister, maxVal

def getHighest():
    return highestRegister, highestVal

if __name__ == "__main__":
    with open("input.txt","r") as f:
        lines = [l.replace("\n","") for l in f.readlines()]

    for line in lines:
        evalLine(line)

    regName, regValue = getMax()
    regName2, regValue2 = getHighest()
    print(f"Register {regName} has the highest value after execution: {regValue}")
    print(f"Register {regName2} had the highest value: {regValue2}")
