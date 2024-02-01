# Meta-Caracteres: . ^ $ * + ? { } [ ] \ | ( ) 
# '|' Significa OU
# '.' significa QUALQUER CARACTERE(com excessão da quebra de linha)
# '[]' Significa um conjunto de caracteres
# RANGE - USADO PARA DETERMINAR UMA SEQUENCIA, POR EXEMPLO: [123456] == [1-6]
# OU [ABCDEFGHIJ] == [A-Z]SSS


#FLAGS: 're.I' OU 're.IGNORECASE' --> Usados para mostrar todos resultados que contenham 
#   a mesma palavra e possuem letras maiúsculas...  

import re

texto = '''João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''
#Fiz um compilado com o compile para teste, o compile serve como uma variavel funcional
#   para uma  palavra específica que seja muito procurada...
    #comp = re.compile('flores')
    #print(comp.search(texto))

print(re.findall('ad....s|Maria', texto))
print(re.findall('João|joão|Maria', texto))
print(re.findall('[Jj]oão|[Mm]aria', texto))
print(re.findall('[A-Z]aria', texto))
print(re.findall('MaRiA', texto, flags=re.IGNORECASE))