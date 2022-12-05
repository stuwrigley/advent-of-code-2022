#!/usr/bin/python3

with open('05_input.txt') as f:
    lines = f.readlines()


def buildStacks(data):
    numStacks=0
    maxHeight=0
    for line in lines:
        if line.strip()[0].isdigit():
            numStacks=int(line.strip().split()[-1])
            break
        maxHeight+=1
    stack=[ [] for _ in range(numStacks) ]
    for row in reversed(lines[0:maxHeight]):
        for crateid in range(numStacks):
            if row[crateid*4+1].isalpha():
                stack[crateid].append(row[crateid*4+1])
    return stack

def moveCratesIndividually(stack,data):
    for line in lines:
        if line[0]=='m':
            parts=line.split()
            for move in range(int(parts[1])):
                stack[int(parts[5])-1].append(stack[int(parts[3])-1].pop())

def moveCratesAsBlock(stack,data):
    for line in lines:
        if line[0]=='m':
            parts=line.split()
            block=stack[int(parts[3])-1][-int(parts[1]):]
            for crate in block:
                stack[int(parts[5])-1].append(crate)
                stack[int(parts[3])-1].pop()

def getTopCrates(stack):
    topCrates=''
    for s in stack:
        topCrates+=(s[-1])
    return topCrates


#part 1
stack=buildStacks(lines)
moveCratesIndividually(stack,lines)
print("Part 1 answer:",getTopCrates(stack))

#part 2
stack=buildStacks(lines)
moveCratesAsBlock(stack,lines)
print("Part 2 answer:",getTopCrates(stack))
