import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import os

# Заголовок приложения
st.title("Анализ температурных данных и мониторинг температуры")

# Файл для загрузки CSV
uploaded_file = st.file_uploader("Загрузите CSV-файл с историческими данными", type=["csv"])

# Поле для API-ключа OpenWeatherMap
API_KEY = st.text_input("Введите API-ключ OpenWeatherMap", type="password")

# Функция для загрузки данных
def load_data(file):
    df = pd.read_csv(file, parse_dates=['timestamp'])
    return df

# Функция для получения текущей температуры через OpenWeatherMap API
def get_current_temperature(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['main']['temp']
    else:
        return None

# Если загружен файл, обрабатываем его
if uploaded_file:
    df = load_data(uploaded_file)

    # Выводим часть данных
    st.write("### Загруженные данные")
    st.write(df.head())

    # Выбираем город для анализа
    cities = df['city'].unique()
    selected_city = st.selectbox("Выберите город", cities)

    # Фильтруем данные по городу
    city_data = df[df['city'] == selected_city]

    # График временного ряда температур
    fig = px.line(city_data, x='timestamp', y='temperature', title=f'Температура в {selected_city}')
    st.plotly_chart(fig)

    # График сезонных профилей
    season_fig = px.box(df[df['city'] == selected_city], x='season', y='temperature', title=f'Сезонные профили {selected_city}')
    st.plotly_chart(season_fig)

    # Получение текущей температуры, если введен API-ключ
    if API_KEY:
        if st.button("Получить текущую температуру"):
            temp = get_current_temperature(selected_city, API_KEY)
            if temp is not None:
                st.write(f"### Текущая температура в {selected_city}: {temp}°C")
            else:
                st.error("Ошибка получения данных. Проверьте API-ключ и попробуйте снова.")
    else:
        st.warning("Введите API-ключ, чтобы получить данные о текущей температуре.")
