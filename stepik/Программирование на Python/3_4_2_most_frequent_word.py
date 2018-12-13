'''
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть,
как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла
(в файле может быть больше одной строки) и выводит
самое частое слово в этом тексте и через пробел то,
сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое
(можно использовать оператор < для строк).
Слова, написанные в разных регистрах, считаются одинаковыми.
Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
'''
with open('dataset_3363_3.txt', 'r') as f:
    content = f.read().splitlines()
# content = ['abc a bCd bC AbC BC BCD bcd ABC']
d = {}
for line in content:
    line = line.split()
    for word in line:
        word = word.lower()
        # print(d)
        # print(word)
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] += 1
oftenest = 0
for key, value in d.items():
    if value > oftenest:
        oftenest = value
mosts = []
for key, value in d.items():
    if value == oftenest:
        mosts.append(key)
mosts.sort()
print(mosts[0], oftenest)








