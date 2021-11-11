# Задание 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток,
# соответственно.

class Kletka:
    def __init__(self, number_cells):

        # количество ячеек в клетке
        self.number_cells = number_cells

    # Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
    def __add__(self, other):
        c = self.number_cells + other.number_cells
        return c

    # вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества
    # ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
    def __sub__(self, other):
        c = self.number_cells - other.number_cells
        if c >= 0:
            return c
        else: return f"Разность отрицательная"

    # умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
    # этих двух клеток.
    def  __mul__(self, other):
        c = self.number_cells * other.number_cells
        return c

    # деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
    # количества ячеек этих двух клеток.
    def __truediv__(self, other):
        c = self.number_cells // other.number_cells
        return c

    def __mod__(self, other):
        c = self.number_cells % other.number_cells
        return c

    # В классе необходимо реализовать метод, принимающий экземпляр класса и количество ячеек в ряду.
    # Данный метод позволяет организовать ячейки по рядам.
    # Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
    # Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
    def make_order(self, cells_in_row):
        if self.number_cells >= cells_in_row:
            a = f'{"*" * cells_in_row} \n' * (self.number_cells // cells_in_row)\
                   + f'{"*" * (self.number_cells % cells_in_row)}'
        else: a = f'{"*" * (self.number_cells % cells_in_row)}'
        return a

kletka_1 = Kletka(21)
kletka_2 = Kletka(18)

add_kletka = Kletka.__add__(kletka_1, kletka_2)
print(add_kletka)

sub_kletka = Kletka.__sub__(kletka_1, kletka_2)
print(sub_kletka)

mul_kletka = Kletka.__mul__(kletka_1, kletka_2)
print(mul_kletka)

div_kletka = Kletka.__truediv__(kletka_1, kletka_2)
print(div_kletka)

ost_kletka = Kletka.__mod__(kletka_1, kletka_2)
print(ost_kletka)

k = kletka_1.make_order(5)
print(k)