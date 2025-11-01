RON_OBJECT_OPEN = "("
RON_OBJECT_CLOSE = ")"
RON_ARRAY_OPEN = "["
RON_ARRAY_CLOSE = "]"
RON_COLON = ":"
RON_COMMA = ","
RON_QUOTE = '"'
RON_NONE = "None"
RON_BOOLEAN_TRUE = "true"
RON_BOOLEAN_FALSE = "false"

def generating_ron(result):
    lines = []
    lines.append(RON_OBJECT_OPEN) 
    if "global" in result and len(result["global"]) > 0:
        for value_name in result["global"]:
            value = result["global"][value_name]
            lines.append(f"\t{value_name}{RON_COLON} {value}{RON_COMMA}")
        if len(result) > 1:
            lines.append("")
    
    for section_name in result:
        if section_name == "global":
            continue
            
        section_items = result[section_name]
        if len(section_items) == 0:
            continue
        
        lines.append(f"\t{section_name}{RON_COLON} {{")
        for param_name in section_items:
            param_value = section_items[param_name]
            lines.append(f"\t\t{param_name}{RON_COLON} {convert_value_to_ron(param_value)}{RON_COMMA}")
        lines.append("\t}" + RON_COMMA)
        
        if section_name != list(result.keys())[-1]:
            lines.append("")
    
    lines.append(RON_OBJECT_CLOSE)
    return "\n".join(lines)

def convert_value_to_ron(value):
    if value == "":
        return RON_QUOTE + RON_QUOTE
    
    if value.lower() in (RON_BOOLEAN_TRUE,RON_BOOLEAN_FALSE): #работаем с типами boolean
        return value.lower()
    
    if value.lower() in ("null", RON_NONE.lower()): #работаем с типом none и null
        return RON_NONE
    
    try: #работаем с дробными и целыми числами
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        pass
    if ((value[0] == RON_QUOTE and value[-1] == RON_QUOTE) or (value[0] == RON_QUOTE and value[-1] == RON_QUOTE)):
        return value
    return RON_QUOTE + value + RON_QUOTE

def main():
    s = "{'global': {'even_week': 'false', 'group_name': 'P3132', 'date': 'Tuesday, 28 Oct 2025 UTC +03:00', 'my_isu': '502873', 'my_varient': '85', 'my_name': 'Малых Кирилл Романович'}, 'class_1': {'title': 'Алгебра и алгоритмы (Базовый уровень)', 'class_format': 'Очный', 'type_title': 'Лекция', 'campus_address': 'Кронверкский пр., д.49, лит.А', 'from_time': '9:50', 'to_time': '11:20', 'auditory_name': 'ауд. 1506', 'teacher_name': 'Кольцова Татьяна Борисовна'}, 'class_2': {'title': 'Алгебра и алгоритмы (Базовый уровень)', 'class_format': 'Очный', 'type_title': 'Практика', 'campus_address': 'Кронверкский пр., д.49, лит.А', 'from_time': '11:30', 'to_time': '13:00', 'auditory_name': 'ауд. 2306/1', 'teacher_name': 'Митина Татьяна Евгеньевна'}, 'class_3': {'title': 'Математический анализ (Базовый уровень)', 'class_format': 'Очный', 'type_title': 'Лекция', 'campus_address': 'Кронверкский пр., д.49, лит.А', 'from_time': '13:30', 'to_time': '15:00', 'auditory_name': 'ауд. 1506', 'teacher_name': 'Кольцова Татьяна Борисовна'}, 'class_4': {'title': 'Математический анализ (Базовый уровень)', 'class_format': 'Очный', 'type_title': 'Практика', 'campus_address': 'Кронверкский пр., д.49, лит.А', 'from_time': '15:30', 'to_time': '17:00', 'auditory_name': 'ауд. 2306/2', 'teacher_name': 'Кочевадов Виталий Алексеевич'}}"
    print(generating_ron(eval(s)))
main()