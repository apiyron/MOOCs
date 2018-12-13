'''
Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, 
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
2:
1 2
4 3

3:
1 2 3
8 9 4
7 6 5

4:
1   2  3  4
12 13 14  5
11 16 15  6
10  9  8  7

5:
1   2  3  4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

6:
1   2  3  4  5 6
20 21 22 23 24 7
19 32 33 34 25 8
18 31 36 35 26 9
17 30 29 28 27 10
16 15 14 13 12 11
'''
n = int(input())
def print_res():
    res = ''
    for i in range(n):
        for j in range(n):
            res += str(a[i][j]) + ' '
        res += '\n'
    print(res[:-2])
a = [[j for j in range(n)] for i in range(n)]
i = 0
c = n
num = 1
run = 0
while (num <= n*n):
    for j in range(run, c+run):
        a[i][j] = num
        num += 1
    c -= 1
    for i in range(n-c-run, n-run):
        a[i][j] = num
        num += 1
    for j in range(c+run-1, run-1, -1):
        a[i][j] = num
        num += 1
    c -= 1
    for i in range(c+run, run, -1):
        a[i][j] = num
        num += 1
    run += 1
print_res()













