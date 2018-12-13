n = input()

x = []
for i in range(0, len(n)):
    x.append(int(n[i]))
if (x[0] + x[1] + x[2] == x[3] + x[4] + x[5]):
    print("Счастливый")
else: print("Обычный")
