# Задание 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

# Создать класс TrafficLight (светофор)
import time
from turtle import color # питон подсказал эту библиотеку для атрибута color

class TrafficLight:
    # атрибут класса/ приватный
    __t_lignt_color = "red"

    # метод класса
    def running(self, time_sleep_1, time_sleep_2, time_sleep_3):

        self.red_mode = time_sleep_1
        self.yellow_mode = time_sleep_2
        self.green_mode = time_sleep_3
        i = 0
        while i < 3:
            __t_lignt_color = "red"
            print("красный сигнал светофора")
            time.sleep(float(self.red_mode))

            __t_lignt_color = "yellow"
            print("желтый сигнал светофора")
            time.sleep(float(self.yellow_mode))

            __t_lignt_color = "green"
            print("зеленый сигнал светофора")
            time.sleep(float(self.green_mode))

            __t_lignt_color = "yellow"
            print("желтый сигнал светофора")
            time.sleep(float(self.yellow_mode))
            i += 1
        return

a = TrafficLight()    #   это объект/экземляр класса
t_lighte_adress = "ул.Ленина,48"
print(t_lighte_adress)
TrafficLight.running(a, 7, 2, 5)
print(_TrafficLight__t_lignt_color)

