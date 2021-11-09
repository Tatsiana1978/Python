# Задание 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def total_consumption(self):
        pass

    def __add__(self, other):
        return self.total_consumption + other.total_consumption

class Coat(Clothes):
    name = "пальто"

    @property
    def total_consumption(self):
        return self.size/6.5 + 0.5

class  Suit(Clothes):
    name = "костюм"

    @property
    def total_consumption(self):
        return 2 * self.size + 0.3

palto = Coat(48)
kostum = Suit(50)

print(palto.total_consumption)
print(kostum.total_consumption)
print(palto + kostum)