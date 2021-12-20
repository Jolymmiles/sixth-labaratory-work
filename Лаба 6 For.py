import math

number = int(input('Введите номер задания: '))
if number == 2:  # Task 2
    n = int(input('n км: '))
    y = int(input('y%: '))
    x = int(input('x :'))
    s = 0
    for i in range(x):
        s = s + n
        n = n + (y * n) / 100
    print(s, ' км')
elif number == 3:  # Task 3
    k = 0
    for i in range(5):
        number = int(input('Введите число:'))
        if number <= 9:
            k = k + 1
    print('Простых чисел: ', k)
elif number == 4:  # Task 4
    s = 0
    for i in range(16):
        for l in range(32):
            if i * 4 + l * 2 <= 64:
                s = s + 1
    print(s)
elif number == 5:  # Task 5
    n = int(input(''))
    n = n + 1
    g = 0
    for i in range(1, n):
        for k in range(10):
            c = i + k
            print(str(i), '+', str(k), '=', c)
elif number == 6:  # Task 6
    n = int(input(''))
    n = n + 1
    g = 0
    for i in range(1, n):
        for k in range(10):
            c = i * k
            print(str(i), '*', str(k), '=', c)
elif number == 7:  # Task 7
    number_of_number = str(input('Введите букву задания: '))
    if number_of_number == 'a':
        s = 0
        for i in range(100, 500):
            s = s + i
        print(s)
    elif number_of_number == 'b':
        a = int(input('Введите откуда начать отсчет до 500: '))
        s = 0
        for i in range(a, 500):
            s = s + i
        print(s)
    elif number_of_number == 'c':
        b = int(input('Введите до сколько считать: '))
        s = 0
        for i in range(-10, b):
            s = s + i
        print(s)
    elif number_of_number == 'd':
        a = int(input('Введите откуда начать отсчет: '))
        b = int(input('Введите до сколько считать: '))
        s = 0
        for i in range(a, b):
            s = s + i
        print(s)
elif number == 8:  # Task 8
    n = int(input('Кол-во вещ. чисел: '))
    Float_numbers = []
    for i in range(n):
        Float_numbers.append(float(input('Вещестенное число: ')))
    s = 0
    for k in range(n):
        s = s + Float_numbers[k] ** 2
    print(s)
elif number == 9:  # Task 9
    v = int(input('Кол-во элементов цепи: '))
    R = []
    for i in range(v):
        R.append(int(input('Введите сопротивление: ')))
    s = 0
    for r in range(len(R)):
        s = s + R[r]
    print(s)
elif number == 10:  # Task 10
    r = 5
    v = 0
    for i in range(1, 12):
        v = v + 4 / 3 * math.pi * r ** 3
        r = r + 0.5
    print('v:', v)
    print('v литров: ', v / 1000)
elif number == 11:  # Task 11
    # переменные
    distance = []
    time = []
    speed = []
    max_speed = 0
    s = 0
    n = int(input('Количество машин: '))
    # Данны ск и времени
    for i in range(n):
        distance.append(int(input('Введите сколько проехала машина: ')))
        time.append(int(input('Введите сколько машина была в пути: ')))
    # Цикл, который узнает ск.км
    # и номер самой быстрой машины
    for k in range(n):
        speed.append(distance[k] // time[k])
        if max_speed < speed[k]:
            max_speed = speed[k]
            if max_speed == speed[k]:
                speedest_car = i + 1
    # Ср. скорсоть
    for c in range(n):
        s = s + speed[c]
    medium_speed = s / n
    print('a) ', max_speed)
    print('b) ', speedest_car)
    print('c) ', medium_speed)
elif number == 12:  # Task 12
    salary_month = []
    quarter = []
    l = 0
    c = 1
    for i in range(1, 12):
        person = int(input('Сотрудник до 12: '))
        if person == 1:
            for c in range(12):
                salary_month.append(int(input('Зарплата: ')))
                l = l + salary_month[c]
                if c % 3 == 0:
                    quarter.append(l)
                    l = 0
    for s in range(1, 4):
        print(quarter[s])
elif number == 13:  # Task 13
    #     weights=[100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]
    #     v=int(input('Input weight:'))
    #     s=0
    #     if weights[8]+weights[9]>=v:
    #         for i in range(len(weights)):
    #             a=weights[i]
    #             for k in range(len(weights)):
    #                 b=weights[k]
    #                 if a+b==v:
    #                     if a==b: continue
    #                     s+=1
    #     elif weights[7]+weights[8]+weights[9]>=v:
    #         for i in range(len(weights)):
    #             a=weights[i]
    #             for k in range(len(weights)):
    #                 b=weights[k]
    #                 for l in range(len(weights)):
    #                     c=weights[l]
    #                     if a+b+c==v:
    #                         if a==b==c or a==b or a==c: continue
    #                         s+=1
    #     elif weights[6]+weights[7]+weights[8]+weights[9]>=v:
    #         for i in range(len(weights)):
    #             a=weights[i]
    #             for k in range(len(weights)):
    #                 b=weights[k]
    #                 for l in range(len(weights)):
    #                     c=weights[l]
    #                     for j in range(len(weights)):
    #                         d=weights[j]
    #                         if a+b+c+d==v:
    #                             if a==b==c or a==b or a==c or a==b==c==d or c==b or c==d or a==d or b==d: continue
    #                             s+=1
    #     elif weights[5]+weights[6]+weights[7]+weights[8]+weights[9]>=v:
    #         for i in range(len(weights)):
    #             a=weights[i]
    #             for k in range(len(weights)):
    #                 b=weights[k]
    #                 for l in range(len(weights)):
    #                     c=weights[l]
    #                     for j in range(len(weights)):
    #                         d=weights[j]
    #                         for h in range(len(weights)):
    #                             e=weights[h]
    #                             if a+b+c+d+e==v:
    #                                 if (a==b==c or a==b or a==c or a==b==c==d or c==b or c==d or a==d
    #                                     or b==d or a==b==c==d==e or a==e or b==e or c==e or d==e): continue
    #                                 s+=1
    #     elif weights[4]+weights[5]+weights[6]+weights[7]+weights[8]+weights[9]>=v:
    #         for i in range(len(weights)):
    #             a=weights[i]
    #             for k in range(len(weights)):
    #                 b=weights[k]
    #                 for l in range(len(weights)):
    #                     c=weights[l]
    #                     for j in range(len(weights)):
    #                         d=weights[j]
    #                         for h in range(len(weights)):
    #                             e=weights[h]
    #                             for x in range(len(weights)):
    #                                 f=weights[x]
    #                                 if a+b+c+d+e+f==v:
    #                                     if (a==b==c or a==b or a==c or a==b==c==d or c==b or c==d or a==d
    #                                         or b==d or a==b==c==d==e or a==e or b==e or c==e or d==e or a==b==c==d==e==f or a==f or b==f or c==f or d==f or e==f): continue
    #                                     s+=1
    #     elif weights[3]+weights[4]+weights[5]+weights[6]+weights[7]+weights[8]+weights[9]>=v:
    #         for i in range(len(weights)):
    #             a=weights[i]
    #             for k in range(len(weights)):
    #                 b=weights[k]
    #                 for l in range(len(weights)):
    #                     c=weights[l]
    #                     for j in range(len(weights)):
    #                         d=weights[j]
    #                         for h in range(len(weights)):
    #                             e=weights[h]
    #                             for x in range(len(weights)):
    #                                 f=weights[x]
    #                                 for z in range(len(weights)):
    #                                     g=weights[z]
    #                                     if a+b+c+d+e+f+g==v:
    #                                         if (a==b==c or a==b or a==c or a==b==c==d or c==b or c==d or a==d
    #                                             or b==d or a==b==c==d==e or a==e or b==e or c==e or d==e
    #                                             or a==b==c==d==e==f or a==f or b==f or c==f or d==f or e==f
    #                                             or a==b==c==d==e==f==g or a==g or b==g or c==g or d==g or e==g or d==g): continue
    #                                         s+=1
    #     elif weights[2]+weights[3]+weights[4]+weights[5]+weights[6]+weights[7]+weights[8]+weights[9]>=v:
    #         for i in range(len(weights)):
    #             a=weights[i]
    #             for k in range(len(weights)):
    #                 b=weights[k]
    #                 for l in range(len(weights)):
    #                     c=weights[l]
    #                     for j in range(len(weights)):
    #                         d=weights[j]
    #                         for h in range(len(weights)):
    #                             e=weights[h]
    #                             for x in range(len(weights)):
    #                                 f=weights[x]
    #                                 for z in range(len(weights)):
    #                                     g=weights[z]
    #                                     for m in range(len(weights)):
    #                                         u=weights[m]
    #                                         if a+b+c+d+e+f+g+u==v:
    #                                             if (a==b==c or a==b or a==c or a==b==c==d or c==b or c==d or a==d
    #                                                 or b==d or a==b==c==d==e or a==e or b==e or c==e or d==e
    #                                                 or a==b==c==d==e==f or a==f or b==f or c==f or d==f or e==f
    #                                                 or a==b==c==d==e==f==g or a==g or b==g or c==g or d==g or
    #                                                 e==g or d==g or a==b==c==d==e==f==g==m or a==m or b==m or
    #                                                 c==m or d==m or e==m or f==m or g==m): continue
    #                                             s+=1
    #     elif weights[1]+weights[2]+weights[3]+weights[4]+weights[5]+weights[6]+weights[7]+weights[8]+weights[9]>=v:
    #         for i in range(len(weights)):
    #             a=weights[i]
    #             for k in range(len(weights)):
    #                 b=weights[k]
    #                 for l in range(len(weights)):
    #                     c=weights[l]
    #                     for j in range(len(weights)):
    #                         d=weights[j]
    #                         for h in range(len(weights)):
    #                             e=weights[h]
    #                             for x in range(len(weights)):
    #                                 f=weights[x]
    #                                 for z in range(len(weights)):
    #                                     g=weights[z]
    #                                     for m in range(len(weights)):
    #                                         u=weights[m]
    #                                         for r in range(len(weights)):
    #                                             p=weights[r]
    #                                             if a+b+c+d+e+f+g+u+p==v:
    #                                                 if (a==b==c or a==b or a==c or a==b==c==d or c==b or c==d or a==d
    #                                                     or b==d or a==b==c==d==e or a==e or b==e or c==e or d==e
    #                                                     or a==b==c==d==e==f or a==f or b==f or c==f or d==f or e==f
    #                                                     or a==b==c==d==e==f==g or a==g or b==g or c==g or d==g or
    #                                                     e==g or d==g or a==b==c==d==e==f==g==m or a==m or b==m or
    #                                                     c==m or d==m or e==m or f==m or g==m or a==b==c==d==e==f==g==m
    #                                                     or a==r or b==r or c==r or d==r or e==r or f==r or g==r or m==r ): continue
    #                                                 s+=1
    #     elif weights[0]+weights[1]+weights[2]+weights[3]+weights[4]+weights[5]+weights[6]+weights[7]+weights[8]+weights[9]>=v:
    #         for i in range(len(weights)):
    #             a=weights[i]
    #             for k in range(len(weights)):
    #                 b=weights[k]
    #                 for l in range(len(weights)):
    #                     c=weights[l]
    #                     for j in range(len(weights)):
    #                         d=weights[j]
    #                         for h in range(len(weights)):
    #                             e=weights[h]
    #                             for x in range(len(weights)):
    #                                 f=weights[x]
    #                                 for z in range(len(weights)):
    #                                     g=weights[z]
    #                                     for m in range(len(weights)):
    #                                         u=weights[m]
    #                                         for r in range(len(weights)):
    #                                             p=weights[r]
    #                                             for q in range(len(weights)):
    #                                                 w=weights[q]
    #                                                 if a+b+c+d+e+f+g+u+p==v:
    #                                                     if (a==b==c or a==b or a==c or a==b==c==d or c==b or c==d or a==d
    #                                                         or b==d or a==b==c==d==e or a==e or b==e or c==e or d==e
    #                                                         or a==b==c==d==e==f or a==f or b==f or c==f or d==f or e==f
    #                                                         or a==b==c==d==e==f==g or a==g or b==g or c==g or d==g or
    #                                                         e==g or d==g or a==b==c==d==e==f==g==m or a==m or b==m or
    #                                                         c==m or d==m or e==m or f==m or g==m or a==b==c==d==e==f==g==m==r
    #                                                         or a==r or b==r or c==r or d==r or e==r or f==r or g==r or m==r
    #                                                         or a==b==c==d==e==f==g==m==r==w or a==w or b==w or c==w or d==w
    #                                                         or e==w or f==w or g==w or m==w or r==w ): continue
    #                                                     s+=1
    #     print(s//2)
    from itertools import combinations

    weights = [100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]
    v = int(input('Введите желаемый вес: '))
    n_comb = 1
    ans = 0
    for n_comb in range(1, len(weights) + 1):
        for comb in combinations(weights, r=n_comb):
            if sum(comb) == v:
                ans += 1
    print(ans)
