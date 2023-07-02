print('введите длину сторон треугольника: ')
a = float(input('сторона a: '))
b = float(input('сторона d: '))
c = float(input('сторона c: '))
if a + b <= c or a + c <= b or b + c <= a:
    print('треугольник не существует')
elif a == b == c:
    print('треугольник равносторонний')
elif a != b and a != c and b != c:
    print('треугольник разносторонний')
else:                                    # if a == b or a == c or b == c:
    print('треугольник равнобедренный')  # print('треугольник равнобедренный')