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
    #Экранирование специальных символов для XML
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
        
        lines.append(f'\t{XML_START_TAG_OPEN}{section_name}{XML_START_TAG_CLOSE}')
        for key, value in section_items.items():
            escaped_value = escape_xml(value)
            lines.append(f'\t\t{XML_START_TAG_OPEN}{key}{XML_START_TAG_CLOSE}{escaped_value}{XML_END_TAG_OPEN}{key}{XML_END_TAG_CLOSE}')
        lines.append(f'\t{XML_END_TAG_OPEN}{section_name}{XML_END_TAG_CLOSE}')
    
    lines.append(f'{XML_END_TAG_OPEN}schedule{XML_END_TAG_CLOSE}')
    return "\n".join(lines)

def main():
    s = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\dict.txt", encoding="utf-8").read()
    xml_output = generating_xml(eval(s))
    f = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\output.xml", "w", encoding="utf-8").write(xml_output)
main()