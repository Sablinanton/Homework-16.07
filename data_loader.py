import pandas as pd
import json
import requests
import matplotlib.pyplot as plt

def load_csv(file_path):
    return pd.read_csv(file_path, delimiter=';')

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return pd.DataFrame(data)

def load_api(url):
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)

def plot_histogram(df, column):
    plt.figure(figsize=(10, 6))
    df[column].hist(bins=30)
    plt.title(f'Гистограмма для {column}')
    plt.xlabel(column)
    plt.ylabel('Частота')
    plt.show()

def plot_line(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_column], df[y_column], marker='o')
    plt.title(f'Линейный график {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def plot_scatter(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column])
    plt.title(f'Диаграмма рассеяния {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()
