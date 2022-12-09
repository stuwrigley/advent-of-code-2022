#!/usr/bin/python3

with open('09_input.txt') as f:
    lines = [line.rstrip() for line in f]

def updateTrailingKnot(head,tail):
    xdiff=head[0]-tail[0]
    ydiff=head[1]-tail[1]
    if abs(xdiff)>1 or abs(ydiff)>1:
        if xdiff>0:
            xdiff=xdiff-1
        if xdiff<0:
            xdiff=xdiff+1
        if ydiff>0:
            ydiff=ydiff-1
        if ydiff<0:
            ydiff=ydiff+1
        return (head[0]-xdiff,head[1]-ydiff)
    else:
        return tail

def updateHead(head,cmd):
    if cmd=='R':
        head=(head[0]+1,head[1])
    if cmd=='L':
        head=(head[0]-1,head[1])
    if cmd=='U':
        head=(head[0],head[1]+1)
    if cmd=='D':
        head=(head[0],head[1]-1)
    return head
    


#part 1
head=(0,0)
tail=(0,0)
visited=set()
visited.add(tail)
for line in lines:
    cmd=line.split()
    shift=int(cmd[1])
    for step in range(shift):
        head=updateHead(head,cmd[0])
        tail=updateTrailingKnot(head,tail)
        visited.add(tail)
        

print("Part 1 answer:",len(visited))

#part 2
head=(0,0)
tails=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
visited=set()
visited.add(tail)
for line in lines:
    cmd=line.split()
    shift=int(cmd[1])
    for step in range(shift):
        head=updateHead(head,cmd[0])
        tails[0]=updateTrailingKnot(head,tails[0])
        for tailid in range(1,len(tails)):
            tails[tailid]=updateTrailingKnot(tails[tailid-1],tails[tailid])
        visited.add(tails[-1])
print("Part 2 answer:",len(visited))





