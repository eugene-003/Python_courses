# TODO импортировать необходимые молули
import json, csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as inp:
        res = [i for i in csv.DictReader(inp)]

    with open(OUTPUT_FILENAME, 'w') as out:
        json.dump(res, out, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
