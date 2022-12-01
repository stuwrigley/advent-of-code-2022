#!/usr/bin/python3
import numpy as np

totals=[]

with open('01_input.txt') as f:
    lines = [line.rstrip() for line in f]

#part 1
total=0
for line in lines:
    if not line:
        totals.append(total)
        total=0
    else:
        total+=int(line)
totals.append(total)
print("Part 1 answer:",max(totals))

#part 2
print("Part 2 answer:",sum(np.sort(totals)[-3:]))
