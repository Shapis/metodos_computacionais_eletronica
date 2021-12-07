import datetime
from mcetoolbox import simplelinkedlist
from mcetoolbox import sort
import random
import timeit


def runWithTimer(func, *args):
    start = timeit.default_timer()
    func(*args).showUpTo(5)
    end = timeit.default_timer()

    print(
        f'Tempo de execução: {str(datetime.timedelta(seconds=end - start))}\n')


def runTests(sll, n):
    _sorter = sort.Sort()
    print(
        "Numero de elementos: " + str(n) + "\n")
    print("Algoritmo usado: " + "Bubble Sort")
    runWithTimer(_sorter.bubbleSort, sll.copy())
    print("Algoritmo usado: " + "Shell Sort")
    runWithTimer(_sorter.shellSort, sll.copy())
    print("Algoritmo usado: " + "Selection Sort")
    runWithTimer(_sorter.selectionSort, sll.copy())
    print("Algoritmo usado: " + "Insertion Sort")
    runWithTimer(_sorter.insertionSort, sll.copy())
    print("----------------------------")


for i in range(5):
    _sll = simplelinkedlist.SimpleLinkedList()
    n = 100*(2**i)
    for j in range(n):
        _sll.insertEnd(random.randint(-n, n))
    runTests(_sll, n)


# n *= 10
# for i in range(n):
#     _sll5.insertEnd(random.randint(-n, n))

# n *= 10
# for i in range(n):
#     _sll6.insertEnd(random.randint(-n, n))

# n *= 10
# for i in range(n):
#     _sll7.insertEnd(random.randint(-n, n))
