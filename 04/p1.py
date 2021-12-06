#!/bin/python3

import sys

def cRow(row):
    if sum(row) == 5:
        return 1
    return 0

def cCol(board, col):
    sum = 0
    for row in board:
        sum += row[col]
    if sum == 5:
        return 1
    return 0


def cBoard(board):
    for row in board:
        if cRow(row) == 1:
            return 1
    for i in range(5):
        if cCol(board, i) == 1:
            return 1
    return 0


def p1():
    if len(sys.argv) != 2:
        print("File")
        exit(-1)

    draws = []
    boards = []
    bindex = -1
    first = 0
    winner = -1
    rdraw = -1
    with open(sys.argv[1]) as f:
        for line in f:
            if first == 0:
                draws = line.strip().split(',')
                first = 1
                continue

            elif len(line.strip()) == 0:
                bindex +=1
                boards.append([])
                continue

            boards[bindex].append(line.strip().split())

    sboards = [[[0,0,0,0,0] for _ in range(5)] for _ in range(len(boards))]

    # start draw
    for k, draw in enumerate(draws):
        for i, board in enumerate(boards):
            for r,row in enumerate(board):
                for c,col_j in enumerate(row):
                    if col_j == draw:
                        sboards[i][r][c] = 1

            if cBoard(sboards[i]) == 1:
                winner = i
                rdraw = k
                break

        if winner >= 0:
            break


    sum = 0
    for k, row in enumerate(boards[winner]):
        for l, col in enumerate(row):
            if sboards[winner][k][l] != 1:
                sum += int(col)

    print(int(draws[rdraw])*sum)







if __name__ == "__main__":
    p1()
