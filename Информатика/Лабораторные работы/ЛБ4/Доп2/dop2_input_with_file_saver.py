import configparser

def simple_ini_parser(ini_string):
    lines = ini_string.split('\n')
    processed_lines = []
    found_section = False
    
    for line in lines:
        stripped = line.strip()
        
        if not found_section and stripped.startswith('[') and stripped.endswith(']'):
            if any('=' in l for l in processed_lines):
                processed_lines.insert(0, '[global]')
            found_section = True
        
        processed_lines.append(line)
    
    if not found_section and any('=' in line for line in processed_lines):
        processed_lines.insert(0, '[global]')
    
    processed_ini = '\n'.join(processed_lines)
    
    config = configparser.ConfigParser()
    config.read_string(processed_ini)
    
    return {section: dict(config[section]) for section in config.sections()}

s = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\input.ini", encoding="utf-8").read()
result = simple_ini_parser(s)
f = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\dict.txt", "w", encoding="utf-8").write(str(result))