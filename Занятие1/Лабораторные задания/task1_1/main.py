DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input())  # TODO запросить у пользователя год рождения
current_year = int(input())  # TODO запросить у пользователя текущий год

# TODO посчитать и распечатать количество прожитых дней
days = (current_year - start_year) * DAYS_OF_YEAR
print(days)