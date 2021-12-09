#!/bin/python3

import sys


r1 = "cf"
r4 = "bcdf"
r7= "acf"
r8 = "abcdefg"

dic = {1:r1,4:r4,7:r7,8:r8}


def p1():
    if len(sys.argv) != 2:
        print("File")
        exit(-1)

    numbers = {}
    with open(sys.argv[1]) as f:
        for i,line in enumerate(f):
            numbers[i] = ["".join(sorted(sub)) for sub in line.strip().replace('|' , '').split()]

    

    for v in numbers.values():
        input = v[:10]
        output = v[10:]

        trans = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
        skip = [0 for _ in range(len(input))]

        #Find 1,4,7,8
        for i,inp in enumerate(input):
            if len(inp) == 2:
                trans[1] = inp
            elif len(inp) == 4:
                trans[4] = inp
            elif len(inp) == 3:
                trans[7] = inp
            elif len(inp) == 7:
                trans[8] = inp
            else:
                skip[i] = 1

        print(trans)

        #Find 3,9,6
        for i,inp in enumerate(input):
            if skip[i] == 1:
                #3
                if trans[1] in inp and len(inp) == 5:
                    trans[3] = inp
                    skip[i] = 0
                #6
                elif not trans[1] in inp and len(inp) == 6:
                    trans[6] = inp
                    skip[i] = 0
                #9
                elif trans[4] in inp and len(inp) == 6:
                    trans[9] = inp
                    skip[i] = 0


        print(trans)

        #Find missing b
        c = [0 for _ in range(6)]

        for k,i in enumerate(list(trans[3])):
            for j in list(trans[3]):
                if i == j:
                    c[k] = 1

        b = ""
        for k,i in enumerate(trans[9]):
             if c[k] == 0:
                 b = trans[9][k]

        print(trans)
        print(b)
        #Find 2,5
        for i,inp in enumerate(input):
            if skip[i] == 1:
                #5
                if not trans[1] in inp and len(inp) == 5 and b in inp:
                    trans[5] = inp
                    skip[i] = 0
                elif not trans[1] in inp and len(inp) == 5 and not b in inp:
                    trans[2] = inp
                    skip[i] = 0

        print(trans)

        for i,inp in enumerate(input):
            if skip[i] == 1:
                trans[0] = inp

        print(trans)
        out =  []
        for o in output:
            for k,v in trans.items():
                if v == o:
                    out.append(k)

        print(out)





if __name__ == "__main__":
    p1()
