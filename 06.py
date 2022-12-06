#!/usr/bin/python3

with open('06_input.txt') as f:
    line = f.readline().strip()

def uniqueBlockPosition(data,blockSize):
    position=blockSize
    while True:
        marker=line[position-blockSize:position]
        if len(marker)==len(set(marker)):
            return position
        position+=1

#part 1
print("Part 1 answer:",uniqueBlockPosition(line,4))

#part 2
print("Part 2 answer:",uniqueBlockPosition(line,14))
