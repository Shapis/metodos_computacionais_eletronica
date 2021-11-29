import re


class Person:
    def __init__(self, id, name, age, weight, height):
        self.name = name
        self.id = id
        self.age = age
        self.weight = weight
        self.height = height


class Node:
    def __init__(self, label):
        self.label = label
        self.next = None

    def getLabel(self):
        return self.label

    def getNext(self):
        return self.next

    def setLabel(self, label):
        self.label = label

    def setNext(self, next):
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    # insert
    def insertSorted(self, label):
        aux = self.head
        i = 0
        for i in range(self.getLength()):
            if aux.getLabel() > label:  # inserir em ordem crescente
                break
            aux = aux.getNext()
        if i == self.getLength() - 1 and i != 0:
            self.append(label)
        else:
            self.insert(label, i)

    def append(self, label):
        self.insert(label, self.getLength())

    def insert(self, label, index):
        if index <= self.getLength() and index >= -(self.getLength()+1) and self.search(label) == None:
            node = Node(label)
            if index < 0:
                index = self.getLength() + index + 1

            if self.empty() == True:
                self.head = node
                node.setNext(node)  # self.head.setNext(self.head)
                self.len += 1
                return
            aux = self.head
            for _ in range(self.getLength() - 1 if index == 0 else index - 1):
                aux = aux.getNext()
            node.setNext(aux.getNext())
            aux.setNext(node)
            if index == 0:
                self.head = node
            self.len += 1

    # remove
    def removeLabel(self, label):
        if not self.empty():
            if self.len == 1:
                self.head = None
                self.len = 0
                return
            index = self.search(label)
            if index == None:
                print("Node não encontrado")
                return
            self.removeIndex(index)

    def removeIndex(self, index):
        # Se meu index for maior que o tamanho da minha lista ou negativo (ERRO!)
        if (index >= self.len):
            print(f"Index out of range: {index}, size: {self.len}")
            return

        # Se o tamanho da minha lista for 1, reseta a lista
        if self.len == 1:
            self.head = None
            self.len = 0
            return

        # Remover um valor em um index dentro do intervalo:

        # Pego o bloco anterior e o próximo do bloco que quero remover
        before = self.head
        for _ in range(self.len - 1 if index - 1 == -1 else index - 1):
            before = before.next
        after = before.next.next

        # Faço meu bloco anterior receber como próximo, o bloco depois do que quero remover
        # Dessa forma perco a informação do bloco no índice que quero remover
        before.next = after

        # Se meu index for 0, também preciso alterar a cabeça da minha lista
        # fazendo com que ela seja agora o bloco que vinha logo depois do que eu queria remover
        if(index == 0):
            self.head = after

        # Diminuo um do tamanho da minha lista
        self.len -= 1
        return

    # search
    def search(self, label):
        aux = self.head
        for i in range(self.getLength()):
            if aux.getLabel() == label:
                return i
            aux = aux.getNext()
        return None

    def searchId(self, id):
        aux = self.head
        for i in range(self.getLength()):
            if aux.getLabel().id == id:
                return aux
            aux = aux.getNext()
        return None

    # show
    def show(self):
        if self.empty() != True:  # not self.empty() #self.empty() != True
            print(self.head.getLabel(), end=' ')
            aux = self.head.getNext()
            while aux != self.head:  # for i in range(self.getLength()):
                print(aux.getLabel(), end=' ')
                aux = aux.getNext()
            print()

    def orderById(self):
        aux = self.head
        for i in range(self.getLength()):
            for j in range(self.getLength() - 1):
                if aux.getLabel().id > aux.getNext().getLabel().id:
                    aux.getLabel().id, aux.getNext().getLabel(
                    ).id = aux.getNext().getLabel().id, aux.getLabel().id
                aux = aux.getNext()
            aux = self.head

    # def removeDuplicates(self):
    #     main = self.head
    #     for i in range(self.getLength()):
    #         aux = main.getLabel()
    #         for k in range(i):
    #             aux.getNext()
    #         for j in range(self.getLength() - 1 - i):
    #             if main.getLabel().id == aux.getLabel().id:

    #             aux = aux.getNext()
    #         aux = self.head

    def copy(self):
        newList = CircularLinkedList()
        aux = self.head
        for i in range(self.getLength()):
            newList.append(aux.getLabel())
            aux = aux.getNext()
        return newList

    def orderAlphabetically(self):
        aux = self.head
        for i in range(self.getLength()):
            for j in range(self.getLength() - 1):
                if (aux.getLabel().name.upper() == aux.getNext().getLabel().name.upper()):
                    pass
                elif min(aux.getLabel().name.upper(), aux.getNext().getLabel().name.upper()) == aux.getNext().getLabel().name.upper():
                    tempName = aux.getLabel().name
                    tempId = aux.getLabel().id
                    tempAge = aux.getLabel().age
                    tempWeight = aux.getLabel().weight
                    tempHeight = aux.getLabel().height
                    aux.getLabel().name = aux.getNext().getLabel().name
                    aux.getLabel().id = aux.getNext().getLabel().id
                    aux.getLabel().age = aux.getNext().getLabel().age
                    aux.getLabel().weight = aux.getNext().getLabel().weight
                    aux.getLabel().height = aux.getNext().getLabel().height
                    aux.getNext().getLabel().name = tempName
                    aux.getNext().getLabel().id = tempId
                    aux.getNext().getLabel().age = tempAge
                    aux.getNext().getLabel().weight = tempWeight
                    aux.getNext().getLabel().height = tempHeight

                    # aux.getLabel().name, aux.getNext().getLabel(
                    # ).name = aux.getNext().getLabel().name, aux.getLabel().name
                aux = aux.getNext()
            aux = self.head

    def printPerson(self):
        aux = self.head
        for i in range(self.getLength()):
            print(f"{aux.getLabel().id} {aux.getLabel().name} {aux.getLabel().age} {aux.getLabel().weight} {aux.getLabel().height}")
            aux = aux.getNext()

    # aux_methods

    def getLength(self):
        return self.len

    def empty(self):
        if self.getLength() == 0:
            return True
        return False

    def compare(self, lista):
        if self.getLength() != lista.getLength():
            return False
        aux = self.head
        aux2 = lista.head
        for i in range(self.getLength()):
            if aux.getLabel() != aux2.getLabel():
                return False
            aux = aux.getNext()
            aux2 = aux2.getNext()
        return True


N = int(input())
LSEC = CircularLinkedList()
for i in range(N):
    _frase = input()
    numbers = re.findall(
        r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", _frase)
    nome = [word for word in _frase.split() if word.isalpha()]
    nome = ' '.join(nome)

    _frase = _frase.split()

    if _frase[0].isnumeric() == False:
        continue

    for j in range(len(numbers)):
        numbers[j] = float(numbers[j])

    if (LSEC.searchId(int(numbers[0])) == None):
        LSEC.append(Person(int(numbers[0]), nome,
                    int(numbers[1]), int(numbers[2]), numbers[3]))


copia = LSEC.copy()
copia.orderAlphabetically()
copia.printPerson()

# for i in range(N):
#     LSEC1.append(X[i])

# for i in range(M):
#     LSEC2.append(X[N+i])

# print(LSEC1.compare(LSEC2))
