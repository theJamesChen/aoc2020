## DAY 10
file = "d10.txt"
with open(file) as f:
    data = f.read().rstrip()

splitdata = data.split('\n')
splitdata = [int(i) for i in splitdata]

splitdata = [0] + splitdata
splitdata.append(max(splitdata)+3)
splitdata.sort()

countones = sum(1 for i in range(1,len(splitdata)) if splitdata[i] - splitdata[i-1] == 3)
countthress = sum(1 for i in range(1,len(splitdata)) if splitdata[i] - splitdata[i-1] == 1)

print(countones*countthress)

counts = [0]*(len(splitdata))

counts[0] = 1
for i in range(1,len(splitdata)):
    for j in range(0,i):
        if splitdata[i] - splitdata[j] <= 3:
            counts[i] += counts[j]

print(counts[-1])
