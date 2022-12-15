#!/usr/bin/python3
import shapely
from shapely import geometry, ops
from numpy.random import permutation

MAX_X=200000000
MIN_X=-200000000

TEST=False

if TEST:
   with open('15_input_test.txt') as f:
       lines = [line.rstrip() for line in f]
else:
   with open('15_input.txt') as f:
    lines = [line.rstrip() for line in f]


sensors=[]
for line in lines:
   loc=(int(line.split(":")[0].split("=")[1].split(",")[0]),int(line.split(":")[0].split("=")[2].split(",")[0]))
   beacon=(int(line.split(":")[1].split("=")[1].split(",")[0]),int(line.split(":")[1].split("=")[2].split(",")[0]))
   sensors.append([loc,beacon])

beacons=[]
for sensor in sensors:
   beacons.append((sensor[1][0],sensor[1][1]))

def manhattanDistance(loc1,loc2):
   return abs(loc1[0]-loc2[0])+abs(loc1[1]-loc2[1])

def distanceBetweenSensorAndBeacon(sensor):
   return manhattanDistance(sensor[0],sensor[1])

def intersectionPoints(sensor,row):
   distance=distanceBetweenSensorAndBeacon(sensor)
   polygon = [(sensor[0][0], sensor[0][1]-distance), (sensor[0][0]-distance, sensor[0][1]), (sensor[0][0], sensor[0][1]+distance), (sensor[0][0]+distance, sensor[0][1])]  # build this from sensor distance
   shapely_poly = shapely.geometry.Polygon(polygon)
   shapely_line = shapely.geometry.LineString([(MIN_X,row),(MAX_X,row)])
   return list(shapely_poly.intersection(shapely_line).coords)

def pointsCovered(sensors,yaxis):
   pointsCovered=set()
   for sensor in sensors:
      ip=intersectionPoints(sensor,yaxis)
      if len(ip)>0:  # sensor area covers line
         if len(ip)==1:
            if ip[0] not in beacons:
               pointsCovered.add(int(ip[0][0]))
         else:
            for x in range(int(ip[0][0]),int(ip[1][0])+1):
               if (x,yaxis) not in beacons:
                  pointsCovered.add(x)
   return pointsCovered



#part 1
if TEST:
   yaxis=10
else:
   yaxis=2000000
covered=pointsCovered(sensors,yaxis)
print("Part 1 answer:",len(covered))

#part 2
tuningFreq=0
minSearchX=0
minSearchY=0
if TEST:
   maxSearchX=20
   maxSearchY=20
else:
   maxSearchX=4000000
   maxSearchY=4000000


def tuningFrequency(loc):
   return loc[0]*4000000 + loc[1]

def pointBeyondAllSensors(loc):
   for sensor in sensors:
      if manhattanDistance(loc,sensor[0])<=distanceBetweenSensorAndBeacon(sensor):
         return False
   return True

def findPointBeyondPerimeter(sensors):
   for sensor in sensors:
      distance=distanceBetweenSensorAndBeacon(sensor)
      for deltax in range(distance+2):
         deltay=(distance+1)-deltax
         for signx,signy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            x = sensor[0][0]+(deltax*signx)
            y = sensor[0][1]+(deltay*signy)
            if not(0<=x<=maxSearchX and 0<=y<=maxSearchY):
                continue
            if pointBeyondAllSensors([x,y]):
               return [x, y]


print("Part 2 answer:",tuningFrequency(findPointBeyondPerimeter(sensors)))
