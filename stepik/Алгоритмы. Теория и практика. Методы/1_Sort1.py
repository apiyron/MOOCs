# Первая строка содержит число n (1≤n≤10000), вторая – n 
# натуральных чисел, не превышающих 10.
# Необходимо вывести упорядоченную по неубыванию 
# последовательность этих чисел (числа должны быть разделены пробелами).

n = int(input())
input_list = input()
input_list = list(input_list.split())
del input_list[n:len(input_list)] #end of the input

for i in range(0, n):
    input_list[i] = int(input_list[i]) #string to integer
#print(input_list) 

s = []
for i in range(0, 11):
    s.append(0) #counting list initialization
for i in range(0, n):
    j = input_list[i]
    s[j] += 1 #counting list
#print(s) 

sorted_list = []
for i in range(0, len(s)):
    if s[i] > 0:
        for j in range(0, s[i]):
            sorted_list.append(i) 
#print(sorted_list)

out = ''
for i in range (0, len(sorted_list)):
    if i != len(sorted_list):
        out += str(sorted_list[i]) + ' '
    else:
        out += str(sorted_list[i])
print(out)
