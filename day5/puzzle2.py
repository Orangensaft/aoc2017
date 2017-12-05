# coding: utf-8
f = open("input.txt","r")
ops = [int(l.replace("\n","")) for l in f.readlines()]
def doStep(ip, ops):
    try:
        offset = ops[ip]
    except:
        return False
    if offset >=3:
        ops[ip] -= 1
    else:
        ops[ip] += 1
    ip+=offset
    return ip
steps = 0
ip = 0
while ip is not False:
    ip = doStep(ip,ops)
    if ip is not False:
        steps+=1
print(f"Number of steps: {steps}")
