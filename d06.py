## DAY 6
file = "d6.txt"
with open(file) as f:
    data = f.read().rstrip()
    
splitdata = data.split('\n\n')

count = 0
count_part1 = 0
for line in splitdata:
    oneline = line.replace('\n', '')
    count_part1 += len(set(oneline))
    line = line.split('\n')
    yesgroup = []
    for person in line:
        yesgroup.append(set(person))
    count += len(set.intersection(*yesgroup))
    
print(count_part1, count)
        
    
