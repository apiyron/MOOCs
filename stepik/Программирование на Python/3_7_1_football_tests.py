'''
Напишите программу, которая принимает на стандартный вход
список игр футбольных команд с результатом матча
и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны
результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1
'''
from_stepik = '''35
Франция;1;Румыния;1
Албания;0;Швейцария;1
Уэльс;2;Словакия;1
Англия;1;Россия;1
Турция;0;Хорватия;1
Польша;1;Северная Ирландия;0
Германия;2;Украина;0
Испания;1;Чехия;0
Бельгия;0;Италия;2
Австрия;0;Венгрия;2
Португалия;1;Исландия;1
Россия;1;Словакия;2
Румыния;1;Швейцария;1
Франция;2;Албания;0
Англия;2;Уэльс;1
Украина;0;Северная Ирландия;2
Германия;0;Польша;0
Италия;1;Швеция;0
Чехия;2;Хорватия;2
Испания;3;Турция;0
Бельгия;3;Ирландия;0
Исландия;1;Венгрия;1
Португалия;0;Австрия;0
Швейцария;0;Франция;0
Румыния;0;Албания;1
Словакия;0;Англия;0
Россия;0;Уэльс;3
Северная Ирландия;0;Германия;1
Украина;0;Польша;1
Хорватия;0;Испания;1
Чехия;0;Турция;2
Венгрия;0;Португалия;3
Исландия;2;Австрия;1
Швеция;1;Бельгия;1
Италия;2;Ирландия;1'''
def add_team(team, teams):
    teams.add(team)
    table[team] = {}
    table[team]['Games'] = 0  # Games
    table[team]['Wins'] = 0  # Wins
    table[team]['Draws'] = 0  # Draws
    table[team]['Losses'] = 0  # Losses
    table[team]['Points'] = 0  # Points
matches = from_stepik.splitlines()
matches_num = int(matches[0])
matches = matches[1:]
print(matches)
teams = set()
table = {}
for i in range(matches_num):
    match = matches[i]
    team_1 = match.split(';')[0]
    team_1_goals = int(match.split(';')[1])
    team_2 = match.split(';')[2]
    team_2_goals = int(match.split(';')[3])
    if team_1 not in teams:
        add_team(team_1, teams)
    if team_2 not in teams:
        add_team(team_2, teams)
    table[team_1]['Games'] += 1  # add game
    table[team_2]['Games'] += 1  # add game
    if team_1_goals > team_2_goals:
        table[team_1]['Wins'] += 1
        table[team_2]['Losses'] += 1
        table[team_1]['Points'] += 3
    elif team_1_goals < team_2_goals:
        table[team_1]['Losses'] += 1
        table[team_2]['Wins'] += 1
        table[team_2]['Points'] += 3
    else:
        table[team_1]['Draws'] += 1
        table[team_2]['Draws'] += 1
        table[team_1]['Points'] += 1
        table[team_2]['Points'] += 1
for team in teams:
    res = ''
    res += team + ':'
    res += str(table[team]['Games']) + ' '
    res += str(table[team]['Wins']) + ' '
    res += str(table[team]['Draws']) + ' '
    res += str(table[team]['Losses']) + ' '
    res += str(table[team]['Points'])
    print(res)
