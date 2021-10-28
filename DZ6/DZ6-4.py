# Задание 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed_1, color, name, is_police):
        self.speed_1 = speed_1
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
       return f"Автомобиль {self.name} поехал"

    def stop(self):
        return f"Автомобиль {self.name} остановился"

    def turn_right(self):
        return f"Автомобиль {self.name} повернул направо"

    def turn_left(self):
        return f"Автомобиль {self.name} повернул налево"

    def show_speed(self):
        return f"Текущая скорость автомобиля {self.name} - {self.speed_1}"

class TownCar(Car):
    def show_speed(self):
        if self.speed_1 > 60:
            print("Вы превысили скорость. Допустимая скорость до 60 км/ч")
        return f"Текущая скорость {self.speed_1} км/ч"
class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed_1 > 40:
            print(f"Вы превысили скорость. Допустимая скорость  до 40 км/ч.")
        return f"Текущая скорость {self.speed_1} км/ч"

class PoliceCar(Car):
    is_police = True

ferrari = SportCar(120, "red", "Ferrari sf90", None)
print(ferrari.go())
print(ferrari.show_speed())

mersedes = TownCar(90, "black", "Mersedes sl60", None)
print(mersedes.stop())

volkswagen = WorkCar(45, "withe", "Volkswagen Transporter", None)
print(volkswagen.turn_left())
print(volkswagen.show_speed())

lada = PoliceCar(120, "blue", "Lada Kalina", True)
print(lada.go())
print(f"Отношение к полиции: {lada.is_police}")
