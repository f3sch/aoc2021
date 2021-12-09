#!/bin/python3

import sys


def lowPoint(map, row, col):
    elem = map[row][col]
    if map[row][col-1] > elem and map[row][col+1] > elem and map[row-1][col] > elem and map[row+1][col] > elem:
        return True
    return False

def p1():
    if len(sys.argv) != 2:
        print("File")
        exit(-1)

    caves = []
    with open(sys.argv[1]) as f:
        for line in f:
            caves.append([int(s) for s in line.strip()])

    # Add padding for easier search
    rows = len(caves) + 2
    cols = len(caves[0]) + 2
    for s in caves:
        s.insert(0, 9)
        s.append(9)

    caves.append([9 for _ in range(cols)])
    caves.insert(0, [9 for _ in range(cols)])

    nLow = 0
    nRisk = 0
    for row in range(1, rows -1):
        for col in range(1, cols -1):
            if lowPoint(caves, row, col):
                # print("---------")
                # print(row, col, " -> ", caves[row][col])
                # print(caves[row][col-1], caves[row][col+1], caves[row-1][col], caves[row+1][col])
                nLow += 1
                nRisk += 1 + caves[row][col]

    print(nLow)
    print(nRisk)



if __name__ == "__main__":
    p1()
