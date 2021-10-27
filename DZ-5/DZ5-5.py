# Задание 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран

with open("DZ55.txt", "w") as file:
    content = "1 2 3 4 5 6 7 8 9 10"
    file.write(content)
content_1 = content.split(" ")
content_2 = [int(el) for el in content_1]
print(sum(content_2))