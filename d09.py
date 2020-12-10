## DAY 9
file = "d9.txt"
with open(file) as f:
    data = f.read().rstrip()
    
splitdata = data.split('\n')
splitdata = [int(i) for i in splitdata]

def twosum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return (True, [dic[num], i])
        else:
            dic[target - num] = i
    return (False, None)

j = 0
for i in range(25, len(splitdata)):
    boolean, pair = twosum(splitdata[j:i], splitdata[i])
    j+=1
    if not boolean:
        number=splitdata[i]
        print(number)
        

for window in range(2,len(splitdata)):
    for i in range(len(splitdata)-window):
        s = splitdata[i:i+window]
        if sum(s) == number:
            print(min(s)+max(s))
