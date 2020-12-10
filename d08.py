## DAY 8
file = "d8.txt"
with open(file) as f:
    data = f.read().rstrip()
    
splitdata = data.split('\n')
splitdata_indx = [(data.split(' ')) for data in splitdata]

def runthis(splitdata_indx):
    total = 0
    i = 0
    checked = set()
    while True:
        if i in checked:
            return (False, total)
            break
        if i == len(splitdata_indx):
            return (True, total)
        checked.add(i)
        instruction, num = splitdata_indx[i]
        if instruction == 'acc':
            total += int(num)
        elif instruction == 'jmp':
            i += int(num)
            continue
        i += 1
print(runthis(splitdata_indx))
    
for i, instructions in enumerate(splitdata_indx):
    instr, num = instructions
    if instr == "acc":
        continue
    create_new_splitdata = [instruc for instruc in splitdata_indx]
    if instr == "jmp":
        create_new_splitdata[i] = ("nop", num)
    else:
        create_new_splitdata[i] = ("jmp", num)
    (boooolean, total) = runthis(create_new_splitdata)
    if boooolean:
        print(total)
        break

