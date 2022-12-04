#!/usr/bin/python3
import re

with open('04_input.txt') as f:
    lines = [line.rstrip() for line in f]

def partialOverlap(a,b):
    return a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]

def fullOverlap(a,b):
    return (a[0] <= b[0] <= a[1] and a[0] <= b[1] <= a[1]) or (b[0] <= a[0] <= b[1] and b[0] <= a[1] <= b[1])

part1Count=0
part2Count=0
for line in lines:
    lims=[int(i) for i in re.split(',|-|\*|\n',line)]
    part1Count+=fullOverlap([lims[0],lims[1]],[lims[2],lims[3]])
    part2Count+=partialOverlap([lims[0],lims[1]],[lims[2],lims[3]])
print("Part 1 answer:",part1Count)
print("Part 2 answer:",part2Count)
