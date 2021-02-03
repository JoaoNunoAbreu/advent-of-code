# -------------------------------------------------------- DAY 4 - PART 2 --------------------------------------------------------
import re

def validbyr(byr):
    return int(byr) >= 1920 and int(byr) <= 2002

def validiyr(iyr):
    return int(iyr) >= 2010 and int(iyr) <= 2020

def valideyr(eyr):
    return int(eyr) >= 2020 and int(eyr) <= 2030

def validhgt(hgt):
    if(hgt[-2:] == "cm"):
        return int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193
    elif(hgt[-2:] == "in"):
        return int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76
    else:
        return False

def validhcl(hcl):
    return re.match("#[a-f0-9]{6}$",hcl)

def validecl(ecl):
    arr = ["amb","blu","brn","gry","grn","hzl","oth"]
    return ecl in arr

def validpid(pid):
    return re.match("[0-9]{9}$",pid) and len(str(pid)) == 9

# ----------------------------------------------------------------------------------

file = open('input.txt', 'r')

passports = []
valids = 0
l = {}
while True:
    line = file.readline()
    if not line:
        break
    if(line == "\n"):
        passports.append(l)
        l = {}
    else:
        parts = line.strip().split(" ")
        for i in parts:
            k = re.search('(.*)(?=:)', i).group()
            val = re.search('(?<=:)(.*)', i).group()
            l[k] = val
        
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
for i in passports:
    if((len(i) == 8 or (len(i) == 7 and all(elem in i.keys()  for elem in fields)))
    and all([validbyr(i["byr"]),
            validiyr(i["iyr"]),
            valideyr(i["eyr"]),
            validhgt(i["hgt"]),
            validhcl(i["hcl"]),
            validecl(i["ecl"]),
            validpid(i["pid"])])):
        valids += 1

print(valids)



