import configparser

def parser(ini_string):
    lines = ini_string.split('\n')
    processed_lines = []
    found_section = False
    
    for line in lines:
        stripped = line.strip()
        
        if not found_section and stripped.startswith('[') and stripped.endswith(']'): #добавляет первую глобальную секцию в самое начало
            if any('=' in l for l in processed_lines):
                processed_lines.insert(0, '[global]')
            found_section = True
        
        processed_lines.append(line)
    
    if not found_section and any('=' in line for line in processed_lines): #если из секций только глобальная
        processed_lines.insert(0, '[global]')
    
    processed_ini = '\n'.join(processed_lines) # обратно в строчки
    
    config = configparser.ConfigParser() #создаёт пустой экземпляр парсера
    config.read_string(processed_ini) # преобразует INI формат в бинарник
    return {section: dict(config[section]) for section in config.sections()} #преобразуем секции в словари

s = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\input.ini", encoding="utf-8").read()
result = parser(s)
f = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\dict.txt", "w", encoding="utf-8").write(str(result))