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

    def show(self):
        if self.len_queue != 0:
            for i in self.queue:
                print(i, end=' ')
            print()


lista = list(map(int, input().split()))

_queue = Queue()
_multiplosTres = Queue()
_multiplosCinco = Queue()
_Avulsos = Queue()

size = 0
for item in lista:
    _queue.enqueue(item)
    size += 1

for item in range(size):
    _temp = _queue.dequeue()
    if _temp % 3 == 0:
        _multiplosTres.enqueue(_temp)
    if _temp % 5 == 0:
        _multiplosCinco.enqueue(_temp)
    if (_temp % 5 != 0 and _temp % 3 != 0):
        _Avulsos.enqueue(_temp)

print(_multiplosTres.queue)
print(_multiplosCinco.queue)
print(_Avulsos.queue)
