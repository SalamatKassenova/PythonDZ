# def listPowers(a):
#     powers = list()
#     for i in a:
#         if i % 2 == 0:
#             powers.append((i, i**2))
#     return powers

# a = [int(num) for num in input("введите список чисел: ").split()]
# result = listPowers(a)
# print(result)



# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x%2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)



list1 = [x for x in range(1,20)]
print(list1)

list1 = list(map(lambda x: x+10, list1))
print(list1)