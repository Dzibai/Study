from random import randint
size = 10
arr = [randint(-100, 100) for i in range(size)]
print(arr)


def sorting(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


print(sorting(arr))
