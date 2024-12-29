# Задание:
# Напишите программу, которая получает от пользователя строку целых чисел, и выводит:
# 	•	Количество положительных чисел.
# 	•	Произведение всех отрицательных чисел.
# 	•	Минимальное и максимальное числа без использования функций min() и max().

line = input("Введите строку целых чисел через пробел: ") # например: 3 7 -8 78 -67 112
#line = '3 -6 -7 -3 -2 45 65 324 -1 1'
# инициализация переменных
numbers = []
negativeCounter = 0
negativeMultiplier = 0

# преобразование строки в массив чисел
strings = line.split(' ')
for myStr in strings:
    numbers.append(int(myStr))

# инициализация переменных
maxNumber = numbers[0]
minNumber = numbers[0]

for number in numbers:
    if number < 0:
        negativeCounter += 1
        # если нет отрицательных элементов, то произведение 0
        negativeMultiplier = negativeMultiplier*number if negativeCounter > 1 else number

    # находим максимальное и минимальное значение
    maxNumber = maxNumber if number < maxNumber else number
    minNumber = minNumber if number > minNumber else number

print(f"\tКоличество положительных чисел: {len(numbers) - negativeCounter}\n"
      f"\tПроизведение всех отрицательных чисел: {negativeMultiplier}\n"
      f"\tМинимальное число: {minNumber}\n"
      f"\tМаксимальное число: {maxNumber}")