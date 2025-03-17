# -*- coding: utf-8 -*-
"""Копия блокнота "hw streamlit.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g3gNlDK2Y5b5H4m44aCGftu4So-jpDkf

## Анализ температурных данных и мониторинг текущей температуры через OpenWeatherMap API

**Описание задания:**  
Вы аналитик в компании, занимающейся изучением климатических изменений и мониторингом температур в разных городах. Вам нужно провести анализ исторических данных о температуре для выявления сезонных закономерностей и аномалий. Также необходимо подключить API OpenWeatherMap для получения текущей температуры в выбранных городах и сравнить её с историческими данными.


### Цели задания:
1. Провести **анализ временных рядов**, включая:
   - Вычисление скользящего среднего и стандартного отклонения для сглаживания температурных колебаний.
   - Определение аномалий на основе отклонений температуры от $ \text{скользящее среднее} \pm 2\sigma $.
   - Построение долгосрочных трендов изменения температуры.
   - Любые дополнительные исследования будут вам в плюс.

2. Осуществить **мониторинг текущей температуры**:
   - Получить текущую температуру через OpenWeatherMap API.
   - Сравнить её с историческим нормальным диапазоном для текущего сезона.

3. Разработать **интерактивное приложение**:
   - Дать пользователю возможность выбрать город.
   - Отобразить результаты анализа температур, включая временные ряды, сезонные профили и аномалии.
   - Провести анализ текущей температуры в контексте исторических данных.
   - Любые графики должны быть интерактивными.


### Описание данных
Исторические данные о температуре содержатся в файле `temperature_data.csv`, включают:
  - `city`: Название города.
  - `timestamp`: Дата (с шагом в 1 день).
  - `temperature`: Среднесуточная температура (в °C).
  - `season`: Сезон года (зима, весна, лето, осень).

Код для генерации файла вы найдете ниже.

### Этапы выполнения

1. **Анализ исторических данных**:
   - Вычислить **скользящее среднее** температуры с окном в 30 дней для сглаживания краткосрочных колебаний.
   - Рассчитать среднюю температуру и стандартное отклонение для каждого сезона в каждом городе.
   - Выявить аномалии, где температура выходит за пределы $ \text{среднее} \pm 2\sigma $.
   - Попробуйте распараллелить проведение этого анализа. Сравните скорость выполнения анализа с распараллеливанием и без него.

2. **Мониторинг текущей температуры**:
   - Подключить OpenWeatherMap API для получения текущей температуры города. Для получения API Key (бесплатно) надо зарегистрироваться на сайте. Обратите внимание, что API Key может активироваться только через 2-3 часа, это нормально. Посему получите ключ заранее.
   - Получить текущую температуру для выбранного города через OpenWeatherMap API.
   - Определить, является ли текущая температура нормальной, исходя из исторических данных для текущего сезона.
   - Данные на самом деле не совсем реальные (сюрпрайз). Поэтому на момент эксперимента погода в Берлине, Каире и Дубае была в рамках нормы, а в Пекине и Москве аномальная. Протестируйте свое решение для разных городов.
   - Попробуйте для получения текущей температуры использовать синхронные и асинхронные методы. Что здесь лучше использовать?

3. **Создание приложения на Streamlit**:
   - Добавить интерфейс для загрузки файла с историческими данными.
   - Добавить интерфейс для выбора города (из выпадающего списка).
   - Добавить форму для ввода API-ключа OpenWeatherMap. Когда он не введен, данные для текущей погоды не показываются. Если ключ некорректный, выведите на экран ошибку (должно приходить `{"cod":401, "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info."}`).
   - Отобразить:
     - Описательную статистику по историческим данным для города, можно добавить визуализации.
     - Временной ряд температур с выделением аномалий (например, точками другого цвета).
     - Сезонные профили с указанием среднего и стандартного отклонения.
   - Вывести текущую температуру через API и указать, нормальна ли она для сезона.

### Критерии оценивания

- Корректное проведение анализа данных – 1 балл.
- Исследование распараллеливания анализа – 1 балл.
- Корректный поиск аномалий – 1 балл.
- Подключение к API и корректность выполнения запроса – 1 балл.
- Проведение эксперимента с синхронным и асинхронным способом запроса к API – 1 балл.
- Создание интерфейса приложения streamlit в соответствии с описанием – 3 балла.
- Корректное отображение графиков и статистик, а также сезонных профилей – 1 балл.
- Корректный вывод текущей температуры в выбранном городе и проведение проверки на ее аномальность – 1 балл.
- Любая дополнительная функциональность приветствуется и оценивается бонусными баллами (не более 2 в сумме) на усмотрение проверяющего.

### Формат сдачи домашнего задания

Решение нужно развернуть в Streamlit Cloud (бесплатно)

*   Создаем новый репозиторий на GitHub.  
*   Загружаем проект.
*   Создаем аккаунт в [Streamlit Cloud](https://streamlit.io/cloud).
*   Авторизуемся в Streamlit Cloud.
*   Создаем новое приложение в Streamlit Cloud и подключаем GitHub-репозиторий.
*   Deploy!

Сдать в форму необходимо:
1. Ссылку на развернутое в Streamlit Cloud приложение.
2. Ссылку на код. Все выводы про, например, использование параллельности/асинхронности опишите в комментариях.

Не забудьте удалить ключ API и иную чувствительную информацию.

### Полезные ссылки
*   [Оформление задачи Титаник на Streamlit](https://github.com/evgpat/streamlit_demo)
*   [Документация Streamlit](https://docs.streamlit.io/)
*   [Блог о Streamlit](https://blog.streamlit.io/)
"""

import pandas as pd
import numpy as np

# Реальные средние температуры (примерные данные) для городов по сезонам
seasonal_temperatures = {
    "New York": {"winter": 0, "spring": 10, "summer": 25, "autumn": 15},
    "London": {"winter": 5, "spring": 11, "summer": 18, "autumn": 12},
    "Paris": {"winter": 4, "spring": 12, "summer": 20, "autumn": 13},
    "Tokyo": {"winter": 6, "spring": 15, "summer": 27, "autumn": 18},
    "Moscow": {"winter": -10, "spring": 5, "summer": 18, "autumn": 8},
    "Sydney": {"winter": 12, "spring": 18, "summer": 25, "autumn": 20},
    "Berlin": {"winter": 0, "spring": 10, "summer": 20, "autumn": 11},
    "Beijing": {"winter": -2, "spring": 13, "summer": 27, "autumn": 16},
    "Rio de Janeiro": {"winter": 20, "spring": 25, "summer": 30, "autumn": 25},
    "Dubai": {"winter": 20, "spring": 30, "summer": 40, "autumn": 30},
    "Los Angeles": {"winter": 15, "spring": 18, "summer": 25, "autumn": 20},
    "Singapore": {"winter": 27, "spring": 28, "summer": 28, "autumn": 27},
    "Mumbai": {"winter": 25, "spring": 30, "summer": 35, "autumn": 30},
    "Cairo": {"winter": 15, "spring": 25, "summer": 35, "autumn": 25},
    "Mexico City": {"winter": 12, "spring": 18, "summer": 20, "autumn": 15},
}

# Сопоставление месяцев с сезонами
month_to_season = {12: "winter", 1: "winter", 2: "winter",
                   3: "spring", 4: "spring", 5: "spring",
                   6: "summer", 7: "summer", 8: "summer",
                   9: "autumn", 10: "autumn", 11: "autumn"}

# Генерация данных о температуре
def generate_realistic_temperature_data(cities, num_years=10):
    dates = pd.date_range(start="2010-01-01", periods=365 * num_years, freq="D")
    data = []

    for city in cities:
        for date in dates:
            season = month_to_season[date.month]
            mean_temp = seasonal_temperatures[city][season]
            # Добавляем случайное отклонение
            temperature = np.random.normal(loc=mean_temp, scale=5)
            data.append({"city": city, "timestamp": date, "temperature": temperature})

    df = pd.DataFrame(data)
    df['season'] = df['timestamp'].dt.month.map(lambda x: month_to_season[x])
    return df

# Генерация данных
data = generate_realistic_temperature_data(list(seasonal_temperatures.keys()))
data.to_csv('temperature_data.csv', index=False)

!pip install streamlit pandas numpy requests plotly pyngrok

import os
os.environ["OPENWEATHER_API_KEY"] = "ad5501b1db0b4e17d1e0396615afe47f"

!pkill -f ngrok

import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
import os
import subprocess
from pyngrok import ngrok
from concurrent.futures import ThreadPoolExecutor
import time
NGROK_AUTH_TOKEN = "2uRWQsVBhRrursScvzOfGGB5gYq_4pAq9D9vD8RKjvPfmvriY"
!ngrok authtoken {NGROK_AUTH_TOKEN}
def load_data(file):
    df = pd.read_csv(file, parse_dates=['timestamp'])
    return df
def calculate_seasonal_stats(df):
    seasonal_stats = df.groupby(['city', 'season'])['temperature'].agg(['mean', 'std']).reset_index()
    return seasonal_stats
def calculate_moving_average(df, window=30):
    df['moving_avg'] = df.groupby('city')['temperature'].transform(lambda x: x.rolling(window, min_periods=1).mean())
    return df
def detect_anomalies(df, seasonal_stats):
    df = df.merge(seasonal_stats, on=['city', 'season'], how='left')
    df['upper_bound'] = df['mean'] + 2 * df['std']
    df['lower_bound'] = df['mean'] - 2 * df['std']
    df['anomaly'] = (df['temperature'] > df['upper_bound']) | (df['temperature'] < df['lower_bound'])
    return df
def parallel_analysis(df):
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        seasonal_stats = executor.submit(calculate_seasonal_stats, df).result()
        df = executor.submit(calculate_moving_average, df).result()
        df = executor.submit(detect_anomalies, df, seasonal_stats).result()
    execution_time = time.time() - start_time
    return df, seasonal_stats, execution_time
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_current_temperature(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['main']['temp']
    else:
        return None
with open("app.py", "w") as f:
    f.write("""import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import os

st.title("Анализ температурных данных и мониторинг текущей температуры")

uploaded_file = st.file_uploader("Загрузите CSV-файл с историческими данными", type=["csv"])
API_KEY = st.text_input("Введите API-ключ OpenWeatherMap", type="password")

if API_KEY:
    st.session_state["api_key"] = API_KEY
    st.success("API-ключ успешно введен!")
else:
    st.warning("Введите API-ключ для получения данных о текущей температуре.")

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['timestamp'])
    st.write("### Загруженные данные")
    st.write(df.head())

    cities = df['city'].unique()
    selected_city = st.selectbox("Выберите город", cities)

    city_data = df[df['city'] == selected_city]

    fig = px.line(city_data, x='timestamp', y='temperature', title=f'Температура в городе {selected_city} с аномалиями')
    st.plotly_chart(fig)

    season_fig = px.box(df[df['city'] == selected_city], x='season', y='temperature', title=f'Сезонные профили температуры в городе {selected_city}')
    st.plotly_chart(season_fig)

    if "api_key" in st.session_state:
        if st.button("Получить текущую температуру"):
            url = f"https://api.openweathermap.org/data/2.5/weather?q={selected_city}&appid={st.session_state['api_key']}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                current_temp = response.json()['main']['temp']
                st.write(f"### Текущая температура в городе {selected_city}: {current_temp}°C")
            else:
                st.error("Ошибка при получении данных. Проверьте API-ключ.")
    else:
        st.warning("Введите API-ключ, чтобы получить данные о текущей температуре.")""")
port = 8501
public_url = ngrok.connect(port).public_url
print(f"Streamlit-приложение доступно по ссылке: {public_url}")

subprocess.Popen(["streamlit", "run", "app.py", "--server.port", str(port)])