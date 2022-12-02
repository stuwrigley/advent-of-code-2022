#!/usr/bin/python3
import numpy as np
from collections import defaultdict

with open('02_input.txt') as f:
    lines = [line.rstrip() for line in f]

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# Opponent: A for Rock, B for Paper, and C for Scissors

#part 1
# X for Rock, Y for Paper, and Z for Scissors
def part1_def_value():
    return 3
outcomeDict = defaultdict(part1_def_value)
outcomeDict["A Z"]=0
outcomeDict["B X"]=0
outcomeDict["C Y"]=0
outcomeDict["A Y"]=6
outcomeDict["B Z"]=6
outcomeDict["C X"]=6

# 1 for Rock, 2 for Paper, and 3 for Scissors
playDict={"X":1,"Y":2,"Z":3}

score=0
for line in lines:
    score+=playDict[line[-1]]+outcomeDict[line]
print("Part 1 answer:",score)

#part 2
outcomeDict={"X":0,"Y":3,"Z":6}
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
playDict={"A X":3,"A Y":1,"A Z":2,"B X":1,"B Y":2,"B Z":3,"C X":2,"C Y":3,"C Z":1}

score=0
for line in lines:
    score+=playDict[line]+outcomeDict[line[-1]]
print("Part 2 answer:",score)
