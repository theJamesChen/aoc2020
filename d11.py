## DAY 11
file = "d11.txt"
with open(file) as f:
    data = f.read().rstrip()

splitdata = data.split('\n')
splitdata = [list(i) for i in splitdata]

width = len(splitdata[0])
length = len(splitdata)
print(length, width)

def occupied(splitdata,i,j):
    occ=0
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for deltai,deltaj in directions:
        if 0<=i+deltai<length and 0<=j+deltaj<width and splitdata[i+deltai][j+deltaj]=='#':
            occ+=1
    return occ

def occupied_part2(splitdata,i,j):
    occ=0
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for deltai,deltaj in directions:
        i_deltai = i+deltai
        j_deltaj = j+deltaj
        while 0<=i_deltai<length and 0<=j_deltaj<width:
            if splitdata[i_deltai][j_deltaj]=='#':
                occ+=1
                break
            elif splitdata[i_deltai][j_deltaj]=='L':
                break
            i_deltai+=deltai
            j_deltaj+=deltaj
    return occ

while True:
    equilibrium=True
    splitdata_copy=[row.copy() for row in splitdata]
    for i,row in enumerate(splitdata_copy):
        for j,cell in enumerate(row):
            count=occupied_part2(splitdata_copy,i,j)
            if cell=='L' and count==0:
                splitdata[i][j]='#'
            elif cell=='#' and count>=5:
                splitdata[i][j]='L'
            equilibrium = equilibrium and (cell==splitdata[i][j])
    if equilibrium:
        break
        
print(sum(splitdata[i][j] == '#' for i in range(length) for j in range(width)))

            
