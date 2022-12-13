#!/usr/bin/python3
from functools import cmp_to_key

with open('13_input.txt') as f:
    lines = [line.rstrip() for line in f]

#parse input
numPairs=int((len(lines)+1)/3)
pairs=[]
for p in range(numPairs):
    pairs.append([eval(lines[p*3]),eval(lines[p*3+1])])


def correctOrder(left,right):
    for itemID in range(max(len(left),len(right))):
        correct=0
        if itemID>=len(left):
            return -1
        if itemID>=len(right):
            return 1
        if type(left[itemID]) is not list and type(right[itemID]) is not list:  # both integers
            if left[itemID]<right[itemID]:
                return -1
            elif left[itemID]>right[itemID]:
                return 1
        elif type(left[itemID]) is  list and type(right[itemID]) is  list:  # both lists
            correct=correctOrder(left[itemID],right[itemID])
        else:  # only one is a list
            if type(left[itemID]) is not list:
                correct=correctOrder([left[itemID]],right[itemID])
            else:
                correct=correctOrder(left[itemID],[right[itemID]])
        if correct!=0:
            return correct
    return 0


#part 1
correctPairs=[]
for pairID in range(numPairs):
    if correctOrder(pairs[pairID][0],pairs[pairID][1])==-1:
        correctPairs.append(pairID+1)
print("Part 1 answer:",sum(correctPairs))

#part 2
dividerPackets=[[[2]],[[6]]]
packets=[]
for pair in pairs:
    packets.append(pair[0])
    packets.append(pair[1])
for divider in dividerPackets:
    packets.append(divider)

packets=sorted(packets, key=cmp_to_key(correctOrder))

decoderKey=1
for divider in dividerPackets:
    decoderKey=decoderKey*(packets.index(divider)+1)

print("Part 2 answer:",decoderKey)
