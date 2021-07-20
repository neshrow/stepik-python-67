#Задача №5
x, y, z = int(input()), int(input()), int(input())
if x >= z >= y:
    print(x, '\n', y, '\n', z)
elif x >= y >= z:
    print(x, '\n', z, '\n', y)
elif y >= z >= x:
    print(y, '\n', x, '\n', z)
elif y >= x >= z:
    print(y, '\n', z, '\n', x)
elif z >= y >= x:
    print(z, '\n', x, '\n', y)
elif z >= x >= y:
    print(z, '\n', y, '\n', x)

"""
Лаконичный вариант из комментариев:

a,b,c = int(input()), int(input()), int(input())
if a < b:
	a, b = b, a
if a < c:
	a, c = c, a
if b > c:
	b, c = c, b
print(a)
print(b)
print(c)
"""