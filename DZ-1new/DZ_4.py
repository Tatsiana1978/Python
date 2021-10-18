# Задание 4.
# Пользователь вводит целое положительное число
number = int((input("Введите  целое положительное число: ")))
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
max_num = 0
while number > 0:
    num = number % 10
    if max_num < num:
        max_num = num
    if num == 9:
        break
    number = (number - max_num) / 10
print(f'Максимальное число - {max_num}')
