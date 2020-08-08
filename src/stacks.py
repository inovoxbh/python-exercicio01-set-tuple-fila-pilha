# -*- coding: utf-8 -*-

# definição: uma coleção de dados onde onde novos itens vão sendo inseridos nas posições finais do array (último que entra, primeiro que sai)

# fonte: https://panda.ime.usp.br/pythonds/static/pythonds_pt/03-EDBasicos/05-PilhaImplementacao.html

# classe pilha
class Stack:
    def __init__(self):
        self.items = []

    def insert(self,item_to_be_inserted):
        self.items.insert(0,item_to_be_inserted)

    def delete(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)        

    def printQueue(self):
        for queueItem in self.items:
            print(queueItem)

# instanciando a pilha
Stack01 = Stack()

# inserindo itens na pilha
Stack01.insert("Mateus")
Stack01.insert("Marcos")
Stack01.insert("Lucas")
Stack01.insert("João")

# imprimindo pilha
print("Pilha original")
Stack01.printQueue()
print("#####################")

# removendo item da pilha
Stack01.delete()
print("Deletando o topo da pilha")
Stack01.printQueue()
print("#####################")

# peek: topo da pilha = último item inserido, primeiro a ser deletado.
print("Topo da pilha")
print(Stack01.peek())
print("#####################")

# size
print("Tamanho da pilha")
print(Stack01.size())
