# В первой строке даны целое число n (1≤n≤100000) и массив
# A[1…n] из n различных натуральных чисел, не превышающих 10^9,
# в порядке возрастания, во второй – целое число k (1≤k≤100000)
# и k натуральных чисел b1,…,bk, не превышающих 10^9. 
# Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n,
# для которого A[j]=bi, или −1, если такого j нет.

A = input()
A = list(A.split())
for i in range (0, len(A)):
    A[i] = int(A[i])
n = A[0]
print(n)
print(A)

k = input()
k = list(k.split())
for i in range (0, len(k)):
    k[i] = int(k[i])
k_len = k[0]
print(k_len)
print(k)

out = []
for i in range (0, k_len):
    out.append(None)
print(out)

for i in range (1, k_len + 1):
    l = 1
    r = n
    j = 0
    if (i == k_len) and (out[i-1] != None): break
    while l <= r:
        print(out)
        j += 1
        m = int(l + float(r - l) / 2)
        print('l='+str(l)+' r='+str(r)+' m='+str(m)+' i='+str(i))
        if j > 20: break
        if A[m] == k[i]:
            out[i-1] = m           
            continue
        elif A[m] > k[i]:
            r = m - 1
            continue
        elif A[m] < k[i]:
            l = m + 1
            continue
        out[i-1] = -1
print(out)

