class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class SimpleLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def insertStart(self, data):
        node = Node(data)

        # lista vazia
        if self.len == 0:
            self.head = node
        else:
            node.setNext(self.head)
            self.head = node
        self.len += 1

    def insertEnd(self, data):
        node = Node(data)
        if self.len == 0:
            self.head = node
        else:
            aux = self.head
            while aux.getNext() is not None:
                aux = aux.getNext()
            aux.setNext(node)
        self.len += 1

    def insertIndex(self, index, data):
        if index < 0 or index > self.len:
            return False
        if index == 0:
            self.insertStart(data)
        else:
            node = Node(data)
            aux = self.head
            for i in range(index - 1):
                aux = aux.getNext()
            node.setNext(aux.getNext())
            aux.setNext(node)
            self.len += 1

    def insertAlphabetic(self, data):
        node = Node(Person(data.name, data.age))

        # lista vazia
        if self.len == 0:
            self.head = node
        else:
            # inserir no começo
            if node.getData().name < self.head.getData().name:
                node.setNext(self.head)
                self.head = node
            else:
                # inserir no meio
                aux1 = self.head
                aux2 = self.head.getNext()
                flag_add = False
                while aux2 != None:
                    if node.getData().name < aux2.getData().name:
                        node.setNext(aux2)  # node.setNext(aux1.getNext())
                        aux1.setNext(node)
                        flag_add = True
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
                # inserir no final
                if flag_add == False:
                    aux1.setNext(node)
        self.len += 1

    def show(self):
        aux = self.head
        while aux is not None:
            print(f'Idade: {aux.getData().age} Nome: {aux.getData().name}')
            aux = aux.getNext()
        print()

    def copy(self):
        aux = self.head
        lista = SimpleLinkedList()
        while aux is not None:
            lista.insertEnd(aux.getData())
            aux = aux.getNext()
        return lista

    def reverse(self):
        prev = None
        aux = self.head
        while aux is not None:
            next = aux.getNext()
            aux.setNext(prev)
            prev = aux
            aux = next
        self.head = prev


sll = SimpleLinkedList()

quantidade = int(input())

for i in range(quantidade):
    _frase = input()
    _nome = ""
    for word in _frase.split(" "):
        if word.isdigit():
            _idade = int(word)
    _nome = ''.join(i for i in _frase if not i.isdigit())

    person = Person(_nome, _idade)
    sll.insertAlphabetic(person)

sll2 = sll.copy()
sll2.reverse()
sll2.show()
