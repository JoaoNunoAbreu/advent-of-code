import re

file = open('input.txt', 'r')
lines = file.readlines()
lines = [i.strip() for i in lines]

print("Part: ",end="")
part = input()

def myreplace(l,s1,s2,index):
    count = 0
    res = l.copy()
    for i in range(len(res)):
        if(s1 in res[i] and count == index):
            res[i] = res[i].replace(s1,s2)
            count += 1
        elif(s1 in res[i]):
            count += 1
    return res

def counter(lines,part):
    visited_indexes = []
    i = 0
    counter = 0
    found = False
    while(True):
    
        if(i in visited_indexes):
            break
        if(i == len(lines)):
            found = True
            break
    
        visited_indexes.append(i)
        op = re.search('(.*)(?= )', lines[i]).group()
        num = re.search('[+-][0-9]+', lines[i]).group()
    
        if(op == "acc"):
            if(num[:1] == "+"):
                counter += int(num[1:])
            else:
                counter -= int(num[1:])
            i += 1
        elif(op == "nop"):
            i += 1
        else:
            if(num[:1] == "+"):
                i += int(num[1:])
            else:
                i -= int(num[1:])

    if((found == True and part == 2) or part == 1):
        print(counter)

if(part == "1"):
    counter(lines,1)

elif(part == "2"):

    jmps = len([i for i in lines if("jmp" in i)])
    nops = len([i for i in lines if("nop" in i)])
    
    for i in range(jmps):
        new_lines = myreplace(lines,"jmp","nop",i)
        counter(new_lines,2)

    for i in range(nops):
        new_lines = myreplace(lines,"nop","jmp",i)
        counter(new_lines,2)

else:
    print("Parte inválida!")
        