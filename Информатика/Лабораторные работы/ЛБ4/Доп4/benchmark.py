import time
import importlib.util
import sys
from io import StringIO

# Полные пути к файлам
NO_LIB = "C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\Доп4\\nolib.py"
WITH_LIB = "C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ4\\Доп4\\withlib.py"

def benchmark(file_path):
    # Перенаправляем stdout в буфер
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    
    start_time = time.time()
    for i in range(100):
        # Загружаем и выполняем модуль каждый раз
        spec = importlib.util.spec_from_file_location("test", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.main()
    
    total_time = time.time() - start_time
    
    # Восстанавливаем stdout
    sys.stdout = original_stdout
    
    print(total_time, "seconds")
    return total_time

if __name__ == "__main__":
    print("nolib.py")
    time1 = benchmark(NO_LIB)
    
    print("withlib.py")
    time2 = benchmark(WITH_LIB)