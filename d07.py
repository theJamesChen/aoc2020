## DAY 7
file = "d7.txt"
with open(file) as f:
    data = f.read().rstrip()
    
splitdata = data.split('\n')
bag_mapping = {}

def unpack(description):
    splitline = description.split()
    number = (' '.join(splitline[:1]))
    color = (' '.join(splitline[1:-1]))
    return number, color

for line in splitdata:
    splitline = line.split()
    colorkey = ' '.join(splitline[:2])
    bags_equal_to = ' '.join(splitline[4:])
    bags_equal_to_split = bags_equal_to.split(',')
    bag_array = []
    for bags in bags_equal_to_split:
        num, color = unpack(bags)
        if num == "no": # unfortunately I parsed it incorrectly... this is a workaround
            num = 1
            color = "other" 
        
        bag_array.append((int(num), color))
    bag_mapping[colorkey] = bag_array
    

def unpack_mapping(keycolor, values, has_gold_mapping = None):
    if has_gold_mapping is None:
        has_gold_mapping = set()
    if keycolor in has_gold_mapping:
        return True
    hasgold = False
    if len(values) == 1 and values[0][1] == 'other':
        return False
    for num, value in values:
        if value == 'shiny gold':
            has_gold_mapping.add(keycolor)
            return True
        
        hasgold = hasgold or unpack_mapping(value, bag_mapping[value], has_gold_mapping)
    
    return hasgold

countgold = 0
for keycolor, values in bag_mapping.items():
    if unpack_mapping(keycolor, values):
        countgold += 1
        
print(countgold)

def total_mapping(keycolor, values):
    total = 1
    if len(values) == 1 and values[0][1] == 'other':
        return 1
    for num, value in values:
        total += (num * total_mapping(value, bag_mapping[value]))
    
    return total

total = total_mapping('shiny gold', bag_mapping['shiny gold'])

print(total-1)

