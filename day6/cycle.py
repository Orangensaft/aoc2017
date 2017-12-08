# coding: utf-8
def cycle(banks):
    idx = findNextBank(banks)
    redistribute(banks,idx)
    return ".".join([str(i) for i in banks])
