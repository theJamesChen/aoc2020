## DAY 12
file = "d12.txt"
with open(file) as f:
    data = f.read().rstrip()

splitdata = data.split('\n')
splitdata = [(i[0],i[1:]) for i in splitdata]
#print(splitdata)

currentd = 'E'
north_south = 0
west_east = 0
compass = ['N', 'E', 'S', 'W']
compass_map = {'N':0, 'E':1, 'S':2, 'W':3}

for moves in splitdata:
    direction, num = moves
    num = int(num)
    if direction == 'F':
        if currentd == 'N':
            north_south += num
        if currentd == 'S':
            north_south -= num
        if currentd == 'E':
            west_east += num
        if currentd == 'W':
            west_east -= num
    elif direction == 'N':
        north_south += num
    elif direction == 'S':
        north_south -= num
    elif direction == 'E':
        west_east += num
    elif direction == 'W':
        west_east -= num
    elif direction == 'L':
        compass_indx = compass_map[currentd]
        currentd = compass[(compass_indx - (num // 90)) % len(compass)]
        #print(currentd)
    elif direction == 'R':
        #print(currentd)
        compass_indx = compass_map[currentd]
        currentd = compass[(compass_indx + (num // 90)) % len(compass)]
        #print(direction, num, currentd, compass_indx, (compass_indx + (num // 90)), (compass_indx + (num // 90)) % len(compass))

print(abs(north_south) + abs(west_east))


currentd = 'E'

north_south = 0
west_east = 0
waypoint_north_south = 1
waypoint_east_west = 10

import math
def rot(x, y, num):
    angle = math.radians(num)
    X = x*math.cos(angle) - y*math.sin(angle)
    Y = y*math.cos(angle) + x*math.sin(angle)
    return [int(round(X)), int(round(Y))]

for moves in splitdata:
    direction, num = moves
    num = int(num)
    if direction == 'F':
            north_south += (num*waypoint_north_south)
            west_east += (num*waypoint_east_west)
    elif direction == 'N':
        waypoint_north_south += num
    elif direction == 'S':
        waypoint_north_south -= num
    elif direction == 'E':
        waypoint_east_west += num
    elif direction == 'W':
        waypoint_east_west -= num
    elif direction == 'L':
        waypoint_east_west, waypoint_north_south = rot(waypoint_east_west, waypoint_north_south, num)
    elif direction == 'R':
        waypoint_east_west, waypoint_north_south = rot(waypoint_east_west, waypoint_north_south, -num)
        
print(abs(north_south) + abs(west_east))



