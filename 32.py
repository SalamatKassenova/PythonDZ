# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def listIndexes(array, min, max):
    indexes = []
    for i in range(len(array)):
        if min <= array[i] <= max:
            indexes.append(i)
    return indexes

array = [int(num) for num in input("Введите элементы массива через пробел: ").split()]
min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))

result = listIndexes(array, min, max)
print(result)