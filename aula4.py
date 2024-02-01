#Quantificadores Greedy e Non-greedy(lazy)

# Meta-Caracteres: ^ $ * + ? { } \ ( ) 

# * ---> 0 ou n 

# + ---> 1 ou n

# ? ---> 0 ou 1

import re

texto = '''
<p>Frase 1</p>
<p>Eita</p>
<p>Qualquer frase</p>
<div></div>
'''

print(re.findall(r'<[pdiv]*>.*<\/[pdiv]*>', texto))
print(re.findall(r'<[pdiv]*>.+?<\/[pdiv]*>', texto))