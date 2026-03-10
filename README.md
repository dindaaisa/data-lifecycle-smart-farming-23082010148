🌱 Smart Farming Sensor Data Analysis & Dashboard
📌 Project Overview

Project ini bertujuan untuk menganalisis data sensor pertanian berbasis Smart Farming menggunakan pendekatan Data Lifecycle Management. Dataset yang digunakan berasal dari platform Kaggle dan berisi berbagai informasi sensor lingkungan yang mempengaruhi hasil panen tanaman.

Melalui proyek ini dilakukan proses:

Data Acquisition

Data Processing

Exploratory Data Analysis (EDA)

Data Visualization

Dashboard Development

Data Quality Monitoring

Hasil akhir dari proyek ini adalah dashboard interaktif menggunakan Streamlit yang memungkinkan pengguna memonitor kondisi pertanian secara visual.

📊 Dataset Information

Dataset yang digunakan:

Smart Farming Sensor Data for Yield Prediction

Dataset ini mensimulasikan operasi pertanian modern yang menggunakan sensor IoT untuk memantau kondisi lingkungan.

Jumlah Data

500 farms

Beberapa fitur utama dalam dataset:
Feature	Description
soil_moisture_%	Persentase kelembaban tanah
soil_pH	Tingkat keasaman tanah
temperature_C	Suhu rata-rata
rainfall_mm	Curah hujan
humidity_%	Kelembaban udara
sunlight_hours	Lama penyinaran matahari
NDVI_index	Indeks vegetasi tanaman
yield_kg_per_hectare	Hasil panen per hektar

Dataset juga menyertakan informasi tambahan seperti:

region

crop type

irrigation type

fertilizer type

sensor id

timestamp

latitude & longitude

🔄 Data Lifecycle Implementation

Project ini mengimplementasikan beberapa tahapan dalam Data Lifecycle Management.

1️⃣ Data Acquisition

Dataset diambil dari platform Kaggle menggunakan API.

2️⃣ Data Processing

Tahap preprocessing meliputi:

Data inspection

Handling missing values

Data type conversion

Data cleaning

Dataset hasil pembersihan disimpan sebagai:

smart_farming_cleaned.csv
3️⃣ Exploratory Data Analysis (EDA)

Beberapa analisis eksploratif dilakukan untuk memahami karakteristik data, seperti:

Distribution of crop yield

Yield comparison by region

Soil moisture vs crop yield

Rainfall vs yield

NDVI vs yield

Correlation analysis

📈 Dashboard Visualization

Dashboard interaktif dibangun menggunakan Streamlit untuk memvisualisasikan data sensor pertanian.

Beberapa fitur utama dashboard:

📊 Data Quality Monitoring

Menampilkan metrik kualitas data seperti:

Accuracy

Completeness

Timeliness

📈 Time Series Monitoring

Menampilkan perubahan soil moisture terhadap waktu untuk memantau kondisi tanah.

🌡 Soil Moisture Gauge

Gauge chart untuk memvisualisasikan tingkat kelembaban tanah secara intuitif.

🔥 Sensor Correlation Heatmap

Menampilkan korelasi antar variabel sensor seperti:

temperature

rainfall

humidity

NDVI

crop yield

🚨 Alert System

Sistem peringatan untuk mendeteksi kondisi tanah yang terlalu kering berdasarkan threshold tertentu.

🗺 Farm Location Map

Visualisasi lokasi farm berdasarkan koordinat geografis.

🖥 Dashboard Preview

(Tambahkan screenshot dashboard di sini)

Contoh:

dashboard_screenshot.png
⚙️ Technologies Used

Beberapa teknologi yang digunakan dalam proyek ini:

Python

Pandas

Matplotlib

Seaborn

Plotly

Streamlit

Google Colab

Kaggle API

GitHub

📂 Project Structure
data-lifecycle-smart-farming
│
├── notebooks
│   └── smart_farming_analysis.ipynb
│
├── dashboard
│   └── streamlit_app.py
│
├── outputs
│   └── smart_farming_cleaned.csv
│
├── reports
│   └── analysis_report.md
│
├── requirements.txt
└── README.md
🚀 How to Run the Dashboard

Clone repository

git clone https://github.com/username/repository-name.git

Install dependencies

pip install -r requirements.txt

Run Streamlit

streamlit run dashboard/streamlit_app.py
📌 Conclusion

Proyek ini menunjukkan bagaimana data sensor pertanian dapat dianalisis dan divisualisasikan menggunakan dashboard interaktif. Dengan memanfaatkan teknologi data analytics, sistem Smart Farming dapat membantu meningkatkan efisiensi dan produktivitas pertanian.

👨‍💻 Author

Project ini dikembangkan sebagai bagian dari tugas Data Lifecycle Management.

Nama: Dinda Aisa Selvira
NPM: 23082010148