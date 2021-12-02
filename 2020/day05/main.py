file = open('input.txt', 'r')
lines = file.readlines()

arr = []
for i in lines:

    rowmin = 0
    rowmax = 127
    colmin = 0
    colmax = 7

    for c in list(i):
        if(c == "F"):
            rowmax -= (rowmax - rowmin + 1) / 2
        elif(c == "B"):
            rowmin += (rowmax - rowmin + 1) / 2 
        elif(c == "L"):
            colmax -= (colmax - colmin + 1) / 2 
        elif(c == "R"):
            colmin += (colmax - colmin + 1) / 2 
     
    arr.append(rowmin * 8 + colmax)

print("Part: ",end="")
part = input()

if(part == "1"):
    print(max(arr))
elif(part == "2"):
    arr.sort()
    for i in range(1,len(arr)):
        if(arr[i]-arr[i-1] == 2):
            print((arr[i]+arr[i-1])/2)
else:
    print("Parte inválida!")