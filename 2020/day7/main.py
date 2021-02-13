import re

file = open('input.txt', 'r')
lines = file.readlines()

print("Part: ",end="")
part = input()

d = {}

# Preenchimento estrutura de dados
for i in lines:
    k = re.search('(.*?)(?= bags)', i).group()
    vals = re.search('(?<=contain )(.*)(?=\.)', i).group().replace(", ",",").split(",")
    vals_fixed = []
    for j in vals:
        j = j.replace("bags","").replace("bag","").strip()
        quant = re.search('(.*?)(?= )', j).group()
        tipo = re.search('(?<= )(.*)', j).group()
        if(quant != "no"):
            vals_fixed.append({
                "quant": int(quant),
                "tipo": tipo
            })
        
    d[k] = vals_fixed


if(part == "1"):
    matches = []
    while(True):
        tmp = matches.copy()
        for key,value in d.items():
            for v in value:
                if((v['tipo'] in matches or v['tipo'] == 'shiny gold') and key not in matches):
                    matches.append(key)
                    
        # Se não houve alterações termina
        if(tmp == matches):
            break

    print(len(matches))

elif(part == "2"):

    def conta(bag_collection, bag_name):
        count = 0
        top_level_bag = bag_collection[bag_name]

        if len(top_level_bag) == 0:
            return count
        else:
            for current_bag in top_level_bag:
                count += current_bag['quant']
                res = conta(bag_collection, current_bag["tipo"])
                count += res * current_bag['quant']

        return count
    
    print(conta(d,'shiny gold'))

else:
    print("Parte inválida!")
        
