
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data[:5])  # Показываем первые 5 записей
else:
    print(f"Ошибка {response.status_code}: Не удалось получить данные")


# Плюсы библиотеки Requsts:
# Получение данных с веб-страниц и их использование в коде
# Передача параметров, заголовков и аутентификации в запросах.
# Поддержка различных HTTP-методов.


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title('Простой график')
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.grid(True)
plt.show()

# Плюсы:
# Создание различных видов графиков.
# Настройка визуальных аспектов (цвета, маркеры, легенда).
# Сохранение графиков в файлы (PNG, PDF, SVG).

import pandas as pd

data = pd.read_csv('/Users/sabrzhan777gmail.com/PycharmProjects/pythonProject1/Module 1/pythonProject/data.csv')

stats = data.describe()

print("Статистика по данным:")
print(stats)

unique_counts = data['column_name'].value_counts()
print("\nКоличество уникальных значений по 'column_name':")
print(unique_counts)

#Возможности:
# Чтение и запись данных в различных форматах (CSV, Excel, SQL и т.д.).
# Удобные методы для анализа и манипуляции данными (фильтрация, группировка, агрегация).
# Легкий доступ к статистике по данным.
