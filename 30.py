import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Створення "забрудненого" набору
data = {
    'Імʼя': ['Олег', 'Марина', 'Іван', '???', 'Анна', 'Вася', 'Оксана', 'Петро', 'Марія', 'Наталя'],
    'Вік': [25, 30, 17, 200, np.nan, 40, 35, 28, 27, 32],
    'Стать': ['Ч', 'Ж', 'Ч', 'А', 'Ж', 'Ч', np.nan, 'Ч', 'Ж', 'Ж'],
    'Місто': ['Київ', 'Львів', 'Харків', 'Київ', np.nan, 'Одеса', 'Львів', 'Львів', 'Одеса', 'Харків'],
    'Зарплата': [5000, 10000, 900000, 8000, 7500, np.nan, 6000, 3000, 7100, 9000],
    'Освіта': ['вища', 'вища', 'середня', '???', 'вища', 'вища', 'середня', 'вища', 'середня', 'початкова']
}
df = pd.DataFrame(data)

# Очищення
df['Імʼя'] = df['Імʼя'].replace('???', np.nan).fillna('Невідомо')
df['Вік'] = df['Вік'].apply(lambda x: np.nan if x > 100 or x < 14 else x)
df['Вік'] = df['Вік'].fillna(df['Вік'].median())
df['Стать'] = df['Стать'].where(df['Стать'].isin(['Ч', 'Ж']), np.nan).fillna(df['Стать'].mode()[0])
df['Місто'] = df['Місто'].fillna(df['Місто'].mode()[0])
df['Зарплата'] = df['Зарплата'].apply(lambda x: np.nan if x > 100000 else x)
df['Зарплата'] = df['Зарплата'].fillna(df['Зарплата'].median())
df['Освіта'] = df['Освіта'].replace('???', np.nan).fillna(df['Освіта'].mode()[0])

# Нормалізація та стандартизація
scaler_minmax = MinMaxScaler()
scaler_zscore = StandardScaler()
df['Зарплата_minmax'] = scaler_minmax.fit_transform(df[['Зарплата']])
df['Зарплата_zscore'] = scaler_zscore.fit_transform(df[['Зарплата']])

# Dummy-кодування (з перетворенням bool у int)
df_encoded = pd.get_dummies(df, columns=['Стать', 'Місто', 'Освіта'], dtype=int)

# Збереження
df_encoded.to_csv("prepared_dataset.csv", index=False)
df_encoded.to_csv("prepared_dataset.csv", index=False, sep=';', encoding='utf-8-sig')
