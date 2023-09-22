"""
Problemas dos parametros mutaveis
Objetos mutaveis = Lista, dicionarios
Objetos imutaveis = tupla, str, valores boolean, numeros(int e float), set
"""


# O interpretador avalia 1 vez só, entao ele seta a lista(mutavel) uma vez!
def lista_de_clientes(clientes_iteravel, lista=[]):  # python indica!
    lista.extend(clientes_iteravel)
    return lista


cliente1 = lista_de_clientes(['Everton', 'Anna', 'Joao'])
cliente2 = lista_de_clientes(['Fabia', 'Jose', 'Mario'])
print(cliente1)
print(cliente2)


# para revolver o problema, é só nao ter um argumento mutavel
def lista_de_clientes2(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


cliente1 = lista_de_clientes2(['Everton', 'Anna', 'Joao'])
cliente2 = lista_de_clientes2(['Fabia', 'Jose', 'Mario'])
print(cliente1)
print(cliente2)