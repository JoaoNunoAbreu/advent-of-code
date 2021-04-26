import re

# Part 1

def check1(array,val):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if(array[i] + array[j] == val):
                return True
    return False

def part1(lines):

    id_begin = 0
    id_end = 25

    while(id_end != len(lines)):
        val = lines[id_end]
        if(check1(lines[id_begin:id_end],val) == False):
            return val
        id_begin += 1
        id_end += 1

# Part 2

def getInterval(lines,value):
    for i in range(len(lines)):
        soma = 0
        for j in range(i+1,len(lines)):
            soma = sum(lines[i:j+1])
            if(soma > value):
                break
            if(soma == value):
                return i,j

def part2(lines,value):
    id_begin,id_end = getInterval(lines,value)
    arr = sorted(lines[id_begin:id_end+1])
    return arr[0] + arr[len(arr)-1]
            

# Main

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    lines = [int(i.strip()) for i in lines]

    print("Part: ",end="")
    part = input()

    if(part == "1"):
        print(part1(lines))
    elif(part == "2"):
        print(part2(lines,part1(lines)))
    else:
        print("Parte inválida!")


if __name__ == '__main__':
    main()