import math
import cmath

print('2.1.	Составить программу! \n'
      'а)вычисления значения функции y = 17x2– 6x + 13 при любом значении x; \n'
      'б)вычисления значения функции y = 3a2 + 5a – 21 при любом значении а.')

try:
    x = float(input('Введите числовое значение "х":'))
    print('y =', 17 * x ** 2 - 6 * x + 13)
except ValueError:
    print('Вы ввели недопустимое значение, повторите ввод!')

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


print('2.7.	 Дана длина ребра куба. Найти объем куба и площадь его боковой поверхности')
cube_edge_length = float(input('Введите значение длины ребра куба:'))
lateral_surface_cube_area = 4 * cube_edge_length ** 2
print('Площадь боковой поверхности куба равна :', lateral_surface_cube_area)
cube_volume = cube_edge_length ** 3
print('Объем куба равен :', cube_volume)


print('2.8.	 Дан радиус окружности. Найти длину окружности и площадь круга.')
circle_radius = float(input('Введите радиус окружности:'))
circumference = 2 * circle_radius * math.pi
print('Длина окружности равна :', circumference)
circle_area = circle_radius ** 2 * math.pi
print('Площадь круга равна :', circle_area)


print('Составить программу:\n'
      'а)вычисления значения функции z = 2x3 – 3,44xy + 2,3x2 – 7,1y + 2 при любых значениях х и y;\n'
      'б)вычисления значения функции x = 3,14(a + b)3+ 2,75b2 – 12,7a– 4,1 при любых значениях a и b.')
x = float(input('Введите x:'))
y = float(input('Введите y:'))
z = 2 * x ** 3 - 3.44 * x * y + 2.3 * x ** 2 - 7.1 * y + 2
print('z = ', z)
a = float(input('Введите a:'))
b = float(input('Введите b:'))
x = 3.14 * (a + b) ** 3 + 2.75 * b ** 2 - 12.7 * a - 4.1
print('x = ', x)


print('2.10.	 Даны два целых числа. Найти:\n'
      'а) их среднее арифметическое;\n'
      'б) их среднее геометрическое.')
num_1 = int(input('Введите первое число:'))
num_2 = int(input('Введите второе число:'))
average_arithmetic = (num_1 + num_2) / 2
average_geometric = (num_1 * num_2) ** (1./2)
print('Среднее арифметическое = ', average_arithmetic)
print('Среднее геометрическое = ', average_geometric)


print('2.11.	 Известны объем и масса тела. Определить плотность материала этого тела.')
body_mass = float(input('Введите массу тела:'))
body_volume = float(input('Введите объем тела:'))
body_density = body_volume * body_mass
print('Искомая плотность материала равна :', body_density)


print('2.12.	 Известны количество жителей в государстве и площадь его территории. Определить плотность населения\n'
      'в этом государстве.')
num_of_people = float(input('Введите кол-во жителей:'))
country_area = float(input('Введите площадь страны:'))
density_of_people = num_of_people / country_area
print('Плотность населения по заданным данным равна :', density_of_people)


print('2.13.	 Составить программу решения линейного уравнения ax + b = 0 (a ≠ 0).')
a = float(input('Введите a:'))
b = float(input('Введите b:'))
if a == 0:
    print('Введенное значение противоречит условию!')
else:
    print('x =', -b / a)


print('2.14.	 Даны катеты прямоугольного треугольника. Найти его гипотенузу.')
a = float(input('Введите катет a:'))
b = float(input('Введите катет b:'))
print('Гипотенуза равна :', math.hypot(a, b))


print('2.15.	 Найти площадь кольца по заданным внешнему и внутреннему радиусам.')
inner_radius = float(input('Введите внутренний радиус:'))
outer_radius = float(input('Введите внешний радиус:'))
ring_area = math.pi * (outer_radius ** 2 - inner_radius ** 2)
print('Площадь кольца равна :', ring_area)


print('2.16.	 Даны катеты прямоугольного треугольника. Найти его периметр.')
triangle_leg_a = float(input('Введите катет a:'))
triangle_leg_b = float(input('Введите катет b:'))
triangle_hypotenuse = math.hypot(triangle_leg_a, triangle_leg_b)
triangle_perimeter = triangle_hypotenuse + triangle_leg_a + triangle_leg_b
print('Периметр треугольника равен :', triangle_perimeter)


print('2.17.	 Даны основания и высота равнобедренной трапеции. Найти ее периметр.')
trapezoid_base_a = float(input('Введите нижнее основание трапеции :'))
trapezoid_base_b = float(input('Введите верхнее основание трапеции :'))
trapezoid_height = float(input('Введите высоту трапеции :'))
trapezoid_side = math.hypot((trapezoid_base_a - trapezoid_base_b)/2, trapezoid_height)
trapezoid_perimetr = trapezoid_side * 2 + trapezoid_base_a + trapezoid_base_b
print(' Периметр трапеции равен :', trapezoid_perimetr)

print('2.18.	 Составить программу вычисления значений функций (слишком большая функция)при любых значениях х и y')
x = float(input('Введите x:'))
y = float(input('Введите y:'))
z1 = x + ((2 + y) / x ** 2)
z2 = y + (1 / (x ** 2 + 10) * (1. / 2))
z = z1 / z2
q = 7.25 * math.sin(x) - math.fabs(y)
print('Ответ, z =', z)
print('Ответ, q =', q)


print('2.19.	 Составить программу расчета значения функций (слишком большая функция) при любых значениях a и b.')
a = float(input('Введите a:'))
b = float(input('Введите b:'))
x1 = (2 / (a ** 2 + 25)) + b
x2 = math.sqrt(b) + ((a + b) / 2)
x = x1 / x2
y = (math.fabs(a) + 2 * math.sin(b)) / (5.5 * a)
print('Ответ, x =', x)
print('Ответ, y =', y)


print('2.20.	 Составить программу расчета значения функций (слишком большая функция) \n'
      'при любых значениях e, f, g и h.')
e = float(input('Введите e:'))
f = float(input('Введите f:'))
g = float(input('Введите g:'))
h = float(input('Введите h:'))
a = math.sqrt(math.fabs(e - (3 / f)) ** 3 + g)
b = math.sin(e) + math.cos(h) ** 2
c = (33 * g) / (e * f - 3)
print('Ответ, a =', a)
print('Ответ, b =', b)
print('Ответ, c =', c)


print('2.20.	 Составить программу расчета значения функций (слишком большая функция) \n'
      'при любых значениях e, f, g и h.')
e = float(input('Введите e:'))
f = float(input('Введите f:'))
g = float(input('Введите g:'))
h = float(input('Введите h:'))
a = (e + f / 2) / 3
b = math.fabs(h ** 2 - g)
c = math.sqrt((g - h) ** 2 - (3 * math.sin(e)))
print('Ответ, a =', a)
print('Ответ, b =', b)
print('Ответ, c =', c)


print('2.22.	 Даны два числа. Найти среднее арифметическое и среднее геометрическое их модулей.')
num_1 = int(input('Введите первое число:'))
num_2 = int(input('Введите второе число:'))
average_arithmetic = (math.fabs(num_1) + math.fabs(num_2)) / 2
average_geometric = (math.fabs(num_1) * math.fabs(num_2)) ** (1./2)
print('Среднее арифметическое = ', average_arithmetic)
print('Среднее геометрическое = ', average_geometric)


print('2.23.	 Даны стороны прямоугольника. Найти его периметр и длину диагонали.')
rectangle_side_a = float(input('Введите a:'))
rectangle_side_b = float(input('Введите b:'))
rectangle_perimeter = 2 * (rectangle_side_b + rectangle_side_a)
rectangle_diagonal_length = math.hypot(rectangle_side_b, rectangle_side_a)
print('Периметр прямоугольника равен :', rectangle_perimeter)
print('Длина диагонали прямоугольника равна :', rectangle_diagonal_length)


print('2.24.	 Даны два числа. Найти их сумму, разность, произведение, а также частное от деления \n'
      'первого числа на второе.')
num_1 = float(input('Введите первое число:'))
num_2 = float(input('Введите второе число:'))
print('Сумма :', num_1 + num_2)
print('Разность :', num_1 - num_2)
print('Произведение :', num_1 * num_2)
print('Частное :', num_1 / num_2)


print('2.25.	 Даны длины сторон прямоугольного параллелепипеда. Найти его объем и площадь боковой поверхности.')
parallelepiped_side_a = float(input('Введите a:'))
parallelepiped_side_b = float(input('Введите b:'))
parallelepiped_side_c = float(input('Введите c:'))
parallelepiped_volume = parallelepiped_side_b * parallelepiped_side_c * parallelepiped_side_a
side_surface_area = 2 * (parallelepiped_side_a * parallelepiped_side_c + parallelepiped_side_b * parallelepiped_side_c)
print('Объем параллелепипеда равен :', parallelepiped_volume)
print('Площадь боковой поверхности параллелепипеда равна :', side_surface_area)


print('2.26.	 Даны координаты на плоскости двух точек. Найти расстояние между этими точками.')
x_1 = float(input('Введите x точки А :'))
y_1 = float(input('Введите y точки А:'))
x_2 = float(input('Введите x точки Б:'))
y_2 = float(input('Введите y точки Б:'))
print('Расстояние между точками равно :', math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2))


print('2.27.	 Даны основания и высота равнобедренной трапеции. Найти периметр трапеции.')
trapezoid_base_a = float(input('Введите нижнее основание трапеции :'))
trapezoid_base_b = float(input('Введите верхнее основание трапеции :'))
trapezoid_height = float(input('Введите высоту трапеции :'))
trapezoid_side = math.hypot((trapezoid_base_a - trapezoid_base_b)/2, trapezoid_height)
trapezoid_perimetr = trapezoid_side * 2 + trapezoid_base_a + trapezoid_base_b
print(' Периметр трапеции равен :', trapezoid_perimetr)


print('2.28.	 Даны основания равнобедренной трапеции и угол при большем основании. Найти площадь трапеции.')
trapezoid_base_a = float(input('Введите нижнее основание трапеции :'))
trapezoid_base_b = float(input('Введите верхнее основание трапеции :'))
trapezoid_angle = float(input('Введите угол при большем основании трапеции :'))
trapezoid_side = ((trapezoid_base_a - trapezoid_base_b) / 2) / math.cos(trapezoid_angle)
trapezoid_height = math.sqrt(trapezoid_side ** 2 - ((trapezoid_base_a - trapezoid_base_b) / 2) ** 2)
trapezoid_area = ((trapezoid_base_a + trapezoid_base_b) / 2) * trapezoid_height
print('Площадь трапеции равна :', trapezoid_area)
