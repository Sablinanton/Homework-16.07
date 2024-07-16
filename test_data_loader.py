import data_loader

# Тест загрузки данных из CSV
df_csv = data_loader.load_csv('C:\\Users\\DELTA\\homework-16.07\\Датасет Вино.csv')
print("CSV Data Loaded:")
print(df_csv.head())
