#!/usr/bin/python3
from collections import defaultdict
import math

TEST=False

if TEST:
   with open('16_input_test.txt') as f:
       lines = [line.rstrip() for line in f]
else:
   with open('16_input.txt') as f:
    lines = [line.rstrip() for line in f]

#parse input
valveRates={}
distances = defaultdict(lambda: defaultdict(lambda: math.inf)) # distance from one valve to another
for line in lines:
   parts=line.split()
   thisValve=parts[1]
   valveRates[thisValve]=int(parts[4].split("=")[1].split(";")[0])
   tunnels=[]
   distances[thisValve][thisValve]=0
   for tunnel in parts[9:]:
      toValve=tunnel.split(",")[0]
      tunnels.append(toValve)
      distances[thisValve][toValve]=1

#add two-step traversals 
for k in valveRates:
   for i in valveRates:
      for j in valveRates:
         distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])


# recursive implementation of Depth-first search (DFS) - https://en.wikipedia.org/wiki/Depth-first_search
def traverseGraph(currentValve,timeLeft,unopenedValves):
   currentPathPressureReleased = 0
   for nextValve in unopenedValves:
      timingRemainingAtNextValve=timeLeft-distances[currentValve][nextValve]-1
      if timingRemainingAtNextValve>=0:
         pressureReleased=valveRates[nextValve] * timingRemainingAtNextValve
         currentPathPressureReleased = max(currentPathPressureReleased,pressureReleased+traverseGraph(nextValve,timingRemainingAtNextValve,unopenedValves-{nextValve}))
   return currentPathPressureReleased

def traverseGraphWithHelp(currentValve,timeLeft,unopenedValves,helper):
   if helper:
      currentPathPressureReleased = traverseGraphWithHelp(start,timeToEscape,unopenedValves,False)
   else:
      currentPathPressureReleased = 0
   for nextValve in unopenedValves:
      timingRemainingAtNextValve=timeLeft-distances[currentValve][nextValve]-1
      if timingRemainingAtNextValve>=0:
         pressureReleased=valveRates[nextValve] * timingRemainingAtNextValve
         currentPathPressureReleased = max(currentPathPressureReleased,pressureReleased+traverseGraphWithHelp(nextValve,timingRemainingAtNextValve,unopenedValves-{nextValve},helper))
   return currentPathPressureReleased



start="AA"
valvesOfInterest={x for x in valveRates if valveRates[x] > 0}  # only consider the ones which will contribute flow

#part 1
timeToEscape=30
releasedPressure=traverseGraph(start,timeToEscape,valvesOfInterest)
print("Part 1 answer:",releasedPressure)

#part 2
timeToEscape=26
releasedPressure=traverseGraphWithHelp(start,timeToEscape,valvesOfInterest,True)
print("Part 2 answer:",releasedPressure)
