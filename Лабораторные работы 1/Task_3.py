list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
members_in_one_team = len(list_players) // 2 #находим серединную точку, от и до которой будем считать
first_team = list_players[:members_in_one_team] #считаем....
second_team = list_players[members_in_one_team:] #считаем....
print(f"Состав первой команды: {first_team} \nCостав второй команды: {second_team}") #получаем

"""Наверное проще записать это в две команды "принт", но раз научились такой функции,
   то почему бы и нет:)"""
