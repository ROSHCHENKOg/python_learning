# TODO решите задачу
import json
def q() -> float:
    fname = "input.json"
    with open(fname) as f:
        data = json.load(f)
        result = sum(i['score'] * i['weight'] for i in data)
        return round(result, 3)

print(q())

"""
Как будто бы сложность ЛР не совсем одинаковая, 
3 задание в 3 ЛР было прям на 9/10 по сложности, а это намного легче, 
но возможно мне опять кажется....
"""
