# Задание 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data):  # принимает дату в виде строки формата «день-месяц-год».
        self.data = data

    def __str__(self):
        return self.data

    @classmethod
    def data_detal(cls, data):
        cls.data = data
        d = cls.data.split('-')  # получаем список с 3мя элементами
        # day = d[0]
        # month = d[1]
        # year = d[2]
        cls.day = int(d[0])
        cls.month = int(d[1])
        cls.year = int(d[2])
        return f"Дата: {cls.day}.{cls.month}.{cls.year }"

    @staticmethod
    def format_data(day, month, year):
        if day < 1 or day > 31:
            print('Введите дату в диапазоне от 1 до 31 включительно')
        elif month < 1 or month > 12:
            print('Введите месяц цифрой в диапазоне от 1 до 12 включительно')
        elif year < 0 or year > 2021:
            print("Введите корректный год")
        else:
            return f'{day:02}/{month:02}/{year:4}'




a = Data('25-10-2000')

print(a)
print(f'Статический метод: \n {a.format_data(31, 12, 2015)}')
print(f"Метод класса: \n {Data.data_detal('25-10-2000')}")
