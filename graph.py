import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# считаем данные из csv файла
data = pd.read_csv("covid_19_data.csv")

# определим размер набора данных
data.shape

# Sample data output
print(data.head())
