#!/usr/bin/python3
import copy
from collections import deque

TEST=False

if TEST:
   with open('17_input_test.txt') as f:
       windDirection = [line.rstrip() for line in f]
else:
   with open('17_input.txt') as f:
    windDirection = [line.rstrip() for line in f]

windDirection=windDirection[0]
windShiftAmount={'<':-1,'>':1}

CHAMBER_WIDTH=7
chamber=[]
chamber.append([0,0,0,0,0,0,0])
maxHeight=0

PART1_ROCKS=2022
PART2_ROCKS=1000000000000

rocks=[]
rocks.append([[2,0],[3,0],[4,0],[5,0]])
rocks.append([[3,0],[2,1],[3,1],[4,1],[3,2]])
rocks.append([[2,0],[3,0],[4,0],[4,1],[4,2]])
rocks.append([[2,0],[2,1],[2,2],[2,3]])
rocks.append([[2,0],[3,0],[2,1],[3,1]])

def leftEdge(rock):
   return min([x[0] for x in rock])

def rightEdge(rock):
   return max([x[0] for x in rock])

def shiftRockSideways(rock,shift,leftChamberEdge,rightChamberEdge,settledRocks):
   shiftAllowed=True
   shiftAllowed=shiftAllowed and not (shift>0 and rightEdge(rock)+shift>rightChamberEdge)
   shiftAllowed=shiftAllowed and not (shift<0 and leftEdge(rock)+shift<leftChamberEdge)
   for block in rock:
      shiftAllowed=shiftAllowed and not (block[0]+shift,block[1]) in settledRocks
   
   if shiftAllowed:
      for block in rock:
         block[0]+=shift
      
def shiftRockUpDown(rock,shift):
   for block in rock:
      block[1]+=shift

def printCavern(settledRocks,rock,height):
   for y in range(height,-1,-1):
      str="|"
      for x in range(CHAMBER_WIDTH):
         if ((x,y) in settledRocks):
            str+="#"
         elif ([x,y] in rock):
            str+="@"
         else:
            str+="."
      print(str+"|")
   print("+-------+")         

rockCount=0
windIndex=0
heighestRock=-1
settledRocks=set()
for x in range(CHAMBER_WIDTH):
   settledRocks.add((x,heighestRock))

lastH=0

#buffers for spotting periodicity
bufferSize=2000
considerFrom=bufferSize*10
lastDeltas=deque()
firstTotals=[]
snapshot=[]
periodicity=0
eachPeriodAdds=0
prevHighest=0
periodSize=0
prevPeriodCount=0

while rockCount<PART2_ROCKS:
   rockID=rockCount%len(rocks)
   rock=copy.deepcopy(rocks[rockID])  # bad performance

   shiftRockUpDown(rock,heighestRock+3+1)

   settled=False
   while not settled:
      # wind blows
      windShift=windShiftAmount[windDirection[windIndex]]
      shiftRockSideways(rock,windShift,0,CHAMBER_WIDTH-1,settledRocks)

      # rock drops
      shiftRockUpDown(rock,-1)
      
      for block in rock:
         settled = settled or (block[0],block[1]) in settledRocks
      if settled:
         shiftRockUpDown(rock,+1)
         for block in rock:
            settledRocks.add((block[0],block[1]))
         lastH=heighestRock
         heighestRock=max(heighestRock,block[1])

      windIndex+=1
      if windIndex>=len(windDirection):
         windIndex=0

   rockCount+=1

   # store deltas and compare against history to spot periodic behaviour   
   if len(firstTotals)<bufferSize:
      firstTotals.append(heighestRock+1)
   lastDeltas.append(heighestRock+1-lastH)
   if len(lastDeltas)>bufferSize:
      lastDeltas.popleft()
   if rockCount==considerFrom:   # once we have a block sufficiently distant from the messyt first period, copy is and use for comparisons
      snapshot=lastDeltas.copy()
   if rockCount>considerFrom:  # first period is messy so need to look for later ones. First period is used for partial period look up
      if lastDeltas==snapshot:  # if the patterns match, we've spotted periodicity
         periodSize=rockCount-prevPeriodCount
         eachPeriodAdds=heighestRock+1 - prevHighest
         prevHighest=heighestRock+1
         prevPeriodCount=rockCount
   
   if rockCount>100000: # once we've seen enough to figure out the periodicity, we can stop
      break  
   if rockCount==PART1_ROCKS:
      print("Part 1 answer:",heighestRock+1)

#part 2
print("Part 2 answer:",(PART2_ROCKS//periodSize)*eachPeriodAdds + firstTotals[PART2_ROCKS%periodSize-1])
