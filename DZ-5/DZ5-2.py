# Задание 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open("text_1.txt", "w") as text_1:
    context = ["Kate is a girl \n", "Mikle is a boy \n", "Ross \n"]
    text_1.writelines(context)
    print(f"Количество строк: {len(context)}")
text_1 = open("text_1.txt", "r")

i = 0
for line in context:
    content = line.split()
    print(f"Количество слов в строке {i + 1}: {len(content)}")
    i += 1

text_1.close()
print("*" * 30)

#Вариант 2 чтение напрямую из файла, без его создания

with open("text_1.txt") as text_1:
    cont_1 = text_1.readlines()
    print(f"Количество строк: {len(cont_1)}")

i = 0
for line in cont_1:
    content = line.split()
    print(f"Количество слов в строке {i + 1}: {len(content)}")
    i += 1
