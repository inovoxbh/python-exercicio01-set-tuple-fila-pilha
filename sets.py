# -*- coding: utf-8 -*-

# definição: uma coleção de dados não ordenada e não indexada

# função para imprimir itens
def print_set(set_to_be_printed):
    for item in set_to_be_printed:
        print(item)
    print("Tamanho da set:",len(set_to_be_printed),"itens")
    print("#########################")

# criação de uma set: 
my_set = {"João","Lucas","Matheus","Marcos"}
print("Set original")
print_set(my_set)

# adicionando item à uma set
my_set.add("Paulo")
print("Set com mais um item")
print_set(my_set)

# removendo item de uma set
my_set.remove("Marcos")
print("Set com menos um item")
print_set(my_set)