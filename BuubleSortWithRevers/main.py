import random
def buubleSort(array):

    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

array = []
i = 0
while i < 100000:
    array.append(random.randint(-1000000,1000000))
    i = i + 1

buubleSort(array)
print(array)

def buubleSortReverseEdition(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]