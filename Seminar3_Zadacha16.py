print('Введите количество чисел в списке')
n = int(input())
lst = [i for i in range(1, n+1)]
print('Получился такой список: ' + str(lst))
print('Bведите число, которое хотите проверить сколько раз оно встречается в списке: ')
x = int(input())
print('Оно встречается: ' + str(lst.count(x)) + ' раз')