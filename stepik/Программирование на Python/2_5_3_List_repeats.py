'''
Напишите программу, которая принимает на вход список чисел в одной строке
и выводит на экран в одну строку значения, которые повторяются в нём
более одного раза.
Для решения задачи может пригодиться метод sort списка.
Порядок вывода повторяющихся элементов может быть произвольным.
Sample Input 1:
4 8 0 3 4 2 0 3
Sample Output 1:
0 3 4
Sample Input 2:
10
Sample Output 2:

Sample Input 3:
1 1 2 2 3 3
Sample Output 3:
1 2 3
'''
a = []
for i in input().split():
    a.append(int(i))
a.sort()
res = []
i = 1
count = 0
while i < len(a):
    while (a[i] == a[i-1]) :
        count += 1
        del(a[i-1])
        i -= count
    if (count > 0) and (len(res) == 0): res.append(a[i])
    elif (count > 0) and (a[i] != res[-1]): res.append(a[i])
    count = 0
    i += 1
out = ''
for i in range(len(res)):
    out += str(res[i]) + ' '
print(out)
