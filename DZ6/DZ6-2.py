# Задание 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.


class Road:
    _all_r_length = 0

    def massa_asf(self, r_lenght_m, r_width_m, thickness_sm):
        massa_kg_1m = 25
        self._r_length = r_lenght_m
        self._r_width = r_width_m
        self._thickness = thickness_sm

        print (f"На дорогу длинной {r_lenght_m} метров, шириной {r_width_m} метров и толщиной асфальта \
{thickness_sm} см понадобится {r_lenght_m * r_width_m * massa_kg_1m * thickness_sm / 1000} тонн асфальта ")

a = Road()
Road.massa_asf(a, 5000, 20, 5)