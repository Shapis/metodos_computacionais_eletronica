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

    def pushCapitalLetter(self, e):
        self.stack.append(str(e).upper())
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
                print(i, end='')
            print()

    def get(self):
        return self.stack

    def length(self):
        return self.len_stack

    def reverse(self):
        _temp = []
        for i in range(self.len_stack):
            _temp.append(self.stack.pop())
        self.stack = _temp

    def isPalindrome(self):
        if self.len_stack != 0:
            if self.stack == self.stack[::-1]:
                return True
            else:
                return False


_input = int(input())
_base = int(input())
_stack = Stack()


while(_input != 0):
    _stack.pushInt(_input % _base)
    _input = int(_input/_base)


_stack.reverse()
_stack.show()
