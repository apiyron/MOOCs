# Дан упорядоченный по возрастанию массив различных целых чисел A[1…n]:
# A[1]<A[2]<…<A[n]. Необходимо за время O(n^2) проверить,
# найдутся ли такие 1≤i,j,k≤n (возможно, равные), что A[i]+A[j]+A[k]=0.

A = input()
A = list(A.split())
for i in range (0, len(A)):
    A[i] = int(A[i])
n = A[0]
print(n)
print(A)
