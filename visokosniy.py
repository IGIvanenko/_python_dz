year = int(input('введите год гггг: '))
if year % 4 !=0 or year % 100 == 0 and year % 400 != 0:
    print('невисокосный')
else:
    print('високосный')