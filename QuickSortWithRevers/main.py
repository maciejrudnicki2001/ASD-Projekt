import random

array = []
i = 0
while i < 100000:
    i = i + 1
    array.append(random.randint(-1000000, 1000000))


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

quicksort(array, 0 , len(array) - 1)
print(array)

def quicksort_reverseEdition(A, p, r):
    if p < r:
        q = partition_ReverseEdition(A, p, r)
        quicksort_reverseEdition(A, p, q - 1)
        quicksort_reverseEdition(A, q + 1, r)

def partition_ReverseEdition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
array2 = []
i = 0
while i < 100000:
    i = i + 1
    array2.append(random.randint(-1000000, 1000000))
quicksort_reverseEdition(array2, 0 ,len(array2) - 1)

