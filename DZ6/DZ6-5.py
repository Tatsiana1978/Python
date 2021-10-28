# Задание 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return "Запуск отрисовки"

class Pen(Stationery):
    def draw(self):
        return f"{self.title}. Запуск написания текста"
class Pencil(Stationery):
    def draw(self):
        return f"{self.title}. Запуск отрисовки чертежа"
class Handle(Stationery):
    def draw(self):
        return f"{self.title}. Запуск отрисовки картинки"

karandash = Pencil("Карандаш")
print(karandash.draw())
rutsh = Pen("Ручка")
print(rutsh.draw())
marker = Handle("Маркер")
print(marker.draw())