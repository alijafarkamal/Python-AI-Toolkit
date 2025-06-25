from random import choice
from string import  digits,ascii_lowercase,ascii_uppercase

special_chars = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
password_length = 40
indices = list(range(password_length))
characters_types = [ascii_uppercase, ascii_lowercase, digits, special_chars]
characters_list = ['']*password_length

for i in range(4):
    index = choice(indices)
    characters_list[index] = choice(characters_types[i]) 
    indices.remove(index)
    
characters_base = ''.join(characters_types)
for index in indices:
    characters_list[index] = choice(characters_base)
    
password = ''.join(characters_list)
print(password)