import data_loader

# Загрузка данных из CSV
df = data_loader.load_csv('C:\\Users\\DELTA\\homework-16.07\\Датасет Вино.csv')

# Тестирование функции подсчета пропущенных значений
missing_values = data_loader.count_missing_values(df)
print("Missing Values:")
print(missing_values)

# Тестирование функции генерации отчета о пропущенных значениях
missing_data_report = data_loader.generate_missing_data_report(df)
print("Missing Data Report:")
print(missing_data_report)
