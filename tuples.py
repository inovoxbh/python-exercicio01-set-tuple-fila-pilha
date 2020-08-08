# -*- coding: utf-8 -*-

# definição: uma coleção de dados ordenada e não alterável

# função para imprimir itens
def print_tuple(tuple_to_be_printed):
    for item in tuple_to_be_printed:
        print(item)
    print("Tamanho da tuple:",len(tuple_to_be_printed),"itens")
    print("#########################")

# criação de uma tuple: 
my_tuple = ("Mateus","Marcos","Lucas","João")
print("Tuple original")
print_tuple(my_tuple)

# primeiro item da tupple
print("Primeiro item da tuple:",my_tuple[0])
print("#########################")

# último item da tupple
print("Último item da tuple:",my_tuple[-1])
print("#########################")