import random

task = int(input("Введите номер задания: "))
count = 0
if task == 1:  # Task 1
    number = int(input("Введите число: "))
    ans = ''
    while number % 10 > 0:
        ostatok = number % 10
        number = number // 10
        ans = ans + str(ostatok)
    print('Answer: ', ans)
elif task == 2:  # Task 2
    number = int(input("Введите число: "))
    while number > 1:
        if number % 2 == 0:  # Четное
            number = number / 2
        elif number % 2 != 0:  # Не четное
            number = (number * 3 + 1) / 2
        print(number)
elif task == 3:  # Task 3
    number = int(input("Введите число: "))
    while number > 0:
        number = number // 10
        count += 1
    print('Answer: ', count)
elif task == 4:  # Task 4
    number = int(input("Введите число: "))
    ans = ''
    while number % 10 > 0:
        ostatok = number % 10
        number = number // 10
        ans = ans + str(ostatok)
    ans = int(ans)
    while ans % 10 != 8:
        count += 1
        ans = ans // 10
    print(count + 1)
elif task == 5:  # Task 5
    scores = 1
    team1 = 0
    team2 = 0
    while scores != 0 and scores < 4:
        scores = int(input('Введите кол-во очков: '))
        if scores == 0:
            break
        team = int(input('Введите команду которой зачислить очки: '))
        if team == 1:
            team1 = team1 + scores
        elif team == 2:
            team2 = team2 + scores
        else:
            print('Такой команды не сущесвтует!')
        print('Счет первой команды:', team1, 'Счет второй команды:', team2)
elif task == 6:  # Task 6
    number = int(input('Введите число: '))
    n = number
    c = number
    b = 0
    multiplication = 1
    sqr = 0
    cub = 0
    ans = ''
    while n > 0:
        count += 1
        b = b + n % 10
        multiplication = multiplication * (n % 10)
        sqr = sqr + (n % 10) ** 2
        cub = cub + (n % 10) ** 3
        n = n // 10
    while number % 10 > 0:
        ostatok = number % 10
        number = number // 10
        ans = ans + str(ostatok)
    ans = int(ans)
    print('a) ', count)
    print('b) ', b)
    print('c) ', multiplication)
    print('d) ', b / count)
    print('e) ', sqr)
    print('f) ', cub)
    print('g) ', ans % 10)
    print('h) ', c % 10 + ans % 10)
elif task == 7:  # Task 7
    number = int(input('Введите сумму: '))
    m64 = number // 64
    m32 = (number % 64) // 32
    m16 = ((number % 64) % 32) // 16
    m8 = (((number % 64) % 32) % 16) // 8
    m4 = ((((number % 64) % 32) % 16) % 8) // 4
    m2 = (((((number % 64) % 32) % 16) % 8) % 4) // 2
    m1 = ((((((number % 64) % 32) % 16) % 8) % 4) % 2) // 1
    print(m64, 'купюр по 64 ', m32, 'купюр по 32 ', m16, 'купюр по 16 ', m8, 'купюр по 8 ', m4, 'купюр по 4 ', m2,
          'купюр по 2 ', m1, 'купюр по 1')
elif task == 8:  # Task 8
    number = int(input('Введите число: '))
    m = int(input('Введите m: '))
    i = 0
    c = 0
    while i != m:
        n = number % 10
        c = c + n
        number = number // 10
        i += 1
    print(c)
elif task == 9:  # Task 9
    number = int(input("Введите число: "))
    i = 2
    while i <= number and number % i != 0:
        i += 1
    print(i)
elif task == 10:  # Task 10
    numbers = []
    for i in range(20):
        numbers.append(random.randint(0, 66))
        print(numbers[i], ' ')
    for i in range(len(numbers)):
        for k in range(1, 20):
            if numbers[i] % 10 == numbers[k] // 10:
                count += 1
    if count >= 20: print('Yes')
elif task == 11:  # Task 11
    number = int(input("Введите число: "))
    a = int(input("Введите цифрру a:"))
    b = int(input("Введите цифрру b:"))
    count1 = 0
    while number > 0:
        if number % 10 == a:
            count += 1
        elif number % 10 == b:
            count1 += 1
        number = number // 10
    if count > 0:
        print('a) Да, есть')
    else:
        print('a) Нету')
    if count > 1:
        print('b) Верно')
    else:
        print('b) Не верно')
    if count > 0 and count1 > 0:
        print('c) Есть')
    else:
        print('c) Нету')
elif task == 12:  # Task 12
    x = 0
    y = 0
    z = 0
    while x < 30 and y < 30 and z < 30:
        x = int(input('Введите x: '))
        y = int(input('Введите y: '))
        z = int(input('Введите z: '))
        if x >= 30 or y >= 30 or z >= 30:
            break
        if x ** 2 == y ** 2 + z ** 2:
            print('Треуголник пифагора')
        elif y ** 2 == x ** 2 + z ** 2:
            print('Треуголник пифагора')
        elif z ** 2 == y ** 2 + x ** 2:
            print('Треуголник пифагора')
        else:
            print('Данный треугольник не удовлетворяет условиям!')
elif task == 13:  # Task 13
    m = int(input('Введите число m: '))
    n = int(input('Введите число n'))
    i = 1
    ans = 0
    while i != m:
        ans = ans + i ** n
        i += 1
    print('Ответ: ', ans)
elif task == 14:  # Task 14
    n = int(input('Введите число n<27: '))
    while n >= 27:
        print('Введите коректное число: ')
        n = int(input('Введите число n<27: '))
    s = 0
    i = 0
    k = 0
    j = 0
    while i != 10:
        while k != 10:
            while j != 10:
                if i + k + j == n:
                    print(str(i) + str(k) + str(j))
                    s += 1
                j += 1
            k += 1
            if j == 10:
                j = 0
        i += 1
        if k == 10:
            k = 0
    print('Кол-во чисел сумма, которых равно', n, ': ', s)
# Пробелы для читабельности
