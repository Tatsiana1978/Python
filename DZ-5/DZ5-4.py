# Задание 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("DZ5-4.txt") as file: # извлекаем файл в строку
    f_line_1 = file.readlines()
    i = 0
    f_line_2 = tuple()
    rus_dict = ["Один", "Два", "Три", "Четыре"]

file_1 = open("DZ5-4-1.txt", "w")
file_1.close()
for el in f_line_1:
    item_1 = f_line_1[i].split(" ")
    item_1[0] = rus_dict[i]

    with open("DZ5-4-1.txt", "a") as file_1: # создаем новый файл и записываем
        file_1.writelines(item_1)
    i += 1
with open("DZ5-4-1.txt") as file_1:
    result = file_1.read()
    print(result)

