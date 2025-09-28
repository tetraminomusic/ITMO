
Hemming = ["r1","r2","i1","r3","i2","i3","i4"]
m = input("Введите ваше сообщение (aka набор из 7 символов, состоящий из \"0\" и \"1\"): ")

if (m.replace('0', '').replace('1', '') == "") and len(m) == 7:
    
    s1 = (int(m[0])+int(m[2])+int(m[4])+int(m[6]))%2
    s2 = (int(m[1])+int(m[2])+int(m[5])+int(m[6]))%2
    s3 = (int(m[3])+int(m[4])+int(m[5])+int(m[6]))%2
    s = str(s1)+str(s2)+str(s3)
    s_10 = int(s, 2)
    if s_10 != 0:

        print(f"S = {s}")

        print(f"Ошибка в {s_10} позиции. Следовательно, ошибка в {Hemming[s_10-1]}")

        print(f"Исправляем {Hemming[s_10-1]} = {int(m[s_10-1])} на {Hemming[s_10-1]} = {abs(int(m[s_10-1])-1)}")

        correct_message = m[0:s_10-1] + str(abs(int(m[s_10-1])-1)) + m[s_10:]

        print(f"Как итог, получаем правильное кодовое слово: {correct_message}, где {correct_message[2]+correct_message[4:7]} - правильное сообщение")
    else:
        print("В данном сообщении ошибки отсутствуют")
else:
    print("Введено некорректное значение")