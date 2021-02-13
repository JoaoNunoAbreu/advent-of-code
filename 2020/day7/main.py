import re,json

file = open('input2.txt', 'r')
lines = file.readlines()

#print("Part: ",end="")
#part = input()

d = {}

for i in lines:
    k = re.search('(.*?)(?= bags)', i).group()
    vals = re.search('(?<=contain )(.*)(?=\.)', i).group().replace(", ",",").split(",")
    vals_fixed = []
    for j in vals:
        j = j.replace("bags","").replace("bag","").strip()
        quant = re.search('(.*?)(?= )', j).group()
        tipo = re.search('(?<= )(.*)', j).group()
        if(quant == "no"):
            quant = 0
            tipo = "N/A"
        vals_fixed.append({
            "quant": quant,
            "tipo": tipo
        })
        
    d[k] = vals_fixed

# Fazer função recursiva que leva como argumentos o dict e lista de bags que contêm shiny gold

alterou = True
matches = []
while(alterou):
    for key,value in d.items():
        for v in value:
            if(v['tipo'] == 'shiny gold'):
                matches.append(key)
    alterou = False

print(matches)
#print(json.dumps(d,indent=4,sort_keys=True))

#if(part == "1"):
#    pass
#
#elif(part == "2"):
#    pass
#        
#else:
#    print("Parte inválida!")

def find_colors(d,l):
    for key,value in d.items():
        for v in value:
            if(v['tipo'] == 'shiny gold'):
                matches.append(key)
    