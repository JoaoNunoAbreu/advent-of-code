import sys
file = open('input.txt', 'r')
lines = file.readlines()
lines = [int(i) for i in lines]

print("Part: ",end="")
part = input()

if(part == "1"):
    for i in lines:
        for j in lines:
            if(i+j == 2020):
                print(i*j)
                sys.exit()
elif(part == "2"):
    for i in lines:
        for j in lines:
            for k in lines:
                if(i + j + k == 2020):
                    print(i*j*k)
                    sys.exit()
else:
    print("Parte inválida!")