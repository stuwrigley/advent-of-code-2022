#!/usr/bin/python3

with open('03_input.txt') as f:
    lines = [line.rstrip() for line in f]


#part 1

def getPriority(ch):
    if ch.isupper():
        return ord(ch) - 38
    else:
        return ord(ch) - 96

score=0
for line in lines:
    midPoint=int(len(line)/2)
    overlap=set(line[:midPoint]).intersection(set(line[midPoint:]))
    for ch in overlap:
        score+=getPriority(ch)
print("Part 1 answer:",score)

#part 2

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

score=0
for group in divide_chunks(lines, 3):
    overlap=set(group[0]).intersection(set(group[1]).intersection(set(group[2])))
    for ch in overlap:
        score+=getPriority(ch)
print("Part 2 answer:",score)
