'''
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму
двух его соседей. Для элементов списка, являющихся крайними,
одним из соседей считается элемент, находящий на противоположном конце
этого списка. Например, если на вход подаётся список "1 3 5 6 10",
то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.
Вывод должен содержать одну строку с числами нового списка,
разделёнными пробелом.
Sample Input 1:
1 3 5 6 10
Sample Output 1:
13 6 9 15 7
Sample Input 2:
10
Sample Output 2:
10
'''
a = []
out = ''
for i in input().split():
    a.append(int(i))
if len(a) > 1: out += str(a[1] + a[-1]) + ' '
for i in range(1, len(a)-1):
    out += str(a[i-1] + a[i+1]) + ' '
if len(a) > 1: out += str(a[-2] + a[0]) + ' '
else: out += str(a[0]) + ' '
print(out)
