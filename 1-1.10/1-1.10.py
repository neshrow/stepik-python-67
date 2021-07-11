#Блок 1-1.10
#Задание №1
A = int(input())
B = int(input())
H = int(input())
if A <= H <= B:
    print('Это нормально')
elif H < A:
    print('Недосып')
elif H > B:  #Можно не указывать услови H > B
    print('Пересып')
#Задание №2
Y = int(input())
if Y % 4 == 0 and Y % 100 != 0:
    print('Високосный')
elif Y % 4 == 0 and Y % 100 == 0 and Y % 400 == 0:
    print('Високосный')
else:
    print('Обычный')