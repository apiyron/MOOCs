fig = input()
if fig == "треугольник": i = 3
elif fig == "прямоугольник": i = 2
elif fig == "круг": i = 1

x = []
for i in range(0, i):
    x.append(float(input()))
i += 1 #для правильного отображения количества сторон
if i == 1:
    s = 3.14 * (x[i-1] ** 2)
elif i == 2:
    s = x[i-2] * x[i-1]
elif i == 3:
    p = (x[i-3] + x[i-2] + x[i-1]) / 2
    s = (p * (p - x[i-3]) * (p - x[i-2]) * (p - x[i-1])) ** (1/2)
print(s)
