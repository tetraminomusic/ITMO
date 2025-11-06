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
    # Экранирование специальных символов для XML
    return str(text)\
            .replace(XML_AMPERSAND, XML_ESCAPED_AMPERSAND)\
            .replace(XML_LESS_THAN, XML_ESCAPED_LESS_THAN)\
            .replace(XML_GREATER_THAN, XML_ESCAPED_GREATER_THAN)\
            .replace(XML_QUOTE, XML_ESCAPED_QUOTE)\
            .replace(XML_APOSTROPHE, XML_ESCAPED_APOSTROPHE)

def generating_xml(result, current_tag="schedule", indent_level=0):
    lines = []
    indent = "\t" * indent_level
    indent_inner = '\t' * (indent_level+1)
    
    if indent_level == 0:
        lines.append(f'{XML_PROLOG_START} {XML_VERSION} {XML_ENCODING}{XML_PROLOG_END}')
        lines.append(f'{XML_START_TAG_OPEN}{current_tag}{XML_START_TAG_CLOSE}')
    
    for key, value in result.items():
        if key == "global" and indent_level > 0:
            continue
            
        if isinstance(value, dict):
            # Вложенная секция (словарь)
            lines.append(f'{indent_inner}{XML_START_TAG_OPEN}{key}{XML_START_TAG_CLOSE}')
            lines.append(generating_xml(value, key, indent_level + 1))
            lines.append(f'{indent_inner}{XML_END_TAG_OPEN}{key}{XML_END_TAG_CLOSE}')
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    lines.append(f'{indent_inner}{XML_START_TAG_OPEN}{key}{XML_START_TAG_CLOSE}')
                    lines.append(generating_xml(item, key, indent_level + 1))
                    lines.append(f'{indent_inner}{XML_END_TAG_OPEN}{key}{XML_END_TAG_CLOSE}')
                else:
                    escaped_value = escape_xml(item)
                    lines.append(f'{indent_inner}{XML_START_TAG_OPEN}{key}{XML_START_TAG_CLOSE}{escaped_value}{XML_END_TAG_OPEN}{key}{XML_END_TAG_CLOSE}')
        else:
            escaped_value = escape_xml(value)
            lines.append(f'{indent_inner}{XML_START_TAG_OPEN}{key}{XML_START_TAG_CLOSE}{escaped_value}{XML_END_TAG_OPEN}{key}{XML_END_TAG_CLOSE}')
    
    # Закрываем корневой тег только для корневого элемента
    if indent_level == 0:
        lines.append(f'{XML_END_TAG_OPEN}{current_tag}{XML_END_TAG_CLOSE}')
    
    return "\n".join(lines)

def main():
    s = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\dict.txt", encoding="utf-8").read()
    xml_output = generating_xml(eval(s))
    f = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\output.xml", "w", encoding="utf-8").write(xml_output)

main()