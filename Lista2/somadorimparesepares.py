class Stack:
    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1

    def pushInt(self, e):
        self.stack.append(int(e))
        self.len_stack += 1

    def pop(self):
        if self.len_stack != 0:
            self.len_stack -= 1
            return self.stack.pop()

    def top(self):
        if self.len_stack == 0:
            return None
        return self.stack[-1]

    def show(self):
        if self.len_stack != 0:
            for i in self.stack:
                print(i, end=' ')
            print()

    def get(self):
        return self.stack

    def length(self):
        return self.len_stack


_stack = Stack()

_lista = list(map(float, input().split()))

for i in _lista:
    _stack.pushInt(i)

print(_stack.get())

pares = 0
impares = 0

for i in range(_stack.length()):
    e = _stack.pop()
    if (e % 2) == 0:
        pares -= e
    else:
        impares += e

print(impares*pares)

print(_stack.get())
