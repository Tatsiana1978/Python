'''
Задание 2.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
'''
class Zero(Exception):

    def __init__(self, text):
        self.text = text

try:
    a = int(input("Введите числитель: "))
    b = int(input("Введите знаменатель: "))
    if b == 0:
        raise Zero("Делить на '0' нельзя")
    else: c = a / b
    print(f'Результат: {c}')
except Zero as err:
    print(err)
except Exception as err:
    print("Ошибка")
    print(err)
