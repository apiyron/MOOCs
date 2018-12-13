'''
Напишите программу, на вход которой подается одна строка с целыми числами.
Программа должна вывести сумму этих чисел.
Используйте метод split строки. 
Sample Input:
4 -1 9 3
Sample Output:
15
'''

a = []
j = 0
sum = 0
for i in input().split():
    a.append(int(i))
    sum += a[j]
    j += 1
print(sum)
