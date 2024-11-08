# TODO решите задачу
import json

FILENAME = 'input.json'


def task() -> float:
    with open(FILENAME, 'r') as inp:
        in__ = json.load(inp)

    res = [i['score'] * i['weight'] for i in in__]
    return round(sum(res), 3)


print(task())
