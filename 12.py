#!/usr/bin/python3
import numpy as np
from collections import deque

with open('12_input.txt') as f:
    lines = [line.rstrip() for line in f]

grid=[]
for line in lines:
    grid.append([ord(x)-97 for x in line])
grid=np.array(grid)

sLoc=np.where(grid == ord('S')-97)
start=list(zip(sLoc[0], sLoc[1]))[0]
eLoc=np.where(grid == ord('E')-97)
end=list(zip(eLoc[0], eLoc[1]))[0]
grid[grid==ord('S')-97]=ord('a')-97
grid[grid==ord('E')-97]=ord('z')-97

ALLOWED_TRANSITIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def validPos(grid,pos,curVal):
    if (pos[0]<0 or pos[1]<0 or pos[0]>=grid.shape[0] or pos[1]>=grid.shape[1]):
        return False
    return grid[pos[0]][pos[1]]<=curVal+1

def findPath(grid,posArray):
    queue=deque((pos,0) for pos in posArray)
    visited=set(posArray)
    while queue:
        curPos, stepCount = queue.popleft()
        if curPos==end:
            return stepCount
        curVal=grid[curPos[0]][curPos[1]]
        for offset_row, offset_col in ALLOWED_TRANSITIONS:
            nextPos=(curPos[0]+offset_row, curPos[1]+offset_col)
            if nextPos not in visited and validPos(grid,nextPos,curVal):
                visited.add(nextPos)
                queue.append((nextPos, stepCount+1))

#part 1
pathLength=findPath(grid,[start])
print("Part 1 answer:",pathLength)

#part 2
sLoc=np.where(grid==0)
allStarts=list(zip(sLoc[0], sLoc[1]))
pathLength=findPath(grid,allStarts)
print("Part 2 answer:",pathLength)
