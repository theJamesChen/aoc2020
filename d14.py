## DAY 14
file = "d14.txt"
with open(file) as f:
    data = f.read().rstrip()

splitdata = data.split('\n')
splitdata = [i for i in splitdata]

def decimalToBinary(n):  
    return bin(n).replace("0b", "") 

mem = {}
for line in splitdata:
    if 'mask' in line:
        current_mask = list(line.split('=')[1].lstrip())
        current_mask = [int(i) if i != 'X' else 2 for i in current_mask]
        #print(current_mask)
    else:
        dictionary_entry, num = line.split(' = ')
        entry = ''.join(filter(lambda i: i.isdigit(), dictionary_entry))
        binary_array = list(decimalToBinary(int(num)))
        if len(binary_array) != 36:
            num_to_add = 36-len(binary_array)
            binary_array = num_to_add*['0'] + binary_array
        binary_array = [int(i) for i in binary_array]
    
        value = [1 if i == 1 else 0 if i == 0 else j for i, j in zip(current_mask, binary_array)]
        mem[entry] = int(str("".join([str(i) for i in value])),2)

#print(mem)
print(sum(mem.values()))


def get_all_combos(binary_array, mask): 
    masked_locations = ['']
    for i in range(len(mask)):
        if mask[i] == 'X':
            locations_0 = [sub_mask + '0' for sub_mask in masked_locations]
            locations_1 = [sub_mask + '1' for sub_mask in masked_locations]
            masked_locations = locations_0 + locations_1
        elif mask[i] == '0':
            masked_locations = [sub_mask + binary_array[i] for sub_mask in masked_locations]
        else:
            masked_locations = [sub_mask + '1' for sub_mask in masked_locations]
    return masked_locations


mem = {}
for line in splitdata:
    if 'mask' in line:
        current_mask = list(line.split('=')[1].lstrip())
        current_mask = [str(i) if i != 'X' else 'X' for i in current_mask]
        #print(current_mask)
    else:
        dictionary_entry, num = line.split(' = ')
        entry = ''.join([i for i in dictionary_entry if i.isdigit()])
    
        binary_array = list(decimalToBinary(int(entry)))
        if len(binary_array) != 36:
            num_to_add = 36-len(binary_array)
            binary_array = num_to_add*['0'] + binary_array
        binary_array = [str(i) for i in binary_array]
        #print(binary_array)
        #print(current_mask)
        locations = get_all_combos(binary_array, current_mask)
    
        for location in locations:
            mem[location] = int(num)

#print(mem)
print(sum(mem.values()))
    
