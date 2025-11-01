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

import json

RON_OBJECT_OPEN = "("
RON_OBJECT_CLOSE = ")"

def generating_ron_simple(data):
    # Убираем глобальную секцию
    if 'global' in data:
        processed_data = {}
        # Обрабатываем параметры из global
        for key, value in data['global'].items():
            processed_data[key] = convert_value(value)
        # Добавляем остальные секции
        for key, value in data.items():
            if key != 'global':
                processed_data[key] = {k: convert_value(v) for k, v in value.items()}
    else:
        processed_data = {k: convert_value(v) for k, v in data.items()}
    
    # Конвертируем в JSON
    json_str = json.dumps(processed_data, ensure_ascii=False, indent=2)
    
    # Заменяем только внешние скобки
    if json_str.startswith('{') and json_str.endswith('}'):
        return RON_OBJECT_OPEN + json_str[1:-1] + RON_OBJECT_CLOSE
    return json_str

def convert_value(value):
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value
    return value
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
    result = simple_ini_parser(s)
    print(generating_ron_simple(result))

main()