import math
import cmath

print('2.1.	Составить программу! \n'
      'а)вычисления значения функции y = 17x2– 6x + 13 при любом значении x; \n'
      'б)вычисления значения функции y = 3a2 + 5a – 21 при любом значении а.')
x = float(input('Введите числовое значение "х":'))
print('y =', 17 * x ** 2 - 6 * x + 13)

a = float(input('Введите числовое значение "a":'))
print('y = ', 3 * a ** 2 + 5 * a - 21)


print('2.2.	 Составить программу вычисления значения функции при любом значении а. \n'
      'a2+10/sqrt(a2+1)')
a = float(input('Введите числовое значение "a":'))
print((a ** 2 + 10) / (a ** 2 + 1) ** (1 / 2))


print('2.3.	 Составить программу: \n'
      'а) вычисления значения функции sqrt((2a+sin|3a|)/3.56 при любом значении а; \n'
      'б) вычисления значения функции sin ((3.2+sqrt(1+x))/|5x|)при любом значении х')
a = float(input('Введите числовое значение "a":'))
if a >= 0:
    print(math.sqrt((2 * a + (math.sin(math.fabs(3 * a)))) / 3.56))
else:
    print(cmath.sqrt((2 * a + (math.sin(math.fabs(3 * a)))) / 3.56))


x = float(input('Введите числовое значение "x":'))
if x >= 0:
    print(math.sin((3.2 + math.sqrt(1 + x) / math.fabs(5 * x))))
else:
    print(cmath.sin((3.2 + cmath.sqrt(1 + x) / math.fabs(5 * x))))


print('2.4.	 Дана сторона квадрата. Найти его периметр.')
square_side = float(input('Введите длину стороны квадрата:'))
square_perimeter = 4 * square_side
print('Периметр квадрата равен :', square_perimeter)


print('2.5.	 Дан радиус окружности. Найти ее диаметр.')
radius_of_round = float(input('Введите радиус круга:'))
print('Диаметр круга равен :', 2 * radius_of_round)


print('2.6.	 Считая, что Земля – идеальная сфера с радиусом R = 6350 км, определить расстояние до линии горизонта \n'
      'от точки с заданной высотой над Землей.')
h_under_earth = float(input('Введите значение высоты над землей:'))
print('Расстояние до линии горизонта :', math.sqrt((6350 + h_under_earth) ** 2 - 6350 ** 2))
