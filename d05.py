## DAY 5
file = "d5.txt"
with open(file) as f:
    lines = [line.rstrip() for line in f]

product = []
for line in lines:
    current_rows = [0, 127]
    current_cols = [0,7]
    rows = line[:7]
    cols = line[7:]
    for letter in rows:
        if letter == "F":
            diff = (current_rows[1] - current_rows[0] + 1)/2
            current_rows = [current_rows[0], diff+current_rows[0]-1]
        else:
            diff = (current_rows[1] - current_rows[0] + 1)/2
            current_rows = [diff + current_rows[0], current_rows[1]]
    #print(cols)
    for letter in cols:
        if letter == "L":
            diff = (current_cols[1] - current_cols[0] + 1)/2
            current_cols = [current_cols[0], diff+current_cols[0]-1]
        else:
            diff = (current_cols[1] - current_cols[0] + 1)/2
            current_cols = [diff + current_cols[0], current_cols[1]]
    product.append(current_rows[0]*8 + current_cols[0])

print(min(product), max(product))
setproduct = set(product)
print(set(range(int(min(product)),int(max(product)))) - setproduct)
