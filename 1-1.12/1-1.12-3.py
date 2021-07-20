#Задача №3
a = float(input('Введите число a: '))
b = float(input('Введите число b: '))
z = input('Введите знак операции (+, -, /, *, mod, pow, div): ')
if z == '+':
    print(a + b)
elif z == '-':
    print(a - b)
elif z == '*':
    print(a * b)
elif z == '/':
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
elif z == 'mod':
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')
elif z == 'pow':
    print(a**b)
elif z == 'div':
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')

"""
Упрощенная проверка на 0 при делении:

a = float(input())
b = float(input())
act = input()

if (act=="/" or act=="mod" or act=="div") and b==0:
    c = "Деление на 0!"
elif act=="+":    c = a + b
elif act=="-":    c = a - b
elif act=="/":    c = a / b
elif act=="*":    c = a * b
elif act=="mod":  c = a % b
elif act=="pow":  c = a ** b
elif act=="div":  c = a // b

print (c)
"""
