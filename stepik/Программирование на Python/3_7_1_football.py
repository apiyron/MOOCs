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
def add_team(team, teams):
    teams.add(team)
    table[team] = {}
    table[team]['Games'] = 0  # Games
    table[team]['Wins'] = 0  # Wins
    table[team]['Draws'] = 0  # Draws
    table[team]['Losses'] = 0  # Losses
    table[team]['Points'] = 0  # Points
matches_num = int(input())
teams = set()
table = {}
for i in range(matches_num):
    match = input()
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
