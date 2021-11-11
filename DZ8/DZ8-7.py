''' Задание 7.
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

class Complex_int:

    def __init__(self, a, b, j='j'):
        self.a = a
        self.b = b
        self.j = j

    def __str__(self):
        return f'({self.a}+{self.b}{self.j})'

    def __add__(self, other):
        return f'({self.a+other.a}+{self.b + other.b}{self.j})'

    def __mul__(self, other):
        return f'({self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}{self.j})'


print('***** Класс комплексных чисел: ***** ')
u = Complex_int(2, 8)
z = Complex_int(3, 5)
print(u)
print(u + z)
print(u * z)


print('***** Проверка: ***** ')
u_1 = complex(2, 8)
z_1 = complex(3, 5)
print(u_1)
print(u_1 + z_1)
print(u_1 * z_1)
