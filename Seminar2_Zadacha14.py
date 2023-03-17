n = int(input('Введите натуральное число: '))
x = 0
for i in range(n):    
    while x<n:        
        x = 2**i
        i = i+1
        if x<n:
            print(x, end = " ")
    