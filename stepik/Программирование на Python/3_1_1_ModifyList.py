# Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать,
# требуется только изменение переданного списка

def modify_list(l):
    length = len(l)
    #print('length =', length)
    i = 0
    while i < length:
        #print('i =',i)
        if (l[i] % 2) != 0:
            #print('continue')
            del l[i]
            length -= 1
            continue
        else:
            l[i] //= 2
        i += 1
#l = [1, 2, 3, 4, 5, 6]
#modify_list(l)
#print(l)
#l = [10, 5, 8, 3]
#modify_list(l)
#print(l)
