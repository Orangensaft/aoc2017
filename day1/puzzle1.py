# coding: utf-8
def nextDigitSum(entry):
    entry = str(entry)
    strLen = len(entry)
    digitSum = 0
    for i in range(strLen):
        cur = entry[i]
        nextDigit = entry[(i+1)%strLen]
        if cur == nextDigit:
            digitSum+=int(cur)
    return digitSum
entr = input("Please enter captcha: ")
print(f"Solution: {nextDigitSum(entr)}")
