money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
b = money_capital + salary
m = 0
while True:
    if b < spend:
        break
    b += salary
    b -= spend
    spend += (increase * spend)
    m += 1
print("Количество месяцев, которое можно протянуть без долгов:", m)
