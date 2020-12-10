## DAY 3
file = "d3.txt"
with open(file) as f:
    lines = [line.rstrip() for line in f]

width = len(lines[0])

steps = [(1,3), (1, 1), (1, 5), (1, 7), (2,1)]
counts = []
for rowstep, colstep in steps:
    count = 0
    for i in range(0, len(lines) // rowstep):
        row, col = i*rowstep, (i*colstep % width)
        if lines[row][col] == '#':
            count += 1
    counts.append(count)
    

import math
print(counts[0], math.prod(counts))
