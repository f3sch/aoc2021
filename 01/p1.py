#!/bin/python3

import sys


def p1():
    if len(sys.argv) != 2:
        print("File")
        exit(-1)

    depths = []
    with open(sys.argv[1]) as f:
        for line in f:
            depths.append(int(line))

    inc = 0
    for i in range(len(depths) - 1 ):
        if depths[i] < depths[i+1]:
            inc += 1

    print(inc)


if __name__ == "__main__":
    p1()
