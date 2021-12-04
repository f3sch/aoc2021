#!/bin/python3

import sys


def p1():
    if len(sys.argv) != 2:
        print("File")
        exit(-1)

    binaryN = []
    with open(sys.argv[1]) as f:
        for line in f:
            binaryN.append(line)

    count1 = [0 for _ in range(12)]
    count0 = [0 for _ in range(12)]

    for bin in binaryN:
        for i in range(12):
            if bin[i] == "1":
                count1[i] += 1
            elif bin[i] == "0":
                count0[i] += 1
            else:
                continue

    gamma_str = ""
    epsilon_str = ""
    for i in range(12):
        if count1[i] > count0[i]:
            gamma_str += "1"
        else:
            gamma_str += "0"

    gamma_rate = int(gamma_str, 2)
    for bit in gamma_str:
        if bit == "1":
            epsilon_str += "0"
        else:
            epsilon_str += "1"

    epsilon_rate = int(epsilon_str, 2)
    

    print("Gamma rate: {}".format(gamma_rate))
    print("Epsilon rate: {}".format(epsilon_rate))
    print("Power consumption: {}".format(gamma_rate*epsilon_rate))




if __name__ == "__main__":
    p1()
