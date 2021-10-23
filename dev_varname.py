
#Script de varredura do padrão _2Dígitos

import re # Módulo regular expressions
datam_84_72 =""
darav_79_77=""

regex= "_[0-9][0-9]" #Padrão de dois dígitos após underline

var_80_83 =locals() # retorna tabela de símbolos
lista_79_78 = []# Criamos uma lista 
lista_79_78.append(var_80_83)# Adicionamos a tabela anterior
match= re.findall(regex,''.join(str(lista_79_78))) # varredura em busca do padrão
mlist=[re.sub('[^a-zA-Z0-9]+', '', _) for _ in match]#removemos underline
print(mlist)#saída com lista final para exibir assinatura
strtoint= list(map(int,mlist))
res = ""
for val in strtoint:
    res = res + chr(val)#conversão
print('Assinatura em código:' , res)