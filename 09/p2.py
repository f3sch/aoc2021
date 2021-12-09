#!/bin/python3

import sys


def lowPoint(map, row, col):
    elem = map[row][col]
    if map[row][col-1] > elem and map[row][col+1] > elem and map[row-1][col] > elem and map[row+1][col] > elem:
        return True
    return False

def searchPoint(map, basin, index, done, todo, point):
    rows = len(map)
    cols = len(map[0])
    #check if point is already in done
    if not point in done:
        done.append(point)
        basin[index].append(point)
    #goto the left
    for row in reversed(range(0,point[0])):
        if not [row, point[1]] in done:
            if map[row][ point[1]] != 9:
                todo.append([row, point[1]])
                basin[index].append([row, point[1]])
            else:
                break
    #goto the right
    for row in range(point[0]+1, rows):
        if not [row, point[1]] in done:
            if map[row][ point[1]] != 9:
                todo.append([row, point[1]])
                basin[index].append([row, point[1]])
            else:
                break

    #go down
    for col in range(point[1]+1, cols):
        if not [point[0], col] in done:
            if map[point[0]][ col] != 9:
                todo.append([point[0], col])
                basin[index].append([point[0], col])
            else:
                break
    #go up
    for col in reversed(range(0, point[1])):
        if not [point[0], col] in done:
            if map[point[0]][col] != 9:
                todo.append([point[0], col])
                basin[index].append([point[0], col])
            else:
                break



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

    seed = []
    for row in range(1, rows -1):
        for col in range(1, cols -1):
            if lowPoint(caves, row, col):
                seed.append([row,col])

    basins =  []
    for i,se in enumerate(seed):
            done = []
            todo = []
            basins.append([])
            searchPoint(caves, basins, i, done, todo, se)
            for to in todo:
                searchPoint(caves, basins, i, done, todo, to)

    nbasins = []
    #make entries unique
    for i,basin in enumerate(basins):
        nbasins.append([])
        for point in basin:
            if point in nbasins[i]:
                continue
            else:
                nbasins[i].append(point)

    basins = nbasins

    # print(basins)
    for i,se in enumerate(seed):
        print(i,se, " : ", basins[i])

    nsize = []
    for size in [len(basin) for basin in basins]:
        nsize.append(size)

    nsize.sort()


    print(nsize[-1]*nsize[-2]*nsize[-3])







if __name__ == "__main__":
    p1()
