file = "d1.txt"
with open(file) as f:
    lines = [int(line.rstrip()) for line in f]
        
sortedlines = sorted(lines)
for i in range(len(sortedlines)):
    l, r = i+1, len(sortedlines)-1
    while l < r:
        s = sortedlines[i] + sortedlines[l] + sortedlines[r]
        if s < 2020:
            l += 1
        elif s > 2020:
            r -= 1
        else:
            print([sortedlines[i], sortedlines[l], sortedlines[r]])
            break
            
