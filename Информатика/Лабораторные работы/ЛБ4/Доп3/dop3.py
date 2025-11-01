XML_PROLOG_START = '<?xml'
XML_PROLOG_END = '?>'
XML_VERSION = 'version="1.0"'
XML_ENCODING = 'encoding="UTF-8"'
XML_START_TAG_OPEN = '<'
XML_START_TAG_CLOSE = '>'
XML_END_TAG_OPEN = '</'
XML_END_TAG_CLOSE = '>'
XML_EMPTY_TAG_CLOSE = '/>'
XML_EQUAL = '='
XML_QUOTE = '"'
XML_APOSTROPHE = "'"
XML_AMPERSAND = '&'
XML_LESS_THAN = '<'
XML_GREATER_THAN = '>'
XML_ESCAPED_AMPERSAND = '&amp;'
XML_ESCAPED_LESS_THAN = '&lt;'
XML_ESCAPED_GREATER_THAN = '&gt;'
XML_ESCAPED_QUOTE = '&quot;'
XML_ESCAPED_APOSTROPHE = '&apos;'


def escape_xml(text):
    """Экранирование специальных символов для XML"""
    return str(text)\
            .replace(XML_AMPERSAND, XML_ESCAPED_AMPERSAND)\
            .replace(XML_LESS_THAN, XML_ESCAPED_LESS_THAN)\
            .replace(XML_GREATER_THAN, XML_ESCAPED_GREATER_THAN)\
            .replace(XML_QUOTE, XML_ESCAPED_QUOTE)\
            .replace(XML_APOSTROPHE, XML_ESCAPED_APOSTROPHE)

def generating_xml(result):
    lines = []
    lines.append(f'{XML_PROLOG_START} {XML_VERSION} {XML_ENCODING}{XML_PROLOG_END}')
    lines.append(f'{XML_START_TAG_OPEN}schedule{XML_START_TAG_CLOSE}')
    
    # Глобальные параметры
    if "global" in result and len(result["global"]) > 0:
        lines.append(f'\t{XML_START_TAG_OPEN}global{XML_START_TAG_CLOSE}')
        for key, value in result["global"].items():
            escaped_value = escape_xml(value)
            lines.append(f'\t\t{XML_START_TAG_OPEN}{key}{XML_START_TAG_CLOSE}{escaped_value}{XML_END_TAG_OPEN}{key}{XML_END_TAG_CLOSE}')
        lines.append(f'\t{XML_END_TAG_OPEN}global{XML_END_TAG_CLOSE}')
    
    # Секции классов
    for section_name in result:
        if section_name == "global": #пропускаем глобальньую секцию
            continue
            
        section_items = result[section_name]
        if len(section_items) == 0: #пропускаем пустые секции
            continue
        
        lines.append(f'\t<{section_name}>')
        for key, value in section_items.items():
            escaped_value = escape_xml(value)
            lines.append(f'\t\t{XML_START_TAG_OPEN}{key}{XML_START_TAG_CLOSE}{escaped_value}{XML_END_TAG_OPEN}{key}{XML_END_TAG_CLOSE}')
        lines.append(f'\t{XML_END_TAG_OPEN}{section_name}{XML_END_TAG_CLOSE}')
    
    lines.append(f'{XML_END_TAG_OPEN}schedule{XML_END_TAG_CLOSE}')
    return "\n".join(lines)

def main():
    s = "{'global': {'even_week': 'false', 'group_name': 'P3132', 'date': 'Tuesday, 28 Oct 2025 UTC +03:00', 'my_isu': '502873', 'my_varient': '85', 'my_name': 'Малых Кирилл Романович'}, 'class_1': {'title': 'Алгебра и алгоритмы (Базовый уровень)', 'class_format': 'Очный', 'type_title': 'Лекция', 'campus_address': 'Кронверкский пр., д.49, лит.А', 'from_time': '9:50', 'to_time': '11:20', 'auditory_name': 'ауд. 1506', 'teacher_name': 'Кольцова Татьяна Борисовна'}, 'class_2': {'title': 'Алгебра и алгоритмы (Базовый уровень)', 'class_format': 'Очный', 'type_title': 'Практика', 'campus_address': 'Кронверкский пр., д.49, лит.А', 'from_time': '11:30', 'to_time': '13:00', 'auditory_name': 'ауд. 2306/1', 'teacher_name': 'Митина Татьяна Евгеньевна'}, 'class_3': {'title': 'Математический анализ (Базовый уровень)', 'class_format': 'Очный', 'type_title': 'Лекция', 'campus_address': 'Кронверкский пр., д.49, лит.А', 'from_time': '13:30', 'to_time': '15:00', 'auditory_name': 'ауд. 1506', 'teacher_name': 'Кольцова Татьяна Борисовна'}, 'class_4': {'title': 'Математический анализ (Базовый уровень)', 'class_format': 'Очный', 'type_title': 'Практика', 'campus_address': 'Кронверкский пр., д.49, лит.А', 'from_time': '15:30', 'to_time': '17:00', 'auditory_name': 'ауд. 2306/2', 'teacher_name': 'Кочевадов Виталий Алексеевич'}}"
    xml_output = generating_xml(eval(s))
    print(xml_output)
main()