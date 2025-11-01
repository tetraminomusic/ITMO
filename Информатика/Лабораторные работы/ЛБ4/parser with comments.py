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
            tokens.append(("COMMENT", comment))
            continue  # ✅ Важно: continue после комментария

        whitespace, s = lex_whitespace(s)
        if whitespace != None:
            continue

        newline, s = lex_new_line(s)
        if newline != None:
            line_counter += 1
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

def consolidation(tokens):
    result = {}
    current_section = "global"
    result[current_section] = {}
    comments = []  # Храним комментарии для текущей позиции

    for token in tokens:
        if token[0] == "COMMENT":
            # Сохраняем комментарий для текущей позиции
            comments.append(token[1])
            
        elif token[0] == "SECTIONS":
            current_section = token[1]
            if current_section not in result:
                result[current_section] = {}
            
            # Сохраняем комментарии перед секцией
            if comments:
                result[current_section]['__comments_before__'] = comments.copy()
                comments.clear()
                
        elif token[0] == "KEY_VALUE":
            key, value = token[1], token[2]
            ron_value = convert_value_to_ron(value)
            result[current_section][key] = ron_value
            
            # Сохраняем комментарии перед ключом
            if comments:
                result[current_section][f'__comment_before_{key}__'] = comments.copy()
                comments.clear()
    
    # Сохраняем оставшиеся комментарии в конце файла
    if comments:
        result['__end_comments__'] = comments
    
    return result

def generating_ron(result):
    lines = []
    lines.append("(")  # Начало общей структуры
    
    # Сначала добавляем глобальные параметры
    if "global" in result and len(result["global"]) > 0:
        # Комментарии перед глобальными параметрами
        if '__comments_before__' in result["global"]:
            for comment in result["global"]['__comments_before__']:
                lines.append(f"    // {comment}")
        
        for value_name in result["global"]:
            if not value_name.startswith('__comment_'):  # Пропускаем служебные поля
                # Комментарии перед конкретным ключом
                comment_key = f'__comment_before_{value_name}__'
                if comment_key in result["global"]:
                    for comment in result["global"][comment_key]:
                        lines.append(f"    // {comment}")
                
                value = result["global"][value_name]
                lines.append(f"    {value_name}: {value},")
        
        # Добавляем пустую строку после глобальных параметров, если есть другие секции
        if len(result) > 1:
            lines.append("")
    
    # Затем добавляем все секции как вложенные структуры
    section_names = [name for name in result if name != "global" and name != "__end_comments__"]
    
    for i, section_name in enumerate(section_names):
        section_items = result[section_name]
        if len(section_items) == 0:
            continue
        
        # Комментарии перед секцией
        if '__comments_before__' in section_items:
            for comment in section_items['__comments_before__']:
                lines.append(f"    // {comment}")
        
        # Добавляем пустую строку перед первой секцией, если есть глобальные параметры
        if i == 0 and "global" in result and len(result["global"]) > 0:
            lines.append("")
        
        lines.append(f"    {section_name}: {{")
        for param_name in section_items:
            if not param_name.startswith('__comment_'):  # Пропускаем служебные поля
                # Комментарии перед конкретным параметром
                comment_key = f'__comment_before_{param_name}__'
                if comment_key in section_items:
                    for comment in section_items[comment_key]:
                        lines.append(f"        // {comment}")
                
                param_value = section_items[param_name]
                lines.append(f"        {param_name}: {param_value},")
        lines.append("    },")
        
        # Добавляем пустую строку между секциями (кроме последней)
        if i < len(section_names) - 1:
            lines.append("")
    
    # Комментарии в конце файла
    if '__end_comments__' in result:
        if lines and lines[-1] != "":
            lines.append("")
        for comment in result['__end_comments__']:
            lines.append(f"    // {comment}")
    
    lines.append(")")  # Конец общей структуры
    return "\n".join(lines)

def convert_value_to_ron(value):
    if value == "":
        return '""'
    
    if value.lower() in ("true","false"): #работаем с типами boolean
        return value.lower()
    
    if value.lower() in ("null","none"): #работаем с типом none и null
        return "None"
    
    try: #работаем с дробными и целыми числами
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        pass
    if ((value[0] == '"' and value[-1] == '"') or (value[0] == "'" and value[-1] == "'")):
        return value
    return f'"{value}"'

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

    ; Что-то вроде комментария

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
    print(generating_ron(result))

main()