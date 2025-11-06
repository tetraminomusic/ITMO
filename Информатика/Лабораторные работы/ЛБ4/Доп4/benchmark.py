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
    sys.stdout = StringIO() #создаём виртуальной консоли в озу
    
    start_time = time.time()
    for i in range(100):
        # Загружаем и выполняем модуль каждый раз
        spec = importlib.util.spec_from_file_location("test", file_path) #спецификация модуля из файла, чтобы консоль понимала, как загрузить модуль
        module = importlib.util.module_from_spec(spec) # создаёт пустой объект модуля на основе спецификации (оболочка)
        spec.loader.exec_module(module) # выполняется код в контексте созданного объекта модуля
        module.main() # вызов функции
    
    total_time = time.time() - start_time
    
    # Восстанавливаем stdout
    sys.stdout = original_stdout
    
    print(total_time, "seconds")
    return total_time

print("nolib.py")
time1 = benchmark(NO_LIB)
    
print("withlib.py")
time2 = benchmark(WITH_LIB)