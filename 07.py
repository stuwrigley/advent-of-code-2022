#!/usr/bin/python3

with open('07_input.txt') as f:
    lines = [line.rstrip() for line in f]

minSize=8381165 #test
minSize=913445 #real

#part 1 & 2
depth=-1
filesizes=[]
runningTotal=0
targetDirSize=70000000
for cmd in lines:
    cmdParts=cmd.split()
    if cmdParts[1]=="cd" and cmdParts[2]=="..":
        filesizes[depth-1]+=filesizes[depth]
        if filesizes[depth]<=100000:
            runningTotal+=filesizes[depth]
        if filesizes[depth]>=minSize and filesizes[depth]<targetDirSize:
            targetDirSize=filesizes[depth]
        filesizes.pop()
        depth-=1
    elif cmdParts[1]=="cd":
        depth+=1
        filesizes.append(0)
    elif cmdParts[0].isdigit():
        filesizes[depth]+=int(cmdParts[0])
while True:
    if depth==0:
        print("Total disk usage:",filesizes[depth])
        print("Smallest deletion:",30000000-(70000000-filesizes[depth]))
        break
    filesizes[depth-1]+=filesizes[depth]
    filesizes.pop()
    depth-=1

print("Part 1 answer:",runningTotal)
print("Part 2 answer:",targetDirSize)
