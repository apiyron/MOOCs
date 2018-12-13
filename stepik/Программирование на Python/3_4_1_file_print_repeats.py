# -*- coding: utf-8 -*-
# !/bin/user/env python
'''
Напишите программу, которая считывает из файла строку,
соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Примечание. Это первое задание типа Dataset Quiz.
В таких заданиях после нажатия "Start Quiz" у вас появляется
ссылка "download your dataset". Используйте эту ссылку для того,
чтобы загрузить файл со входными данными к себе на компьютер.
Запустите вашу программу, используя этот файл в качестве входных данных.
Выходной файл, который при этом у вас получится,
надо отправить в качестве ответа на эту задачу. 
Sample Input:
a3b4c2e10b1
Sample Output:
aaabbbbcceeeeeeeeeeb
aaabbbbcceeeeeeeeeee
'''
with open('res.txt', 'w') as f:
    f.write('')
with open('dataset_3363_2.txt', 'r') as f:
    string = f.readline().strip()
reps = 0
out = ''

def parse(string):
    string += 's'
    char = ''
    reps = 0
    res = ''
    for i in range(len(string)):
        if string[i].isdigit():
            reps = reps*10 + int(string[i])
        else:
            res += char*reps
            char = string[i]
            reps = 0
    return res

print(parse(string))

'''
with open('res.txt', 'w') as f:
    for i in range(0, len(string), 2):
        f.write(string[i]*int(string[i+1]))
'''



















