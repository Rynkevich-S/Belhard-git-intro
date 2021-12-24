if __name__ == '__main__':
    a = input('Введите число a: ')
    b = input('Введите число b: ')
    c = input('Введите число c: ')
    result = ((int(a)**2 + int(b)**2) / (3 * int(b) - 4))
    result2 = (4 * int(c)**5 / 6)
    answer = result // result2
    answer2 = result % result2
    print(f'Деление без остатка: {answer}')
    print(f'Деление с остатком: {answer2}')
