import re
import sys
file = open('input.txt', 'r')
lines = file.readlines()

print("Part: ",end="")
part = input()

count = 0

if(part == "1"):
    col = 0
    for i in lines:
        if(i[col] == "#"):
            count += 1
        col += 3
    print(count)
elif(part == "2"):
    col1 = count1 = 0
    col2 = count2 = 0
    col3 = count3 = 0
    col4 = count4 = 0
    for i in lines:
        if(i[col1] == "#"):
            count1 += 1
        if(i[col2] == "#"):
            count2 += 1
        if(i[col3] == "#"):
            count3 += 1
        if(i[col4] == "#"):
            count4 += 1
        col1 += 1
        col2 += 3
        col3 += 5
        col4 += 7
    
    col5 = count5 = 0
    row5 = 0
    while(row5 < len(lines)):
        if(lines[row5][col5] == "#"):
            count5 += 1
        row5 += 2
        col5 += 1

    print(count1*count2*count3*count4*count5)
else:
    print("Parte inválida!")
