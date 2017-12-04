# coding: utf-8
def isValid(passwd):
    allWords = set()
    words = passwd.split(" ")
    for word in words:
        if word in allWords:
            return False
        allWords.add(word)
    return True
f = open("input.txt","r")
lines = [l.replace("\n","") for l in f.readlines()]
count = 0
for line in lines:
    if isValid(line):
        count+=1
        
print(f"Valid passphrases: {count}")
