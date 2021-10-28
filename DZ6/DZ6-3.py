# Задание 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    count_workers = 0

    def __init__(self, name, surname, position, oklad, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.oklad = oklad
        self.bonus = bonus
        self._income = {"oklad": oklad, "bonus": bonus}
        Worker.count_workers += 1

class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return sum(self._income.values())


ivanov = Position("Иван", "Иванов", "инженер", 50000, 10000)
print(f"ФИО сотрудника: {ivanov.get_full_name()}")
print(f"Доход: {ivanov.get_total_income()}")
print(f"Количество сотрудников: {Worker.count_workers}")
