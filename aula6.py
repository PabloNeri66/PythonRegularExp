# Meta-Caracteres: ^ $ 

# ^ --> Começa com

# $ --> Termina com

#[^A-Z] o chapéuzinho(circunflexo) pode signifcar Negação...

#esses dois metas-caracteres $ e ^ são bastante funcionais para 
#               um cadastro com cpf rg etc...

import re

cpf = '147.852.963-12'

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}\-[0-9]{2})$', cpf))




#tags = (re.findall(r'<([pdiv]*)>(.+?)<\/\1', texto))
#tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
#pprint(tags)