import csv


# Определяется функция read_csv, которая принимает один аргумент file_path
def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        # with используется для автоматического закрытия файла после завершения чтения\редактирования
        # newline='' предотвращает добавление лишних пустых строк
        # вызываем класс чтения из модуля csv и преобразовываем в словарь
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data


# Функция записи данных в файл
def write_csv(file_path, data, fieldnames):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        # with используется для автоматического закрытия файла после завершения
        # 'w' означает возможность записи файла, режим работы с файлом
        # newline='' предотвращает добавление лишних пустых строк
        # вызываем класс записи из модуля csv и записываем заголовки, затем остальные данные
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def sort_data(data, sort_key, numeric=False):
    # функция сортировки данных
    # по умолчанию функция sorted сортирует элементы списка по алфавиту (или в порядке возрастания)
    # функция lambda проверяет параметр numeric и либо преобразует значение ключа в целое число для числовой сортировки
    # либо оставляет его строкой для строковой сортировки
    return sorted(data, key=lambda x: int(x[sort_key]) if numeric else x[sort_key])


def filter_data(data, criterion_key, criterion_value, numeric=False):
    # функция фильтрации данных
    # если параметр numeric равен True
    # возвращается новый список, содержащий только те элементы, которые удовлетворяют условию
    if numeric:
        return [item for item in data if int(item[criterion_key]) > criterion_value]
    else:
        return [item for item in data if item[criterion_key] == criterion_value]


def main():
    file_path = 'data1.csv'
    data = read_csv(file_path)
    # выведем data для понимания работы функции
    print("Вводные данные из файла csv:")
    for row in data:
        print(row)
    fieldnames = ['№', 'Кличка', 'Порода', 'Возраст']

    # Сортировка по строковому полю (например, "Кличка")
    sorted_by_name = sort_data(data, 'Кличка')
    print("\nСортировка по Кличке (задание 2.1):")
    for row in sorted_by_name:
        print(row)

    # Сортировка по числовому полю (например, "Возраст")
    sorted_by_age = sort_data(data, 'Возраст', numeric=True)
    print("\nСортировка по Возрасту (задание 2.2):")
    # выводим в читабельном виде, каждую строку с новой строки
    for row in sorted_by_age:
        print(row)

    # Фильтрация данных по критерию (например, возраст больше 5)
    filtered_data = filter_data(data, 'Возраст', 5, numeric=True)
    print("\nФильтрация: Возраст больше 5 (задание 2.3)")
    # выводим в читабельном виде, каждую строку с новой строки
    for row in filtered_data:
        print(row)

    # Добавление новых данных (задание 3)
    new_data = {'№': '5', 'Кличка': 'Барсик', 'Порода': 'Сиамская кошка', 'Возраст': '3'}
    data.append(new_data)

    # Сохранение данных обратно в файл
    write_csv(file_path, data, fieldnames)

    data = read_csv(file_path)
    # выведем данные после записи
    print("\nКонечные данные в файле csv:")
    for row in data:
        print(row)


main()
