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

def generating_ron(result,indent_level=0):
    lines = []
    indent = "\t" * indent_level
    inner_indent = "\t" * (indent_level + 1)
    
    lines.append(indent + RON_OBJECT_OPEN) 
    
    keys = list(result.keys())
    i = 0
    while i < len(keys):
        key = keys[i]
        value = result[key]
        
        if isinstance(value, dict):
            line_content = f"{inner_indent}{key}{RON_COLON} {generating_ron(value, indent_level + 1)}"
        else:
            line_content = f"{inner_indent}{key}{RON_COLON} {convert_value_to_ron(value)}"
        
        if i < len(keys) - 1:
            line_content += RON_COMMA 
        
        lines.append(line_content)
        i += 1
    
    lines.append(indent + RON_OBJECT_CLOSE)
    return "\n".join(lines)

def convert_value_to_ron(value):
    if isinstance(value, (list, tuple)):
        items = [convert_value_to_ron(item) for item in value]
        return RON_ARRAY_OPEN + ", ".join(items) + RON_ARRAY_CLOSE
    
    if isinstance(value, dict):  # Обработка вложенных объектов (на всякий случай)
        return generating_ron(value)
    
    value_str = str(value)
    
    if value_str == "":  # работаем с кавычками
        return RON_QUOTE + RON_QUOTE
    
    if value_str.lower() in (RON_BOOLEAN_TRUE, RON_BOOLEAN_FALSE):  # работаем с типами boolean
        return value_str.lower()
    
    if value_str.lower() in ("null", RON_NONE.lower()):  # работаем с типом none и null
        return RON_NONE
    
    try:  # работаем с дробными и целыми числами
        if "." in value_str:
            return float(value_str)
        return int(value_str)
    except ValueError:
        pass
    
    if ((value_str[0] == RON_QUOTE and value_str[-1] == RON_QUOTE) or 
        (value_str[0] == "'" and value_str[-1] == "'")):  # если значение уже в кавычках
        return value_str
    
    return RON_QUOTE + value_str + RON_QUOTE  # добавляем кавычки, если таковы не имеются

def main():
    s = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\dict.txt", encoding="utf-8").read()
    f = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\output.ron", "w", encoding="utf-8").write(generating_ron(eval(s)))

main()