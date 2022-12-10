#!/usr/bin/python3
import numpy as np

with open('10_input.txt') as f:
    lines = [line.rstrip() for line in f]

def render(crt):
    for row in range(len(crt)):
        line=""
        for col in range(len(crt[0])):
            if crt[row][col]==1:
                line+="#"
            else:
                line+="."
        print(line)
    

signalStrengthPoints=range(20,221,40)
signalStrengthTotal=0
reg=1
opCount=0

rows=6
cols=40
crt=np.zeros((rows,cols))


for op in lines:
    if op=="noop":
        wait=1
        inc=0
    else:
        wait=2
        inc=int(op.split()[1])
    for delay in range(wait):
        opCount+=1

        currentRow=(opCount-1)//cols
        currentCol=(opCount-1)%cols
        if reg-1<=currentCol<=reg+1:
            crt[currentRow][currentCol]=1

        if opCount in signalStrengthPoints:
            signalStrengthTotal+=opCount*reg
        if delay==wait-1:
            reg+=inc

print("Part 1 answer:",signalStrengthTotal)
print("Part 2 answer:")
render(crt)





