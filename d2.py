file = "d2.txt"
with open(file) as f:
    lines = [line.rstrip() for line in f]

valid = 0
for line in lines:
    (ranges, letter, pwd) = line.split()
    low, high = ranges.split('-')
    letter = letter[0]
    
    if (pwd[int(low)-1] == letter) ^ (pwd[int(high)-1] == letter):
        valid +=1
print(valid)
