
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

result1 = "В команде Мастера кода участников: %s !" % team1_num
result2 = "Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num)

result3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
result4 = "Волшебники данных решили задачи за {} с !".format(team2_time)

result5 = f"Команды решили {score_1} и {score_2} задач."
result6 = f"Результат битвы: {challenge_result}"
result7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"

# Вывод результатов
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)