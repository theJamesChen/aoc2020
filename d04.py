## DAY 4
file = "d4.txt"
with open(file) as f:
    data = f.read()
    
splitdata = data.split('\n\n')
required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
count = 0
for i, line in enumerate(splitdata):
    valid = True
    splitdata[i] = line.replace('\n', ' ')
    passport = splitdata[i].split()
    fields = [e.split(':') for e in passport]
    if required.issubset([field[0] for field in fields]):
        for field in fields:
            key, value = field[0], field[1]
            if key == 'byr' and not (int(value) >=1920 and int(value) <= 2002):
                valid = False
            elif key == 'iyr' and not (int(value) >=2010 and int(value) <= 2020):
                valid = False 
            elif key == 'eyr' and not (int(value) >=2020 and int(value) <= 2030):
                valid = False
            elif key == 'hgt':
                if value[-2:] != "cm" and value[-2:] != "in":
                    valid = False
                elif value[-2:] == "cm" and not (int(value[:-2]) >= 150 and int(value[:-2]) <=193):
                    valid = False
                elif value[-2:] == "in" and not (int(value[:-2]) >= 59 and int(value[:-2]) <= 76):
                    valid = False
            elif key == 'hcl':
                allowed = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
                if not (value[0] == '#' and len(value) == 7 and set(value[1:]).issubset(allowed)):
                    valid = False
            elif key == 'ecl':
                allowed = {'amb','blu' ,'brn', 'gry' ,'grn' ,'hzl', 'oth'}
                if value not in allowed:
                    valid = False
            elif key == 'pid':
                if not (len(value) == 9 and value.isnumeric()):
                    valid = False
            
        if valid:
            count += 1
        

print(count)
