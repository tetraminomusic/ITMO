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
        comment, s = lex_comment(s)
        if comment != None:
            tokens.append(("COMMENT",comment))
            continue

        whitespace, s = lex_whitespace(s)
        if whitespace != None:
            continue

        newline, s = lex_new_line(s)
        if newline != None:
            line_counter+=1
            continue

        section_name, s = lex_section_name(s)
        if section_name != None:
            tokens.append(("SECTIONS", section_name))
            continue

        key, s = lex_key(s)
        if key != None:
            value, s = lex_value(s)
            tokens.append(("KEY_VALUE", key, value))
            continue
        raise Exception(f"Ошибка в {line_counter}: '{s[0]}'")
    
    return tokens

def consolidation(tokens): # производит десереализацию
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
            
            ron_value = value
            result[current_section][key] = ron_value
    return result

def main():

    s = """
    even_week = false
    group_name = P3132
    date = Tuesday, 28 Oct 2025 UTC +03:00
    my_isu = 502873
    my_varient = 85
    my_name = Малых Кирилл Романович

    [class_1]
    title = Алгебра и алгоритмы (Базовый уровень)
    class_format = Очный
    type_title = Лекция
    campus_address = Кронверкский пр., д.49, лит.А
    from_time = 9:50
    to_time = 11:20
    auditory_name = ауд. 1506
    teacher_name = Кольцова Татьяна Борисовна

    [class_2]
    title = Алгебра и алгоритмы (Базовый уровень)
    class_format = Очный
    type_title = Практика
    campus_address = Кронверкский пр., д.49, лит.А
    from_time = 11:30
    to_time = 13:00
    auditory_name = ауд. 2306/1
    teacher_name = Митина Татьяна Евгеньевна

    [class_3]
    title = Математический анализ (Базовый уровень)
    class_format = Очный
    type_title = Лекция
    campus_address = Кронверкский пр., д.49, лит.А
    from_time = 13:30
    to_time = 15:00
    auditory_name = ауд. 1506
    teacher_name = Кольцова Татьяна Борисовна

    [class_4]
    title = Математический анализ (Базовый уровень)
    class_format = Очный
    type_title = Практика
    campus_address = Кронверкский пр., д.49, лит.А
    from_time = 15:30
    to_time = 17:00
    auditory_name = ауд. 2306/2
    teacher_name = Кочевадов Виталий Алексеевич
"""
    tokens = lex_for_ini(s)
    result = consolidation(tokens)
    print(result)
    
main()