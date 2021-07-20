#Задача №4
figure = input()
if figure == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c))**0.5
    print(S)
elif figure == 'прямоугольник':
    a = float(input())
    b = float(input())
    S = a * b
    print(S)
elif figure == 'круг':
    r = float(input())
    S = 3.14 * (r**2)
    print(S)
else:
    print('Такой фигуры нет!')