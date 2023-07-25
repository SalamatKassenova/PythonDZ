def recurisveSum(A, B):
    if A == 0:
        return B
    elif B == 0:
        return A
    else:
        return recurisveSum(A + 1, B - 1)
    
A = int(input("Введите первое целое положительное число: "))
B = int(input("Введите второе целое положительное число, чтобы узнать сумму: "))

result = recurisveSum(A, B)
print(f"сумма {A} и {B} равна: {result}")