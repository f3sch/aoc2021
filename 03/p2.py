#!/bin/python3

import sys
import copy

def countN(binaryN, count0, count1, pos):
    for bin in binaryN:
            if bin[pos] == "1":
                count1[pos] += 1
            elif bin[pos] == "0":
                count0[pos] += 1
            else:
                continue
    return

def removeN(binaryN, kbit, pos):
    tmp = list(filter(lambda bit: bit[pos] != kbit, binaryN))
    return tmp

def p1():
    if len(sys.argv) != 2:
        print("File")
        exit(-1)

    binaryN = []
    with open(sys.argv[1]) as f:
        for line in f:
            binaryN.append(line)

    count1oxy = [0 for _ in range(12)]
    count1c02 = [0 for _ in range(12)]
    count0oxy = [0 for _ in range(12)]
    count0c02 = [0 for _ in range(12)]

    oxy = copy.deepcopy(binaryN)
    c02 = copy.deepcopy(binaryN)
    for pos in range(12):
        countN(oxy, count0oxy, count1oxy, pos)
        print(oxy)
        print(count0oxy)
        print(count1oxy)

        if count1oxy[pos] >= count0oxy[pos]:
            oxy = removeN(oxy, "1", pos)
        else:
            oxy = removeN(oxy, "0", pos)

        if len(oxy) == 1:
            break

    for pos in range(12):
        countN(c02, count0c02, count1c02, pos)
        if count1c02[pos] >= count0c02[pos]:
            c02 = removeN(c02, "0", pos)
        else:
            c02 = removeN(c02, "1", pos)

        if len(c02) == 1:
            break

    oxy_rate = int(oxy[0],2)
    c02_rate = int(c02[0],2)




    print("Oxy rate: {}".format(oxy_rate))
    print("C02 rate: {}".format(c02_rate))
    print("Life support: {}".format(oxy_rate*c02_rate))




if __name__ == "__main__":
    p1()
