#Задача №1
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c))**0.5
print(S)
"""
Возможно добавить условие проверки валидности треугольника:
if a+b>c and a+c>b and b+c>a:
  p=(a+b+c)/2
  s=(p*(p-a)*(p-b)*(p-c))**0.5
  print (s)
else:
  print ('Не выполнено неравенство треугольника')
"""