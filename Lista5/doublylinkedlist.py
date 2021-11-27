class Node:
    def __init__(self, label):
        self.prev = None
        self.label = label
        self.next = None

    def getPrev(self):
        return self.prev

    def getLabel(self):
        return self.label

    def getNext(self):
        return self.next

    def setPrev(self, prev):
        self.prev = prev

    def setLabel(self, label):
        self.label = label

    def setNext(self, next):
        self.next = next


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def insert(self, label):
        node = Node(label)

        # lista vazia
        if self.empty() == True:
            self.head = node
        else:
            # inserir no começo
            if node.getLabel()[1] > self.head.getLabel()[1]:
                self.head.setPrev(node)
                node.setNext(self.head)
                self.head = node
            else:
                # inserir no meio
                aux1 = self.head
                aux2 = self.head.getNext()
                flag_add = False
                while aux2 != None:
                    if node.getLabel()[1] > aux2.getLabel()[1]:
                        node.setPrev(aux1)
                        node.setNext(aux2)  # node.setNext(aux1.getNext())
                        aux1.setNext(node)
                        aux2.setPrev(node)
                        flag_add = True
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
                # inserir no final
                if flag_add == False:
                    aux1.setNext(node)
                    node.setPrev(aux1)
        self.len += 1

    def removeLast(self):
        if self.empty() == False:
            aux = self.head
            while aux.getNext() != None:
                aux = aux.getNext()
            aux.setNext(None)
            self.len -= 1

    def removeFirst(self):
        if self.empty() == False:
            self.head = self.head.getNext()
            self.head.setPrev(None)
            self.len -= 1

    def remove(self, label):
        # não remover de uma lista vazia ou um índice maior que a lista
        if self.search(label) != False:
            # remover uma lista com apenas 1 elemento
            # self.len == 1
            if self.head.getLabel()[0] == label and self.head.getNext() == None:
                self.head = None
            # remover o primeiro elemento da lista
            elif self.head.getLabel()[0] == label:
                self.head = self.head.getNext()
                self.head.setPrev(None)
            # remover do meio ou final da lista
            else:
                aux1 = self.head
                aux2 = self.head.getNext()
                while aux2 != None:
                    if aux2.getLabel() == label:
                        # aux1.setNext(aux2.getNext()) OOOOOU
                        aux2 = aux2.getNext()
                        aux1.setNext(aux2)
                        if aux2 != None:
                            aux2.setPrev(aux1)
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
            self.len -= 1

    def showAll(self):
        if self.empty() == False:
            aux = self.head
            while aux.getNext() != None:
                print(
                    f'Descricao: {aux.getLabel()[0]}, Prioridade: {aux.getLabel()[1]}')
                aux = aux.getNext()
            print(
                f'Descricao: {aux.getLabel()[0]}, Prioridade: {aux.getLabel()[1]}')

    def show(self, label):
        aux = self.head
        while aux != None:
            if aux.getLabel() == label:
                print(aux.getLabel(), end=' ')
                break
            aux = aux.getNext()

    def search(self, label):
        aux = self.head
        while aux != None:
            if aux.getLabel() == label:
                return aux
                break
            aux = aux.getNext()
        return None

    def searchName(self, label):
        count = 0
        aux = self.head
        while aux != None:
            if aux.getLabel()[0] == label:
                return count
                break
            count += 1
            aux = aux.getNext()
        return None

    def searchByName(self, label):
        count = 0
        aux = self.head
        while aux != None:
            if aux.getLabel()[0] == label:
                return aux
            count += 1
            aux = aux.getNext()
        return None

    def searchPriority(self, label):
        aux = self.head
        while aux != None:
            if aux.getLabel()[1] == label:
                print(f"Descrição : {aux.getLabel()[0]}")
                break
            aux = aux.getNext()
        return None

    def printPriority(self, label):
        aux = self.head
        count = 0
        while aux != None:
            if aux.getLabel()[1] == label:
                print(f"Descrição : {aux.getLabel()[0]}")
                count += 1
            aux = aux.getNext()
        if count == 0:
            print('nenhuma tarefa como esse prioridade foi encontrada')
        return None

    def alter(self, label, newLabel):
        aux = self.searchByName(label)
        aux2 = self.search(newLabel)
        if aux != None and aux2 == None:
            self.removeByName(label)
            self.insertSpecific(newLabel)

    def length(self):
        return self.len

    def empty(self):
        if self.head == None:  # self.length() == 0
            return True
        return False

    def removeByName(self, label):
        # não remover de uma lista vazia ou um índice maior que a lista
        if self.searchByName(label) != False:
            # remover uma lista com apenas 1 elemento
            # self.len == 1
            if self.head.getLabel()[0] == label and self.head.getNext() == None:
                self.head = None
            # remover o primeiro elemento da lista
            elif self.head.getLabel()[0] == label:
                self.head = self.head.getNext()
                self.head.setPrev(None)
            # remover do meio ou final da lista
            else:
                aux1 = self.head
                aux2 = self.head.getNext()
                while aux2 != None:
                    if aux2.getLabel() == label:
                        # aux1.setNext(aux2.getNext()) OOOOOU
                        aux2 = aux2.getNext()
                        aux1.setNext(aux2)
                        if aux2 != None:
                            aux2.setPrev(aux1)
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
            self.len -= 1

    def insertSpecific(self, label):
        node = Node(label)

        # lista vazia
        if self.empty() == True:
            self.head = node
        else:
            # inserir no começo
            if node.getLabel() > self.head.getLabel():
                self.head.setPrev(node)
                node.setNext(self.head)
                self.head = node
            else:
                # inserir no meio
                aux1 = self.head
                aux2 = self.head.getNext()
                flag_add = False
                while aux2 != None:
                    if node.getLabel() > aux2.getLabel():
                        node.setPrev(aux1)
                        node.setNext(aux2)  # node.setNext(aux1.getNext())
                        aux1.setNext(node)
                        aux2.setPrev(node)
                        flag_add = True
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
                # inserir no final
                if flag_add == False:
                    aux1.setNext(node)
                    node.setPrev(aux1)
        self.len += 1


dll = DoublyLinkedList()
opcao = ''

while(opcao != 'H'):
    _input = input().split()
    opcao = _input[0]
    if opcao == 'H':
        print("programa encerrado")
        break
    if opcao == 'A':
        _frase = [_input[1], int(_input[2])]
        if _frase[1] > 10 or _frase[1] < 1:
            print("tarefa não inserida por não ter prioridade válida")
        elif (dll.search(_frase) == None):
            dll.insert(_frase)
            print("tarefa adicionada com sucesso")
        else:
            print("já tem uma atividade com essa descrição")
    elif opcao == 'B':
        _frase = _input[1]
        print(
            f'serão executadas {dll.searchName(_frase)} tarefas antes da informada')
    elif opcao == 'C':
        dll.removeFirst()
        print("Tarefa executada")
    elif opcao == 'D':
        _frase = _input[1]
        dll.remove(_frase)
        print("Tarefa removida")
    elif opcao == 'E':
        _frase = int(_input[1])
        dll.printPriority(_frase)
    elif opcao == 'F':
        dll.showAll()
    elif opcao == 'G':
        _frase = [_input[1], int(_input[2])]
        if _frase[1] <= 10 and _frase[1] >= 1:
            dll.alter(_frase[0], _frase)
            print("tarefa alterada com sucesso")
        else:
            print("tarefa não alterada por não ter prioridade válida")
