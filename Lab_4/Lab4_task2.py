# TODO импортировать необходимые молули

import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as f:  # TODO считать содержимое csv файла
        data = [dat for dat in csv.DictReader(f)]
    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(data, f, indent=4)  # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    # А кто проверит?)
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
