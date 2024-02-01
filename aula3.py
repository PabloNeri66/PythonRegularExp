# Meta-Caracteres: ^ $ * + ? { } \ ( ) 

# * ---> 0 ou n 

# + ---> 1 ou n   -- {1,}

# ? ---> 0 ou 1

# {} ---> {n} ou {min, max} exemplos:
#       {10,} 10 ou mais vezes, ou seja, as chaves possuem função similar ao +
#       {10} Específicamente 10. ou {5,10} 5 a 10 repetições desse caractere. 

#()+ quantificador ele se aplica a um grupo: [a-z]+

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
print(re.findall('ve{3}m{1,2}', texto, re.I))
print(re.findall('jo+Ão+', texto, flags=re.IGNORECASE))
print(re.findall('jo{1,}Ão{1,}', texto, flags=re.IGNORECASE))
#print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.I))

texto2 = 'João ama ser amado não amad nem amao'
print(re.findall('ama[do]*', texto2, re.I))