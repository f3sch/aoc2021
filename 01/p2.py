#!/bin/python3

import sys


def p2():
    if len(sys.argv) != 2:
        print("File")
        exit(-1)

    depths = []
    with open(sys.argv[1]) as f:
        for line in f:
            depths.append(int(line))

    inc = 0
    for i in range(len(depths) - 3 ):
        a = depths[i] + depths[i+1] + depths[i+2]
        b = depths[i + 1] + depths[i+2] + depths[i+3]
        if a < b:
            inc += 1

    print(inc)


if __name__ == "__main__":
    p2()
