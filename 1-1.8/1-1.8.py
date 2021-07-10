#Блок 1-1.8
#Задание №1
X = int(input())
Y = int(input())
print(X * 60 + Y)
#Задание №2
X = int(input())
print(X // 60)
print(X % 60)
#Задание №3
X = int(input())  #желаемое
H = int(input()) * 60  #часы переводим в минуты
M = int(input())  #минуты
total = X + H + M
print(total // 60)
print(total % 60)
