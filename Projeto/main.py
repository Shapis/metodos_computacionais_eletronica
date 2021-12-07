import datetime
from mcetoolbox import simplelinkedlist
from mcetoolbox import sort
import random
import timeit


def getTimer(func, *args):

    start = timeit.default_timer()
    func(*args).showUpTo(10)
    end = timeit.default_timer()
    return (end - start)


def formatTime(t):
    return str(datetime.timedelta(seconds=t))


def formatOutput(listas):
    print("\nTempo de execução de lista ascendente: " + formatTime(listas[0]))
    print("Tempo de execução de lista descendente: " + formatTime(listas[1]))
    print("Tempo de execução de lista aleatória: " + formatTime(listas[2]))
    print("\nTempo médio: " +
          formatTime((listas[0] + listas[1] + listas[2]) / 3))
    print()
    print()


def runTests(sllRandom, sllAscending, sllDescending, n):
    timesList = []
    _sorter = sort.Sort()
    print(
        "Numero de elementos: " + str(n) + "\n")
    print("Algoritmo utilizado: " + "Bubble Sort\n")
    timesList.append(getTimer(_sorter.bubbleSort, sllAscending.copy()))
    timesList.append(getTimer(_sorter.bubbleSort, sllDescending.copy()))
    timesList.append(getTimer(_sorter.bubbleSort, sllRandom.copy()))
    formatOutput(timesList)
    timesList.clear()
    print("Algoritmo usado: " + "Shell Sort\n")
    timesList.append(getTimer(_sorter.shellSort, sllAscending.copy()))
    timesList.append(getTimer(_sorter.shellSort, sllDescending.copy()))
    timesList.append(getTimer(_sorter.shellSort, sllRandom.copy()))
    formatOutput(timesList)
    timesList.clear()
    print("Algoritmo usado: " + "Selection Sort\n")
    timesList.append(getTimer(_sorter.selectionSort, sllAscending.copy()))
    timesList.append(getTimer(_sorter.selectionSort, sllDescending.copy()))
    timesList.append(getTimer(_sorter.selectionSort, sllRandom.copy()))
    formatOutput(timesList)
    timesList.clear()
    print("Algoritmo usado: " + "Insertion Sort\n")
    timesList.append(getTimer(_sorter.insertionSort, sllAscending.copy()))
    timesList.append(getTimer(_sorter.insertionSort, sllDescending.copy()))
    timesList.append(getTimer(_sorter.insertionSort, sllRandom.copy()))
    formatOutput(timesList)
    timesList.clear()
    print("----------------------------\n\n\n")


for i in range(5):
    _sllRandom = simplelinkedlist.SimpleLinkedList()
    _sllAscending = simplelinkedlist.SimpleLinkedList()
    _sllDescending = simplelinkedlist.SimpleLinkedList()
    n = 100*(2**i)
    for j in range(n):
        _sllRandom.insertEnd(random.randint(-n, n))
    for j in range(n):
        _sllAscending.insertEnd(j - n/2)
    for j in range(n, 0, -1):
        _sllDescending.insertEnd(j - 1 - n/2)
    runTests(_sllRandom, _sllAscending, _sllDescending, n)
