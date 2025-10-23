# Author = Malykh Kirill Romanovich
# Group = P3132
# Date = 08.10.2025

import re
glasnaya = r"[аоэуяёеюиы]"

while 1:
    s, p = input("Введите Хайку:\n"), []
    s = s.split("/") # Делим входящую строку на подстроки
    if len(s) == 3:
        for i in range(len(s)):
            p.append(re.findall(glasnaya, s[i], re.IGNORECASE)) #находим все гласные в каждой из подстрок
        if len(p[0]) == 5 and len(p[1]) == 7 and len(p[2]) == 5: # проверяем всё это на условие из тз
            print("Хайку!")
        else:
            print("Не хайку.")
            
    else:
        print("Не хайку. Должно быть 3 строки.")


