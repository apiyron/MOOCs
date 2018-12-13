a = float(input())
b = float(input())
oper = str(input())

if oper == "+": res = a + b
elif oper == "-": res = a - b
elif oper == "/":
    if b != 0: res = a / b
    else: res = "Деление на 0!"
elif oper == "*": res = a *b
elif oper == "mod":
    if b != 0: res = a % b
    else: res = "Деление на 0!"
elif oper == "pow": res = a ** b
elif oper == "div":
    if b != 0: res = a // b
    else: res = "Деление на 0!"

print(res)
