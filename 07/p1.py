#!/bin/python3

import sys
import numpy as np

def p1():
    if len(sys.argv) != 2:
        print("File")
        exit(-1)

    pos = []
    with open(sys.argv[1]) as f:
        for line in f:
            for num in line.strip().split(','):
                pos.append(int(num))

    pos.sort()
    mid = np.median(np.array(pos))

    print(mid)

    sum = 0
    for i in pos:
        sum += abs(i-mid)

    print(sum)





if __name__ == "__main__":
    p1()
