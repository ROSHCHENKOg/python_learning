# TODO Напишите функцию find_common_participants
def find_common_participants(team1, team2, r=','):
    t1 = set(team1.split(r))
    t2 = set(team2.split(r))
    intersection = (list(t1.intersection(t2)))
    intersection.sort()
    return intersection

"""
    Долго не мог додуматься, что нужно задать значение третьей переменной,
    хорошо что подсказки есть, когда задание проверяешь
"""

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
