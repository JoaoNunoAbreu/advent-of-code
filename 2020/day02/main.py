import re
import sys
file = open('input.txt', 'r')
lines = file.readlines()

print("Part: ",end="")
part = input()

valids = 0
for i in lines:
    c = re.search('(?<= )(.*)(?=:)', i).group()
    nums = re.search('[^ ]+', i).group()
    nums_part = nums.split("-")
    word = re.search('(?<=: )(.*)$', i).group()
    if(part == "1"):
        if(word.count(c) >= int(nums_part[0]) and word.count(c) <= int(nums_part[1])):
            valids += 1
    elif(part == "2"):
        if(int(nums_part[0]) < len(word) and (word[int(nums_part[0])-1] == c) != (word[int(nums_part[1])-1] == c)):
            valids += 1
    else:
        print("Parte inválida!")
        sys.exit()
        
print(valids)