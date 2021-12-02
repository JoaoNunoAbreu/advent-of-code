file = open('input.txt', 'r')

print("Part: ",end="")
part = input()

count = 0
l = []

if(part == "1"):
    while True:
        line = file.readline()
        if not line:
            break
        if(line == "\n"):
            n = len(list(dict.fromkeys(l)))
            l = []
            count += n
        else: 
            l += list(line.strip())

    print(count)

elif(part == "2"):

    d = {}
    num = 0
    while True:
        line = file.readline()
        if not line:
            break
        if(line == "\n"):
            count += len(set.intersection(*map(set,list(d.values()))))
            d = {}
            num = 0
        else: 
            d[num] = list(line.strip())
            num += 1

    print(count)
        
else:
    print("Parte inválida!")