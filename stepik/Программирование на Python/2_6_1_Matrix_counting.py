'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент 
в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1
Sample Input 2:
1
end
Sample Output 2:
4
'''
a = [[int(i) for i in input().split()]]
b = input()
while b != 'end':
    a.append([int(i) for i in b.split()])
    b = input()
h = len(a)
w = len(a[0])
b = [[j for j in range(w)] for i in range(h)]
for i in range(h):
    for j in range(w):
        b[i][j] = 0
for i in range(h):
    for j in range(w):
        if (h == 1) and (w == 1):
            b[i][j] = a[0][0] * 4
            break
        if (i == 0):
            if (j == 0):  # top left angle (L + R + Up + Down elems)
                b[i][j] = a[0][(w-1)%w] + a[0][1%w] + a[(h-1)%h][0] + a[1%h][0]
            elif (j == w-1) and ((h <= 2) or (w <= 2)):  # top right angle
                b[i][j] = a[0][(w-2)%w] + a[0][0] + a[(h-1)%h][(w-1)%w] + a[1%h][(w-1)%w]
            else:  # top elements
                b[i][j] = a[i][(j-1)%w] + a[i][(j+1)%w] + a[(h-1)%h][j] + a[1%h][j]
            continue
        if (i == h-1):
            if (j == 0):  # bottom left angle
                b[i][j] = a[(h-1)%h][(w-1)%w] + a[(h-1)%h][1%w] + a[(h-2)%h][0] + a[0][0]
            elif (j == w-1) and ((h <= 2) or (w <= 2)):  # bottom right angle
                b[i][j] = a[(h-1)%h][(w-2)%w] + a[(h-1)%h][0] \
                    + a[(h-2)%h][(w-1)%w] + a[0][(w-1)%w]
            else:
                b[i][j] = a[i][(j-1)%w] + a[i][(j+1)%w] + a[h-2][j] + a[0][j]
            continue
        elif (j == 0) and ((h >= 3) or (w >= 3)):
            b[i][j] = a[i%h][(w-1)%w] + a[i%h][1%w] + a[(i-1)%h][j] + a[(i+1)%h][j]
        elif (j == w-1) and ((h >= 3) or (w >= 3)):
            b[i][j] = a[i][(w-2)%w] + a[i][0] + a[i-1][j] + a[i+1][j]
        else:
            b[i][j] = a[i][j-1] + a[i][j+1] + a[i-1][j] + a[i+1][j]
res = ''
for i in range(h):
    for j in range(w):
        res += str(b[i][j]) + ' '
    res += '\n'
print(res[:-2])
