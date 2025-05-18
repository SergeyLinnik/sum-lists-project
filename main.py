# Ввод двух списков чисел
list1 = list(map(int, input("Введите первый список чисел через пробел: ").split()))
list2 = list(map(int, input("Введите второй список чисел через пробел: ").split()))

# Создание нового списка
result = []

# Определяем минимальную длину для сложения
min_len = min(len(list1), len(list2))

# Складываем элементы до минимальной длины
for i in range(min_len):
    result.append(list1[i] + list2[i])

# Добавляем оставшиеся элементы более длинного списка
if len(list1) > len(list2):
    result.extend(list1[min_len:])
else:
    result.extend(list2[min_len:])

# Вывод результата
print("Результирующий список:")
print(result)
