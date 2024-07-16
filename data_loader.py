import pandas as pd
import json
import requests
import matplotlib.pyplot as plt

def load_csv(file_path):
    """
    Загрузка данных из CSV файла.
    :param file_path: путь к CSV файлу
    :return: DataFrame с данными
    """
    return pd.read_csv(file_path, delimiter=';')

def load_json(file_path):
    """
    Загрузка данных из JSON файла.
    :param file_path: путь к JSON файлу
    :return: DataFrame с данными
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return pd.DataFrame(data)

def load_api(url):
    """
    Загрузка данных из API.
    :param url: URL API
    :return: DataFrame с данными
    """
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)

def plot_histogram(df, column):
    """
    Построение гистограммы для указанного столбца DataFrame.
    :param df: DataFrame с данными
    :param column: Столбец для построения гистограммы
    """
    plt.figure(figsize=(10, 6))
    df[column].hist(bins=30)
    plt.title(f'Гистограмма для {column}')
    plt.xlabel(column)
    plt.ylabel('Частота')
    plt.show()

def plot_line(df, x_column, y_column):
    """
    Построение линейного графика для указанных столбцов DataFrame.
    :param df: DataFrame с данными
    :param x_column: Столбец для оси X
    :param y_column: Столбец для оси Y
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_column], df[y_column], marker='o')
    plt.title(f'Линейный график {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def plot_scatter(df, x_column, y_column):
    """
    Построение диаграммы рассеяния для указанных столбцов DataFrame.
    :param df: DataFrame с данными
    :param x_column: Столбец для оси X
    :param y_column: Столбец для оси Y
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column])
    plt.title(f'Диаграмма рассеяния {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def count_missing_values(df):
    """
    Подсчет пустых или пропущенных значений в каждом столбце DataFrame.
    :param df: DataFrame с данными
    :return: Series с количеством пропущенных значений для каждого столбца
    """
    return df.isnull().sum()

def generate_missing_data_report(df):
    """
    Генерация отчета с информацией о пропущенных значениях.
    :param df: DataFrame с данными
    :return: DataFrame с информацией о пропущенных значениях
    """
    missing_data = count_missing_values(df)
    percent_missing = (missing_data / len(df)) * 100
    report = pd.DataFrame({'Missing Values': missing_data, 'Percentage': percent_missing})
    return report
