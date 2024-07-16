import data_loader

# Тест загрузки данных из CSV
df_csv = data_loader.load_csv('C:\\Users\\DELTA\\homework-16.07\\Датасет Вино.csv')
print("CSV Data Loaded:")
print(df_csv.head())

# Здесь вы можете добавить тесты для JSON и API, если у вас есть соответствующие файлы и URL
