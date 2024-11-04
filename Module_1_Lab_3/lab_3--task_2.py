# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(participants_first_group_, participants_second_group_, fig=','):
    first = []
    second = []

    for i in participants_first_group_.split(fig):
        first.append(i)

    for i in participants_second_group_.split(fig):
        second.append(i)

    res = []
    for i in first:
        if i in second:
            res.append(i)
    res.sort()
    return res


if __name__ == '__main__':
    print("Общие участники:", *find_common_participants(participants_first_group, participants_second_group, '|'))
    
