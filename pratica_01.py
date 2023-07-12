# Imprimir tipos dos elementos da lista_nums
lista_nums = [1.0, 2.0, 3.0, 4.0, 5.0]
for item in lista_nums:
    print(type(item))

# Imprimir apenas elementos string da lista_mista
lista_mista = [1, "gato", 2, "cachorro", 3, "peixe"]
for item in lista_mista:
    if isinstance(item, str):
        print(item)
