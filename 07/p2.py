#!/bin/python3

import sys
import numpy as np

def fuel(start, end):
    change = end - start
    return sum([i for i in range(1, change+1)])

def p1():
    if len(sys.argv) != 2:
        print("File")
        exit(-1)

    pos = []
    with open(sys.argv[1]) as f:
        for line in f:
            for num in line.strip().split(','):
                pos.append(int(num))

    check = [i for i in range(np.min(pos), np.max(pos)+1)]
    res = []

    for posb in check:
        sum_fuel = 0
        for crab in pos:
            mi = np.min([crab, posb])
            ma = np.max([crab, posb])
            sum_fuel += fuel(mi, ma)
            # print("... {} -> {} from {} to {}".format(crab, fuel(mi, ma), mi, ma))
        res.append(sum_fuel)

    # print("Fuel:")
    # for i,fue in enumerate(res):
    #     print(check[i], fue)

    min = np.min(res)
    min_pos = [i for i,x in enumerate(res) if x == min]

    for i in min_pos:
        print(res[i], i)



if __name__ == "__main__":
    p1()
