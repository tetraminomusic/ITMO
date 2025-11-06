INI_SECTION_OPEN = "["
INI_SECTION_CLOSE = "]"
INI_COMMENT = [";",'#']
INI_EQUALS = "="
INI_NEWLINE = "\n"
INI_WHITESPACE = ["\t"," "]

#ищем начала секций
def lex_section_name(s):
    if s[0] == INI_SECTION_OPEN:
        s = s[1:]
        for i in range(len(s)):
            if s[i] == INI_SECTION_CLOSE:
                return s[:i].strip(), s[i+1:].strip()
            elif s[i] == INI_NEWLINE:
                raise Exception("Незакрытая секция")
        raise Exception("Незакрытая секция")
    else:
        return None, s

#заголовки переменных
def lex_key(s):
    if "=" in s:
        for i in range(len(s)):
            if s[i] == INI_EQUALS:
                return s[:i].strip(), s[i+1:]
            elif s[i] == INI_NEWLINE:
                raise Exception("Нет имени")
    else:
        return None, s

#содержимое или значения перменных
def lex_value(s):
    for i in range(len(s)):
        if s[i] in INI_COMMENT:
            return s[:i].strip(), s[i:]
        elif s[i] == INI_NEWLINE:
            return s[:i].strip(), s[i+1:]
        
    return s.strip(),""

#Проверка на наличие комментариев        
def lex_comment(s):
    if s != "" and s[0] in INI_COMMENT:
        for i in range(len(s)):
            if s[i] == INI_NEWLINE:
                return s[1:i].strip(), s[i+1:]
        return s[1:].strip(), ""
    else:
        return None, s

def lex_new_line(s):
    if s != "" and s[0] == INI_NEWLINE:
        return True, s[1:]
    else:
        return None, s

def lex_whitespace(s):
    if s != "" and s[0] in INI_WHITESPACE:
        return True, s[1:]
    else:
        return None, s
    
def lex_for_ini(s):
    tokens = []
    line_counter = 1
    while len(s) != 0:

        #Рассматриваем комментарии
        comment, s = lex_comment(s)
        if comment != None:
            tokens.append(("COMMENT",comment))
            continue

        #Рассматриваем пробелы
        whitespace, s = lex_whitespace(s)
        if whitespace != None:
            continue

        #подсчёт количества новых строк для нахождения ошибок
        newline, s = lex_new_line(s)
        if newline != None:
            line_counter+=1
            continue

        #Рассматрием секции
        section_name, s = lex_section_name(s)
        if section_name != None:
            tokens.append(("SECTIONS", section_name))
            continue

        #Рассматрием ключ - значения
        key, s = lex_key(s)
        if key != None:
            value, s = lex_value(s)
            tokens.append(("KEY_VALUE", key, value))
            continue
        raise Exception(f"Ошибка в {line_counter}: '{s[0]}'")
    
    return tokens

def consolidation(tokens): # производит десереализацию и преобразует в питоновский словарь
    result = {}
    current_section = "global"
    result[current_section] = {}

    for token in tokens:
        if token[0] == "SECTIONS":
            current_section = token[1] 
            if current_section not in result:
                result[current_section] = {}
        elif token[0] == "KEY_VALUE":
            key, value = token[1], token[2]
            result[current_section][key] = value
    return result


def main():
    s = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\input.ini", encoding="utf-8").read()
    tokens = lex_for_ini(s)
    result = consolidation(tokens)
    f = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\dict.txt", "w", encoding="utf-8").write(str(result))

main()