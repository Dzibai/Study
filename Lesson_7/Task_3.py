from random import randint
size = 11
limit = 100
arr = [randint(-limit, limit) for i in range(size)]
print(arr)


def median(array):
    result = []
    for i in range(min(array), max(array)):
        if i in array:
            result.append(i)
    return result[int(len(result) / 2)]


print(f'Медиана - {median(arr)}')
