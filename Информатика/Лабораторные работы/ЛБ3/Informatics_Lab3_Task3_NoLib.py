# Author = Malykh Kirill Romanovich
# Group = P3132
# Date = 08.10.2025

# Для работы программы требуется библиотека pymorphy2

import re

def is_adjective(word):
    return re.fullmatch(r"\b(?:[А-Яа-яЁё]+(?:нн|ов|ев|ск|ист|ат|чив|лив|уч|юч|яч|есн|к|онн|енн|тельн|ин|ан|ян|)(?:ый|ая|ое|ые|ой|им|ых|ую|его|ему|их|ом|ем|ими|ыми|ого|ому|ей|ую|их|им|ий|яя|ее|ие))\b", word)

end_of_adj = r"(?:ый|ий|ой|ая|яя|ое|ее|ого|его|ому|ему|ую|юю|ым|им|ом|ем|их|ых|ую|юю|ыми|ими)"
adj = rf"\b[а-яёА-ЯЁ]{{2,}}{end_of_adj}\b"

while 1:
    try:
        num, s = int(input("Введите порядковый номер повторяющегося прилагательного: ")), input("Введите вашу строку:\n")

        if num > 0:

            list_of_adj_prototype, list_of_adj, list_of_adj2 = re.findall(adj, s), [], [] #Составляем приблизительный список прилагательных, в которые могут входить и существительные

            for i in list_of_adj_prototype: # при помощи данного цикла мы в новый массив записывам только прилагательные при помощи pymorphy2
                if is_adjective(i):
                    list_of_adj.append(i.lower())
            
            print(list_of_adj)

            test = " ".join([i for i in list_of_adj]) #создаём строку для последующего отбора повторяющихся прилагательных

            for i in list_of_adj: #проверка условия на повторяющиеся прилагательные (словоформы)
                if test.count(re.sub(end_of_adj, "", i)) > 1:
                    list_of_adj2.append(i)
            try:
                target = list_of_adj2[num-1]
                osnova_slova, okon_slova = re.sub(end_of_adj, "", target), (re.findall(end_of_adj, target))[-1]

                print("\nРезультат выполнения программы:\n")
                print(re.sub(rf"(?<={osnova_slova}){end_of_adj}", okon_slova, s, flags=re.IGNORECASE)) # (?<={osnova_slova}) - конструкция предугадывания

            except (IndexError):
                print("Ошибка:\nВведено некорректный номер прилагательного или в тексте отсутствуют повторяющиеся прилагательные")
        else:
            print("Введено некорректный номер прилагательного")
    except (ValueError):
        print("Ошибка, ввидет число")


# Уточнение: Порядковый номер в данном случае подразумевается порядковым номером в последовательности, состоящей из повторяющихся прилагательных из исходной строки