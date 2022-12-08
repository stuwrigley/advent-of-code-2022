#!/usr/bin/python3
import numpy as np

grid=[]
with open('08_input.txt') as f:
    lines = [line.rstrip() for line in f]

for line in lines:
    grid.append([int(x) for x in line])
grid=np.array(grid)
rows, cols = grid.shape

#part 1
visible=np.zeros_like(grid)
for row in range(rows):
    prevHeight=-1
    for col in range(cols):
        if grid[row][col]>prevHeight:
            visible[row][col]=1
            prevHeight=grid[row][col]
    prevHeight=-1
    for col in range(cols-1,-1,-1):
        if grid[row][col]>prevHeight:
            visible[row][col]=1
            prevHeight=grid[row][col]
for col in range(cols):
    prevHeight=-1
    for row in range(rows):
        if grid[row][col]>prevHeight:
            visible[row][col]=1
            prevHeight=grid[row][col]
    prevHeight=-1
    for row in range(rows-1,-1,-1):
        if grid[row][col]>prevHeight:
            visible[row][col]=1
            prevHeight=grid[row][col]

print("Part 1 answer:",sum(sum(visible)))

#part 2
view=np.zeros_like(grid)
for row in range(1,rows-1):
    for col in range(1,cols-1):
        viewscore=[0,0,0,0]
        for rinc in range(row+1,rows):
            viewscore[0]+=1
            if grid[rinc][col]>=grid[row][col]:
                break
        for rinc in range(row-1,-1,-1):
            viewscore[1]+=1
            if grid[rinc][col]>=grid[row][col]:
                break
        for cinc in range(col+1,cols):
            viewscore[2]+=1
            if grid[row][cinc]>=grid[row][col]:
                break
        for cinc in range(col-1,-1,-1):
            viewscore[3]+=1
            if grid[row][cinc]>=grid[row][col]:
                break
        view[row][col]=np.prod(viewscore)

print("Part 2 answer:",np.max(view))
