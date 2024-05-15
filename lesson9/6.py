# Дан словарь наблюдения за температурой 
# {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
# Отсортировать словарь по температуре в порядке возрастания и обратно.

temp = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

sorted_temp = dict(sorted(temp.items(), key=lambda item: item[1]))
print(sorted_temp)