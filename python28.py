# Найти корни квадратного уравнения Ax² + Bx + C = 0
a = float(input('number for a: '))
b = float(input('number for b: '))
c = float(input('number for c: '))
def findx(a, b, c):
    discriminant = b**2 - 4*a*c
    print('Дискриминант = ' + str(discriminant))
    if discriminant < 0:
        print('Корней нет')
    elif discriminant == 0:
        x = -b / (2 * a)
        print('x = ' + str(x))
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print('x₁ = ' + str(x1))
        print('x₂ = ' + str(x2))
findx(a, b, c)