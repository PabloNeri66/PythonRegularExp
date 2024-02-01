#Quantificadores Greedy e Non-greedy(lazy)

# Meta-Caracteres: ^ $ 

#(abc|def)+       Grupo!!! nos grupos podemos transportar seu valor 
#            sem ficar reescrevendo... Como se fosse uma variável.

#Grupo () é chamado de retrovisores também...  
# () \1
# () () \1 \2
#(()) () \1 \2 \3 conte pela abertura dos grupos...
# '?:' dentro de um grupo indica  ao python que esse grupo não será contabilizado.
#                    ou seja, se esse na lógica fosse o grupo 3 de quatro retrovisores
#                    então, o quarto se tornaria o gp3 e este sumiria da contagem.
#?P cria um retrovisor que pode ser nomeado.

#Retrovisores são usados para dividir e salvar as aberturas ou o metacaracteres 
#           ou os parâmetros


import re
from pprint import pprint


texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''


#cpf = '147.852.963-12'

#print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}\-[0-9]{2})', cpf))



#tags = (re.findall(r'<([pdiv]*)>(.+?)<\/\1', texto))
#tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
#pprint(tags)

 
#for tag in tags:
#   um, dois, tres = tag
#   print(tres)


print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r' \1"\3"\4 ', texto))
