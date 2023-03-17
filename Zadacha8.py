#Задача 8: 

n = int(input('Введите количество долек по горизонтпли: '))
m = int(input('Введите количество долек по вертикали: '))
k = int(input('Сколько долек вы хотите получить за 1 разлом: '))

flag = True
if n<m:
    i=n
    x=m
else:
    i=m
    x=n
sum = int(n*m)
if k == sum:
    flag = False
    print('у вас и так столько долек, разламывать не надо')  
elif k>sum:
    flag = False
    print('в вашем шоколаде нет столько долек, купите еще шоколада')  
while flag:
    if (k<sum and k%i == 0 and k>=i) or (k<sum and k%x == 0 and k>=x) :
        flag = False
        print('yes')
    else:
        print('no')
        flag = False