import pandas as pd
import json
import requests

def load_csv(file_path):
    """
    Загрузка данных из CSV файла.
    :param file_path: путь к CSV файлу
    :return: DataFrame с данными
    """
    return pd.read_csv(file_path)

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
