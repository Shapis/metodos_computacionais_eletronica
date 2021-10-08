def bubblesort(l):

    # Swap the elements to arrange in order
    for iter_num in range(len(l)-1, 0, -1):
        for idx in range(iter_num):
            if l[idx] > l[idx+1]:
                temp = l[idx]
                l[idx] = l[idx+1]
                l[idx+1] = temp


meuInput = input()
minhaLista = list(map(float, meuInput.split()))
bubblesort(minhaLista)

print(
    f'{minhaLista[-1]} {minhaLista[-2]} {minhaLista[-3]} {minhaLista[0]} {minhaLista[1]}')
