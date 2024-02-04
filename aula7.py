#              -SHORT RANGES-

#\w ----> [a-zA-Z0-9À-ú_] esse \w é para python!
#\w ----> [a-zA-Z0-9]  --> re.A re.ASCII   'essa FLAG (re.A) fará que o python se comporte como JavaScript'

#A negação de \w seria \W
#\W ---> [^a-zA-Z0-9À-ú_]

#\d --> [0-9]
#\D --> [^0-9]

#\s --> [ \r\n\f\t]   encontra os espaços na string.
#\S --> [^ \r\n\f\t]

#\b borda
#\B Não borda


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

#print(re.findall(r'[a-z]+', texto, re.IGNORECASE))

#print(re.findall(r'[a-zA-Z]+', texto))

#print(re.findall(r'[a-zA-Z0-9]+', texto))

#print(re.findall(r'[a-zA-Z0-9À-ú]+', texto)),

#WORDS --> \w
#print(re.findall(r'\w+', texto, re.I))
#print(re.findall(r'\W+', texto, re.I))
#pode perceber com esse comando que o console não pega palavras com acento 
#de forma correta, porque o re.ASCII tira o comando full unicode do \w

#Digits --> \d
#print(re.findall(r'\d+', texto, re.I))
#print(re.findall(r'\D+', texto, re.I))

#SPACES ---> \s
#print(re.findall(r'\s+', texto, re.I))


# BOARD ---> \b
#print(re.findall(r'\be\w+', texto, re.I))
#print(re.findall(r'\w+e\b', texto, re.I))
#print(re.findall(r'\b\w{4}\b', texto, re.I))
print(re.findall(r'flores\B', texto, re.I))
