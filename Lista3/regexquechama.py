class Queue:  # FIFO => First In, First Out
    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def enqueue(self, e):
        self.queue.append(e)  # ou self.queue.insert(-1, e)
        self.len_queue += 1

    def dequeue(self):
        if self.len_queue != 0:
            self.len_queue -= 1
            return self.queue.pop(0)  # self.queue.remove(0)

    def front(self):
        if self.len_queue != 0:
            return self.queue[0]

    def top(self):
        if self.len_queue != 0:
            return self.queue[-1]

    def show(self):
        if self.len_queue != 0:
            for i in self.queue:
                print(i, end=' ')
            print()

    def isInverso(self):
        return self.len_queue


_lista = list(map(str, input()))
_q = Queue()

for item in _lista:
    _q.enqueue(item)


if (_q.top() == _q.front()):
    print("VERDADE")
else:
    print("FALSO")
