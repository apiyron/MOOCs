'''
Простейшая система проверки орфографии основана
на использовании списка известных слов.
Каждое слово в проверяемом тексте ищется в этом списке и,
если такое слово не найдено, оно помечается, как ошибочное.
Напишем подобную систему.
Через стандартный ввод подаётся следующая структура:
первой строкой — количество d записей в списке известных слов,
после передаётся  d строк с одним словарным словом на строку,
затем — количество l строк текста, после чего — l строк текста.
Напишите программу, которая выводит слова из текста,
которые не встречаются в словаре. Регистр слов не учитывается.
Порядок вывода слов произвольный.
Слова, не встречающиеся в словаре,
не должны повторяться в выводе программы.
Sample Input:
3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa
Sample Output:
aab
aba
c
aaa
'''

words_num = int(input())
words_dict = set()
for i in range(words_num):
    words_dict.add(input().lower())
lines_num = int(input())
texts = ''
for i in range(lines_num):
    texts += (input()+' ')
text_all = []
text_all = [word for word in texts.split(' ')]
del text_all[-1]
words_incorrect = set()
for word in text_all:
    if word.lower() not in words_dict:
        words_incorrect.add(word)
for word_incorrect in words_incorrect:
    print(word_incorrect)























