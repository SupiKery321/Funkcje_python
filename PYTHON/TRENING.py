from itertools import chain

skills = [
    ["Java", "Python"],
    ["Docker"],
    ["PHP", "C++"]
]

splaszczona_lista = (list((chain.from_iterable(skills))))

ladna_lista = ", ".join(splaszczona_lista)

print(ladna_lista)