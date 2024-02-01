import re

# findall search sub
# compile
# count = 0, ele pega todas as palavras especificada que encontrar no texto e substitui.

#'Teste' e 'teste' são diferentes para as strings das expressões regulares... se atentar


string = 'Este é um teste de expressões regulares. Mas o teste da vida e amar'
#print(re.search(r'teste', string))
#print(re.findall(r'teste', string,))
#print(re.sub(r'teste','ABCD', string, count=0))

comp = re.compile('teste')
print(comp.search(string))
print(comp.findall(string))
print(comp.sub('DEF', string, count=1))