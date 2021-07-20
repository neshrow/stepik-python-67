#Задача №7
number = int(input())
first = number // 1000
second = number % 1000
a = first // 100
b = (first // 10) % 10
c = first % 10
d = second // 100
e = (second // 10) % 10
f = second % 10
if a + b + c == d + e + f:
    print('Счастливый')
else:
    print('Обычный')
'''
Лаконичное решение с комментариев на основе пройденного материала:

a, b, c, d, e, f = input()
sumabc = (int(a))+(int(b))+(int(c))
sumdef = (int(d))+(int(e))+(int(f))
if sumabc==sumdef:
    print ("Счастливый")
else:
    print("Обычный")
'''
