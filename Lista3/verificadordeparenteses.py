class Stack:
    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, e):  # inserir elemento na pilha
        self.stack.append(e)
        self.len_stack += 1

    def pop(self):  # remover e retornar elemento na pilha
        if self.len_stack != 0:
            self.len_stack -= 1
            return self.stack.pop()

    def top(self):  # exibir o topo da pilha
        if self.len_stack == 0:
            return None
        return self.stack[-1]

    def show(self):
        if self.len_stack != 0:
            for i in self.stack:
                print(i, end=' ')
            print()

    def length(self):
        return self.len_stack


_lista = list(map(str, input()))
_stack = Stack()

for item in _lista:
    if (item == "(" or item == ")"):
        if (_stack.top() == "(" and item == ")"):
            _stack.pop()
        else:
            _stack.push(item)


if _stack.length() == 0:
    print("CERTO")
elif (_stack.top() == "("):
    print("ERRADO: Abre parênteses sem o fecha parênteses correspondente")
elif (_stack.top() == ")"):
    print("ERRADO: Fecha um parênteses sem ter aberto")
