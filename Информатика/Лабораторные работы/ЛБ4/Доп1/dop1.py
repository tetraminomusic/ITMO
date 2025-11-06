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
    if "global" in result and len(result["global"]) > 0: #работаем со парами внутри глобальной секции
        for value_name in result["global"]:
            value = result["global"][value_name]
            lines.append(f"\t{value_name}{RON_COLON} {value}{RON_COMMA}")
        if len(result) > 1:
            lines.append("")
    
    for section_name in result:
        if section_name == "global": #пропускаем глобальную секцию
            continue
            
        section_items = result[section_name]
        if len(section_items) == 0: #скипаем пустые секции
            continue
        
        lines.append(f"\t{section_name}{RON_COLON} {{") #обработка секций
        for param_name in section_items:
            param_value = section_items[param_name]
            lines.append(f"\t\t{param_name}{RON_COLON} {convert_value_to_ron(param_value)}{RON_COMMA}")
        lines.append("\t}" + RON_COMMA)
        
        if section_name != list(result.keys())[-1]: #если секция не ластовая, то добавляем свободную строку
            lines.append("")
    
    lines.append(RON_OBJECT_CLOSE)
    return "\n".join(lines)

def convert_value_to_ron(value):
    if value == "": #работем с кавычками
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
    if ((value[0] == RON_QUOTE and value[-1] == RON_QUOTE) or (value[0] == RON_QUOTE and value[-1] == RON_QUOTE)): #если значение уже в кавычках
        return value
    return RON_QUOTE + value + RON_QUOTE #добавляем кавычки, если таковы не имеются

def main():
    s = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\dict.txt", encoding="utf-8").read()
    f = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\output.ron", "w", encoding="utf-8").write(generating_ron(eval(s)))
main()