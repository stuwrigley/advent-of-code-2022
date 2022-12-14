#!/usr/bin/python3
import numpy as np

with open('14_input.txt') as f:
    lines = [line.rstrip() for line in f]

DO_PART1=False

def printCave(cave,extentX,extentY,curSand):
   for y in range(extentY[0],extentY[1]+1):
        str=""
        for x in range(extentX[0],extentX[1]+1):
            if cave[x][y]==1:
                str+="#"
            elif cave[x][y]==2 or (x==curSand[0] and y==curSand[1]):
                str+="o"
            elif x==500 and y==0:
                str+="+"
            else:
                str+="."
        print(str)

def runSandFlow(cave):
    settledCount=0
    withinCave=True
    while withinCave:
        sandPos=[500,0]
        settled=False
        while not settled and withinCave:
            if cave[sandPos[0]][sandPos[1]+1]==0: # air below - so move down
                sandPos=[sandPos[0],sandPos[1]+1]
            elif cave[sandPos[0]][sandPos[1]+1]>0: # rock or sand below
                if cave[sandPos[0]-1][sandPos[1]+1]>0:
                    if cave[sandPos[0]+1][sandPos[1]+1]>0:
                        settled=True
                        settledCount+=1
                        cave[sandPos[0],sandPos[1]]="2"
                    else:
                        sandPos=[sandPos[0]+1,sandPos[1]+1]                
                else:
                    sandPos=[sandPos[0]-1,sandPos[1]+1]
            if sandPos==[500,0]: # source blocked!
                return settledCount
            withinCave = sandPos[1]<=extentY[1] and sandPos[0]>=extentX[0] and sandPos[0]<=extentX[1]
    return settledCount

#parse input
numCols=1000
numRows=200
extentX=[numCols,0]
extentY=[numRows,0]
cave=np.zeros(shape=(numCols, numRows), dtype=np.uint8)
for line in lines:
    nodes=line.split(" -> ")
    for nodeID in range(len(nodes)-1):
        start=[int(x) for x in nodes[nodeID].split(",")]
        end=[int(x) for x in nodes[nodeID+1].split(",")]

        extentX=[min(extentX[0],start[0],end[0]),max(extentX[1],start[0],end[0])]
        extentY=[min(extentY[0],start[1],end[1]),max(extentY[1],start[1],end[1])]
        
        if start[0]==end[0]:
            for y in range(min(start[1],end[1]),max(start[1],end[1])+1):
                cave[start[0]][y]=1
        else:
            for x in range(min(start[0],end[0]),max(start[0],end[0])+1):
                cave[x][start[1]]=1


extentY[0]=0


if DO_PART1:
    #part 1
    printCave(cave,extentX,extentY,[0,0])
    settledCount=runSandFlow(cave)        
    print("Part 1 answer:",settledCount)
else:
    #part 2
    for x in range(numCols):
        cave[x][extentY[1]+2]=1
    extentY[1]=extentY[1]+2
    extentX[0]=0
    extentX[1]=numCols-1
    printCave(cave,extentX,extentY,[0,0])
    settledCount=runSandFlow(cave)
    printCave(cave,extentX,extentY,[0,0])
    print("Part 2 answer:",settledCount)
