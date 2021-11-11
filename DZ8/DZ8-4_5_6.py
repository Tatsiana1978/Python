'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.

'''

class Company:
    count_tehn = 0
    name = "OOO 'Заря'"
    calc = {}
    calc[name] = []

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Central_office(Company):
    name = "Центральный офис"
    # calc = {}
    # calc[name] = []

    def __init__(self, name):
        self.name = name

class Office_region_1(Company):
    name = "Региональный офис №1"
    # calc = {}
    # calc[name] = []

    def __init__(self, name):
        self.name = name

class Office_region_2(Company):
    name = "Региональный офис №2"
    calc = {}
    calc[name] = []

    def __init__(self, name):
        self.name = name


class Sklad(Company):
    name = "Центральный склад"
    calc = {}
    calc[name] = []

    def __init__(self, name):
        self.name = name


class Tehnika:
    count = 0 # всего техники в компании
    name = "Оргтехника"
    dict_inv_num = {} # словарь {инв.номер: владелец}
    keeper = Sklad.name

    def __init__(self, name, model, keeper):
        self.keeper = keeper
        self.name = name
        self.model = model


    def __str__(self):
        return f'Вид оргтехники -{self.name}, модель {self.model}'


    def uchet(self):  #  ([класс техники(имя), инв.номер]: владелец)
        return f"{self.name} модель {self.model} (инв.номер:{self.inv_num_1}) " \
               f"находится в подразделении: {Tehnika.dict_inv_num[self.inv_num_1]}"

    def moving(self, inv_num_1, new_keeper): # смена владельца, или местонахождения устройства
        self.new_keeper = new_keeper
        Tehnika.dict_inv_num[self.inv_num_1] = self.new_keeper
        Company.calc[Company.name].append(self.inv_num_1)
        print(f" Устройство инв.номер: {inv_num_1} перемещено с {self.keeper} в {self.new_keeper}")
        return self.keeper == new_keeper

    def parametrs(self):
        return (f'Информация об устройстве: {self.name} модель {self.model} (инв.номер {self.inv_num_1})')

class Printer(Tehnika):
    name = "Принтер"

    def __init__(self, model, print_type, paper_format, print_color=None):
        self.print_type = print_type
        self.model = model
        self.print_color = print_color
        self.paper_format = paper_format
        Tehnika.count += 1
        self.inv_num_1 = 1000 + Tehnika.count
        Tehnika.dict_inv_num[self.inv_num_1] = Sklad.name

    def parametrs(self):
        return (f'Информация об устройстве: {self.name} модель {self.model} (инв.номер {self.inv_num_1})\n '
                f'Характеристики: тип печати - {self.print_type}, цветной - {self.print_color}, '
                f'формат бумаги - {self.paper_format}, '
                f'находится в подразделении - {self.keeper}')

class Xerox(Tehnika):
    name = "Ксерокс"

    def __init__(self, model, print_type, paper_format, print_color=None):
        self.print_type = print_type
        self.model = model
        self.print_color = print_color
        self.paper_format = paper_format
        Tehnika.count += 1
        self.inv_num_1 = 1000 + Tehnika.count
        Tehnika.dict_inv_num[self.inv_num_1] = Sklad.name

    def parametrs(self):
        return (f'Информация об устройстве: {self.name} модель {self.model} (инв.номер {self.inv_num_1})\n '
                f'Характеристики: тип печати - {self.print_type}, цветной - {self.print_color}, '
                f'формат бумаги - {self.paper_format}, '
                f'находится в подразделении - {self.keeper}')

class Scaner(Tehnika):
    name = "Сканер"

    def __init__(self, model, paper_format, reading_color=None):
        self.paper_format = paper_format
        self.model = model
        self.reading_color = reading_color
        Tehnika.count += 1
        self.inv_num_1 = 1000 + Tehnika.count
        Tehnika.dict_inv_num[self.inv_num_1] = Sklad.name

    def parametrs(self):
        return (f'Информация об устройстве: {self.name} модель {self.model} (инв.номер {self.inv_num_1})\n '
                f'Характеристики: цветной - {self.reading_color}, '
                f'формат бумаги - {self.paper_format}, '
                f'находится в подразделении - {self.keeper}')

class Fax(Tehnika):
    name = "Факс"

    def __init__(self, model, print_type, paper_format, print_color, telefon=True):
        self.print_type = print_type
        self.print_color = print_color
        self.paper_format = paper_format
        Tehnika.count += 1
        self.telefon = telefon
        self.inv_num_1 = 1000 + Tehnika.count
        Tehnika.dict_inv_num[self.inv_num_1] = Sklad.name
        self.model = model

    def parametrs(self):
        return (f'Информация об устройстве: {self.name} модель {self.model} (инв.номер {self.inv_num_1})\n '
                f'Характеристики: тип печати - {self.print_type}, цветной - {self.print_color}, '
                f'формат бумаги - {self.paper_format}, наличие телефона - {self.telefon}, '
                f'находится в подразделении - {self.keeper}')



print("----------Покупаем устройства и Проверяем их параметры:----------")
panasonic = Fax("KF-12", "лазерный", "А4", telefon=True, print_color="нет")
print(panasonic.parametrs())

epson = Printer("Е100", "струйный", "А2", "есть")
print(epson.parametrs())

print("----------Приходуем их на склад----------")
print(panasonic.uchet())
print(epson.uchet())
print("----------Перемещаем со склада----------")
a = panasonic.inv_num_1
panasonic.moving(a, Office_region_2.name)
b = epson.inv_num_1
epson.moving(b, Office_region_1.name)

print("----------Отчет по наличию техники----------")

print(f'Всего единиц оргтехники: {Tehnika.count}')

for key, values in Tehnika.dict_inv_num.items():
    print(f'Инв.номер {key}, в подразделении {values}')


print(f'Техника в подразделениях: {Company.calc}')

