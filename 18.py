#!/usr/bin/python3
from collections import deque

TEST=False

if TEST:
   with open('18_input_test.txt') as f:
      lines = [line.rstrip() for line in f]
else:
   with open('18_input.txt') as f:
      lines = [line.rstrip() for line in f]

#parse input
voxels=[]
for line in lines:
   voxels.append([int(x) for x in line.split(",")])

ADJACENTS=[[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
def numSurfacesNotTouchingAnything(voxel,voxels):
   surfaceArea=6
   for x,y,z in ADJACENTS:
      surfaceArea-=[voxel[0]+x,voxel[1]+y,voxel[2]+z] in voxels
   return surfaceArea

# tried recursion but exceeded depth limit!
def connectedToOutside(voxel,voxels,bounds):
   if voxel in voxels:
      return False
   queue = deque([(voxel[0],voxel[1],voxel[2])])
   seen = set()
   while queue:
      vox=queue.popleft()
      if [vox[0],vox[1],vox[2]] in voxels:
         continue
      if vox in seen:
         continue
      seen.add(vox)
      if vox[0]<bounds[0] or vox[0]>bounds[1] or vox[1]<bounds[2] or vox[1]>bounds[3] or vox[2]<bounds[4] or vox[2]>bounds[5]:  # voxel is beyond the envelope of the boulder
         return True
      if len(seen)>5000:
         return True
      for x,y,z in ADJACENTS:
         nextVoxel=(vox[0]+x,vox[1]+y,vox[2]+z)
         queue.append(nextVoxel)
   return False
      

   
def trappedAir(voxels):
   trapped=[]
   maxX=max([x[0] for x in voxels])
   minX=min([x[0] for x in voxels])
   maxY=max([x[1] for x in voxels])
   minY=min([x[1] for x in voxels])
   maxZ=max([x[2] for x in voxels])
   minZ=min([x[2] for x in voxels])
   boulderBounds=[minX, maxX, minY, maxY, minZ, maxZ]
   for x in range(boulderBounds[0],boulderBounds[1]+1):
      for y in range(boulderBounds[2],boulderBounds[3]+1):
         for z in range(boulderBounds[4],boulderBounds[5]+1):
            if [x,y,z] not in voxels:
               allx=[]
               ally=[]
               allz=[]
               for voxel in voxels:
                  if voxel[1]==y and voxel[2]==z:
                     allx.append(voxel[0])
                  if voxel[0]==x and voxel[2]==z:
                     ally.append(voxel[1])
                  if voxel[0]==x and voxel[1]==y:
                     allz.append(voxel[2])
               if len(allx)==0 or len(ally)==0  or len(allz)==0 :  # outside the boulder
                  continue

               localMaxX=max(allx)
               localMinX=min(allx)
               localMaxY=max(ally)
               localMinY=min(ally)
               localMaxZ=max(allz)
               localMinZ=min(allz)
               
               if localMinX<x<localMaxX and localMinY<y<localMaxY and localMinZ<z<localMaxZ:  # inside the edges (but could still be connected with the outside)
                  if not connectedToOutside([x,y,z],voxels,boulderBounds):
                     trapped.append([x,y,z])
   return trapped

#part 1
totalSurfaceArea=0
for voxel in voxels:
   totalSurfaceArea+=numSurfacesNotTouchingAnything(voxel,voxels)  
print("Part 1 answer:",totalSurfaceArea)

#part 2
trapped=trappedAir(voxels)
totalAirSurfaceArea=0
for airVoxel in trapped:
   totalAirSurfaceArea+=numSurfacesNotTouchingAnything(airVoxel,trapped)
print("Part 2 answer:",totalSurfaceArea-totalAirSurfaceArea)
