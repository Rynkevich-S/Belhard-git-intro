if __name__ == '__main__':
    a = input("1 - Введите текст : ")
    b = input("2 - Введите текст : ")

    if len(a) > len(b):
        print('1 строка длиннее')
    elif len(a) == len(b):
        print('1 и 2 строка равны')
    else:
        print('2 строка длиннее')

    print(f'Первый символ 1 строки: {a[0]}')
    print(f'Последний символ 2 строки: {b[-1]}')
    print(a in b)
    print(b in a)
