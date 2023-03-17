s = int(input('Сумма этих чисел равна: '))
p = int(input('Произведение этих чисел равно: '))
flag=True
for i in range(s):
    for k in range(s):
        if i+k == s and i*k == p and flag == True:
                print(i, k)
                flag = False
        
