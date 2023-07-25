def powerRecursive(A, B):
    if B == 0:
        return 1
    elif B < 0:
        return 1 / powerRecursive(A, -B)
    else:
        return A * powerRecursive(A, B - 1)
    
A = int(input("Введите число, которое хотите возвести в степень: "))
B = int(input("Введите число, в какую степень хотите возвести: "))

result = powerRecursive(A, B)
print(f"{A} в степени {B} будет равно: {result}")