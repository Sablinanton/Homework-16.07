import data_loader

# Загрузка данных из CSV
df = data_loader.load_csv('C:\\Users\\DELTA\\homework-16.07\\Датасет Вино.csv')

# Тестирование функций визуализации
data_loader.plot_histogram(df, 'alcohol')  # Гистограмма для столбца 'alcohol'
data_loader.plot_line(df, 'fixed acidity', 'pH')  # Линейный график 'fixed acidity' vs 'pH'
data_loader.plot_scatter(df, 'fixed acidity', 'density')  # Диаграмма рассеяния 'fixed acidity' vs 'density'
