import os

# Объявление функции
def count_files_in_directory(directory):
    try:
        # получаем список файлов в директории
        files = os.listdir(directory)
        # для наглядности можно вывести, что записалось в переменную
        # видим список(list) всего содержимого в директории
        print (files)
        # цикл проходит по элементам и с  помощью if проверяет на то файл ли это, или что-то другое
        # возвращает 1 для каждого элемента item в списке files, который является файлом
        # os.path.join() добавляет к пути директории наименование файла (или папки, что встречает на пути)
        # и if os.path.isfile() проверяет, является ли этот путь, созданный функцией, файлом (true\false)
        file_count = sum(1 for item in files if os.path.isfile(os.path.join(directory, item)))
        print(f"Количество файлов в директории '{directory}': {file_count}")
    except FileNotFoundError:
        print(f"Директория '{directory}' не найдена.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Указываю путь к интересующей директории
directory_path = 'C:\\Users\\ADmin\\PythonProjects\\labs\\folder_with_files'
# Вызываю функцию
count_files_in_directory(directory_path)