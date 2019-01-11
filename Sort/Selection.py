def change(x, i, j):
    x[i], x[j] = x[j], x[i]


def selectionSort(x):
    for size in reversed(range(len(x))):
        max_i = 0
        for i in range(1, 1+size):
            if x[i] > x[max_i]:
                max_i = i
        change(x, max_i, size)


def selectionSort2(x):
    for start in range(0, len(x)-1):>>
        min_idx = start
        for idx in range(start+1, len(x)):
            if x[idx] < x[min_idx]:
                min_idx = idx
        x[start], x[min_idx] = x[min_idx], x[start]
    return x


x[9]
x[8]
x = [5, 2, 10, 4, 9, 17, 1, 7, 12, 20]
selectionSort2(x)
print(x)