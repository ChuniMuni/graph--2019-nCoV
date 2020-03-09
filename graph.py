import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# считаем данные из csv файла
data = pd.read_csv("covid_19_data.csv")

# определим размер набора данных
data.shape

# Sample data output
# print(data.head())

data.describe()

# Проверка на дубликаты
# print(sum(data.duplicated(['Country/Region', 'Province/State', 'ObservationDate'])))

data.loc[data['Country/Region'] == 'Mainland China', 'Country/Region'] = 'China'

# Выводим общий список
country_list = data['Country/Region'].unique()
print('Коронавирус COVID19 обнаружен в {} странах:'.format(country_list.size))

for country in sorted(country_list):
    print('- {}'.format(country))

# Анализ по отдельной стране
var = data[data['Country/Region'] == 'Russia']
print(var)
