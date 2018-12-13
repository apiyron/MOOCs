n = int(input())

def endcheck(n):
    end = ""
    if (n % 10 == 0) or (n % 10 >= 5) or (11 <= n % 100 <= 14):
        end = "ов"
    elif (4 >= n % 10 >= 2):
        end = "а"
    return end
if n>=0: print(str(n) + " программист" + endcheck(n))
