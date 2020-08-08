# -*- coding: utf-8 -*-

# definição: uma coleção de dados onde onde novos itens vão sendo inseridos nas posições iniciais do array (primeiro que entra, primeiro que sai)

# fonte: https://panda.ime.usp.br/pythonds/static/pythonds_pt/03-EDBasicos/12-FilaImplementacao.html

# classe fila
class Queue:
    def __init__(self):
        self.items = []

    def insert(self,item_to_be_inserted):
        self.items.insert(0,item_to_be_inserted)

    def delete(self):
        return self.items.pop()

    def printQueue(self):
        for queueItem in self.items:
            print(queueItem)

# instanciando a fila
Queue01 = Queue()

# inserindo itens na fila
Queue01.insert("Mateus")
Queue01.insert("Marcos")
Queue01.insert("Lucas")
Queue01.insert("João")

# imprimindo lista
print("Fila original")
Queue01.printQueue()
print("#####################")

# removendo primeiro item inserido na fila
Queue01.delete()
print("Deletando início da fila (o primeiro que chegou)")
Queue01.printQueue()
