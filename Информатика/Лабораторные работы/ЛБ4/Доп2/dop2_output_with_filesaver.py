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
    
    # Конвертация в json
    json_str = json.dumps(processed_data, ensure_ascii=False, indent=2)
    
    # Заменяем только внешние скобки
    if json_str.startswith('{') and json_str.endswith('}'):
        return RON_OBJECT_OPEN + json_str[1:-1] + RON_OBJECT_CLOSE
    return json_str

def convert_value(value): #здесь работаем только с числами
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
    s = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\dict.txt", encoding="utf-8").read()
    ron = generating_ron_simple(eval(s))
    f = open("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\output.ron", "w", encoding="utf-8").write(ron)

main()