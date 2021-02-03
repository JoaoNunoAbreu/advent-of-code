# -------------------------------------------------------- DAY 4 - PART 1 --------------------------------------------------------
import re

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
    if(len(i) == 8 or (len(i) == 7 and all(elem in i.keys()  for elem in fields))):
        valids += 1

print(valids)