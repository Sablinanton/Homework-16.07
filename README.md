report_content = """
Отчет о выполнении домашних заданий

Задание 1: Создание модуля data_loader для загрузки данных из различных источников (CSV, JSON, API)
-----------------------------------------------------------------------------------
Был создан модуль data_loader.py, содержащий функции для загрузки данных из CSV, JSON файлов и API.
Функции:
1. load_csv(file_path): Загружает данные из CSV файла и возвращает DataFrame.
2. load_json(file_path): Загружает данные из JSON файла и возвращает DataFrame.
3. load_api(url): Загружает данные из API и возвращает DataFrame.

Задание 2: Создание методов для добавления и удаления различных типов визуализации
-----------------------------------------------------------------------------------
Были добавлены функции для построения гистограмм, линейных графиков и диаграмм рассеяния.
Функции:
1. plot_histogram(df, column): Строит гистограмму для указанного столбца DataFrame.
2. plot_line(df, x_column, y_column): Строит линейный график для указанных столбцов DataFrame.
3. plot_scatter(df, x_column, y_column): Строит диаграмму рассеяния для указанных столбцов DataFrame.

Задание 3: Создание метода для подсчета пустых или пропущенных значений в каждом столбце DataFrame
-----------------------------------------------------------------------------------
Были добавлены функции для подсчета пропущенных значений и генерации отчета о пропущенных значениях.
Функции:
1. count_missing_values(df): Подсчитывает пропущенные значения в каждом столбце DataFrame.
2. generate_missing_data_report(df): Генерирует отчет о пропущенных значениях.
"""

with open('README.txt', 'w', encoding='utf-8') as file:
    file.write(report_content)
