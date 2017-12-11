def analyzeStream(stream,debug=False):
    depth = 0
    groupCount = 0
    score = 0
    delCount = 0 #part 2
    skipNext = False
    inGarbage = False

    for character in stream:
        if debug:
            input(f"Char: {character}; d:{depth} gc:{groupCount} s:{score} sn:{skipNext} iG:{inGarbage}")
        if skipNext: #We have to skip the next char
            skipNext = False #We don't have to skip anymore
            continue
        if character == "!": #Skip next char
            skipNext = True
            continue
        if inGarbage:
            if character == ">": # exit garbage
                inGarbage = False
                continue
            delCount+=1 #part2
            continue #Ignore everything in garbage
        if character == "<": #Start garbage
            inGarbage = True
            continue
        if character == ",":
            continue #no need to handle commas.
        if character == "{": #start group
            depth+=1
            continue
        if character == "}": #end group
            score+=depth
            depth-=1
            groupCount+=1
            continue
    return groupCount, score, delCount

if __name__ == "__main__":
    with open("input.txt","r") as f:
        stream = f.read()
    groupCount, score, deleted = analyzeStream(stream)
    print(f"Total score: {score}")
    print(f"Deleted: {deleted}")#part2
