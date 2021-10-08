class Stack:
    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, e):
        self.stack.append(e)
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
        if self.len_stack == 0:
            for i in self.stack:
                print(i, end=' ')
            print()
