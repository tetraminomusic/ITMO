# Author = Malykh Kirill Romanovich
# Group = P3132
# Date = 08.10.2025

import re

while 1:
    s = input("Введите список (в одну строку без разделителей) стипендиатов текущего семестра:\n")
    my_group = "P3132"

    group = r"P[0-9]+"      #поиск по номеру группы
    pattern_surname = r"(?:\b[А-ЯЁ][а-я]*(?:\-[а-яА-ЯёЁ]+)?\b\s)" #Поиск фамилий (В том числе двойных)
    pattern_fullname = rf"{pattern_surname}[А-ЯЁ]\.[А-ЯЁ]\.\s{group}" #Объединяем фамилию и инициалы
    first_letter = r"[А-ЯЁ]" #Ищем все первые буквы 

    a = re.findall(pattern_fullname, s)

    print("\nОтвет:\n")

    if len(a) == 0:
        print("Бро, ты ввёл какую-то шляпу полную 💀💀💀💀💀")

    for i in a:
        
        k = i.split()
        nfl = re.findall(first_letter, k[0]) #nfl - name first letter
        nfl.append(k[1][0]) # первый инициал
        nfl.append(k[1][2]) # второй инициал
        if len(nfl) == 4:
            if not ((nfl[2] == nfl[3] and (nfl[0] == nfl[2] or nfl[1] == nfl[2])) and re.findall(group, i) == [my_group]):
                print(i)
        elif len(nfl) == 3:
            if not (len(set(nfl)) == 1 and re.findall(group, i) == [my_group]):
                print(i)
        else:
            print("Бро, ты ввёл какую-то шляпу полную 💀💀💀💀💀")