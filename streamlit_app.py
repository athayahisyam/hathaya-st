# Import relevant libraries

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import statsmodels.api as sm

st.set_page_config(layout="wide")

# Load dataset

df = pd.read_csv("cm_eu.csv")

# Perbaikan dan pembersihan data

df.interpolate(inplace = True)
df['date'] = df['date'].str.replace('/', '-')
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# Judul dan penjelasan aplikasi
st.title('Analisis Data Karbon Monitor Eropa')
st.write('Selamat datang di aplikasi analisis data Karbon Monitor Eropa.')
st.write('Dataset yang digunakan diambil dari makalah yang ditulis oleh Piyu Ke, Zhu Deng, Biqing Zhu, et al. pada tahun 2023 dengan judul "Carbon Monitor Europe near-real-time daily CO2 emissions for 27 EU countries and the United Kingdom". Dataset ini berisi data emisi CO2 harian dalam waktu nyata untuk 27 negara anggota UE dan Britania Raya.')

# Tampilkan informasi tentang dataset
st.header('Informasi Dataset')
st.write('Dataset berisi informasi emisi karbon dioksida (CO2) harian untuk 27 negara anggota UE dan Britania Raya. Data ini meliputi tahun 2019 hingga 2022 dan terdiri dari beberapa sektor, termasuk daya, penerbangan domestik, penerbangan internasional, industri, transportasi darat, dan sektor rumah tangga. Setiap baris dataset mencakup atribut seperti negara, tanggal, sektor, nilai emisi, dan timestamp.')
st.write('Dataset ini dapat digunakan untuk analisis tren emisi CO2, pembandingan antar negara dan sektor, serta pemodelan dan prediksi emisi di masa depan.')

# Analisis Data Eksploratori
st.header('Analisis Data Eksploratori')
st.write('Sebelum melakukan visualisasi data, kita dapat melakukan beberapa analisis data eksploratori untuk memahami struktur dataset.')

# Tampilkan beberapa baris pertama dataset
st.subheader('Tampilan beberapa baris pertama dataset')
st.dataframe(df.head())

# Informasi umum tentang dataset
st.subheader('Informasi umum tentang dataset')
st.write('Jumlah total data:', len(df))
st.write('Kolom dalam dataset:', df.columns.tolist())
st.write('Deskripsi statistik dataset:')
st.write(df.describe())

# Visualisasi Data
st.header('Visualisasi Data')

# Tambahkan visualisasi data di sini (contoh: bar plot, line plot, scatter plot, dll.)
# Misalnya, untuk menampilkan grafik bar emisi per tahun:
emisi_per_tahun = df.groupby(df['date'].dt.year)['value'].sum()
st.subheader('Grafik Total Emisi CO2 per Tahun')
st.bar_chart(emisi_per_tahun)

# Menambahkan visualisasi tambahan sesuai kebutuhan

# Akhir dari kode Streamlit
