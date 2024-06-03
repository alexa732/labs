import numpy as np

# Объявление функции генерации рандомом матрицы
def generate_matrix_a(n, m):
    # Генерирует матрицу размером n на m со случайными элементами (от -100 до 100)
    return np.random.randint(-100, 100, size=(n, m))

# Объявление функции с поиском максим.значений элементов столбца матрицы
def column_with_max_abs_sum(matrix_a):
    # Находит индекс столбца с максимальной суммой абсолютных значений элементов
    # Так как нужна сумма значений, np.abs(matrix_a) делает все элементы "положительными" (модуль числа)
    # axis=0 означает, что суммируем по столбцам
    abs_sums = np.sum(np.abs(matrix_a), axis=0)
    return np.argmax(abs_sums)

# Функция поиска наименьшего элемента в заданном столбце матрицы
def min_element_in_column(matrix_a, column_index):
    # ':' означает, что мы выбираем все строки
    return np.min(matrix_a[:, column_index])


# Функция записи данных в файл .txt
def save_to_file(filename, data):
    # with используется для автоматического закрытия файла после завершения
    # 'w' означает возможность записи файла, режим работы с файлом
    with open(filename, 'w') as file:
        file.write(data)


def main(n, m, filename):
    # Главная функция, выполняющая все шаги обработки матрицы из задания
    matrix_a = generate_matrix_a(n, m)
    max_abs_sum_col_index = column_with_max_abs_sum(matrix_a)
    min_element = min_element_in_column(matrix_a, max_abs_sum_col_index)

    # Получаем результат
    result = (
        f"Сгенерированная матрица:\n{matrix_a}\n\n"
        f"Индекс столбца с максимальной суммой абсолютных значений: {max_abs_sum_col_index}\n"
        f"Наименьший элемент в этом столбце: {min_element}\n"
    )

    save_to_file(filename, result)



N = 5  # Количество строк
M = 4  # Количество столбцов

FILENAME = "result.txt"

main(N, M, FILENAME)
