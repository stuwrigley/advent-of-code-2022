#!/usr/bin/python3
import re
import math
import numpy as np

with open('11_input.txt') as f:
    lines = [line.rstrip() for line in f]

def showItems(monkeys):
    for mid in range(len(monkeys)):
        print("Monkey",mid,":",monkeys[mid]['items'])

def showNumItemsInspected(monkeys):
    for mid in range(len(monkeys)):
        print("Monkey",mid,"inspected items",monkeys[mid]['itemsInspected'],"times.")

DO_PART1 = False

#parse input
numMonkeys=int((len(lines)+1)/7)
monkey=[]
for monkeyID in range(numMonkeys):
    offset=monkeyID*7
    items=[int(x) for x in re.split(', | ',lines[offset+1].strip())[2:]]
    op=lines[offset+2].strip().split('=')[1].strip()
    div=int(lines[offset+3].strip().split()[3])
    testTrue=int(lines[offset+4].strip().split()[5])
    testFalse=int(lines[offset+5].strip().split()[5])
    monkey.append({"items":items,"op":op,"div":div,"testTrue":testTrue,"testFalse":testFalse,"itemsInspected":0})

if DO_PART1:
    #part 1
    for round in range(20):
        for monkeyID in range(numMonkeys):
            for old in monkey[monkeyID]['items']:
                newWorryLevel=math.floor(eval(monkey[monkeyID]['op'])/3)
                if newWorryLevel%monkey[monkeyID]['div']==0:
                    monkey[monkey[monkeyID]['testTrue']]['items'].append(newWorryLevel)
                else:
                    monkey[monkey[monkeyID]['testFalse']]['items'].append(newWorryLevel)
                monkey[monkeyID]['itemsInspected']+=1
            monkey[monkeyID]['items']=[]

else:
    #part 2
    divisors=[]
    for m in monkey:
        divisors.append(m['div'])
    supermodulo=np.prod(sorted(divisors))

    
    for round in range(10000):
        for monkeyID in range(numMonkeys):
            for old in monkey[monkeyID]['items']:
                #newWorryLevel=math.floor(eval(monkey[monkeyID]['op'])/3)
                newWorryLevel=eval(monkey[monkeyID]['op'])%supermodulo
                if newWorryLevel%monkey[monkeyID]['div']==0:
                    monkey[monkey[monkeyID]['testTrue']]['items'].append(newWorryLevel)
                else:
                    monkey[monkey[monkeyID]['testFalse']]['items'].append(newWorryLevel)
                monkey[monkeyID]['itemsInspected']+=1
            monkey[monkeyID]['items']=[]
        if round==0 or round==19 or (round+1)%1000==0:
            print("== After round",round+1,"==")
            showNumItemsInspected(monkey)
            print("")
        

inspectionTotals=[]
for m in monkey:
    inspectionTotals.append(m['itemsInspected'])
monkeyBusiness=np.prod(sorted(inspectionTotals)[-2:])
print("Part","1" if DO_PART1 else "2","answer:",monkeyBusiness)





