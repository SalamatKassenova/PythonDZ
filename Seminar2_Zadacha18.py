print('Введите количество чисел в списке')
n = int(input())
lst = [i for i in range(1, n+1)]
print('Получился такой список: ' + str(lst))
print('Bведите число, а мы выведем его, либо ближайшее в списке: ')
myNumber = int(input())
print(min(lst, key=lambda x:abs(x-myNumber)))