
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

    def insertOrdered(self, data):
        node = Node(data)

        # lista vazia
        if self.len == 0:
            self.head = node
        else:
            # inserir no começo
            if node.getData() < self.head.getData():
                node.setNext(self.head)
                self.head = node
            else:
                # inserir no meio
                aux1 = self.head
                aux2 = self.head.getNext()
                flag_add = False
                while aux2 != None:
                    if node.getData() < aux2.getData():
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
            print(aux.getData(), end=' ')
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

_frase = list(map(int, input().split()))

for i in range(len(_frase)):
    sll.insertOrdered(_frase[i])


# sll.show()
sll2 = sll.copy()
sll2.reverse()
sll2.show()
