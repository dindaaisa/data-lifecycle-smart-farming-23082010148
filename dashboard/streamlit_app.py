import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(page_title="Smart Farming Dashboard", layout="wide")

st.title("🌱 Smart Farming Sensor Dashboard")
st.markdown("Monitoring sensor IoT untuk analisis pertanian cerdas")

# =============================
# LOAD DATA
# =============================
data_path = os.path.join("outputs", "smart_farming_cleaned.csv")
df = pd.read_csv(data_path)

df["timestamp"] = pd.to_datetime(df["timestamp"])

# =============================
# DATA QUALITY SCORE
# =============================
st.subheader("📊 Data Quality Monitoring")

total_cells = df.size
missing_cells = df.isna().sum().sum()
non_null_cells = total_cells - missing_cells

accuracy = 1 - (missing_cells / total_cells)
completeness = non_null_cells / total_cells

last_30_days = datetime.now() - timedelta(days=30)
recent_data = df[df["timestamp"] >= last_30_days]

timeliness = len(recent_data) / len(df)

col1, col2, col3 = st.columns(3)

col1.metric("Accuracy", f"{accuracy:.2f}")
col2.metric("Completeness", f"{completeness:.2f}")
col3.metric("Timeliness (30 days)", f"{timeliness:.2f}")

st.divider()

# =============================
# SIDEBAR FILTER
# =============================
st.sidebar.header("Filter Data")

region = st.sidebar.selectbox(
    "Select Region",
    df["region"].unique()
)

crop = st.sidebar.selectbox(
    "Select Crop Type",
    df["crop_type"].unique()
)

filtered_df = df[
    (df["region"] == region) &
    (df["crop_type"] == crop)
]

# =============================
# KPI METRICS
# =============================
st.subheader("📈 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Yield",
    f"{round(filtered_df['yield_kg_per_hectare'].mean(),2)} kg"
)

col2.metric(
    "Average Soil Moisture",
    f"{round(filtered_df['soil_moisture_%'].mean(),2)} %"
)

col3.metric(
    "Average Temperature",
    f"{round(filtered_df['temperature_C'].mean(),2)} °C"
)

st.divider()

# =============================
# DATASET PREVIEW
# =============================
st.subheader("📄 Dataset Preview")

st.dataframe(filtered_df.head())

st.divider()

# =============================
# TIME SERIES SENSOR
# =============================
st.subheader("📈 Soil Moisture Trend")

df_sorted = filtered_df.sort_values("timestamp")

fig1, ax1 = plt.subplots(figsize=(10,4))

sns.lineplot(
    x="timestamp",
    y="soil_moisture_%",
    data=df_sorted,
    color="green",
    ax=ax1
)

plt.xticks(rotation=45)

st.pyplot(fig1)

st.divider()

# =============================
# GAUGE METER
# =============================
st.subheader("🌡 Soil Moisture Gauge")

current_moisture = filtered_df["soil_moisture_%"].mean()

fig_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=current_moisture,
    title={'text': "Soil Moisture (%)"},
    gauge={
        'axis': {'range': [0,50]},
        'steps': [
            {'range': [0,20], 'color': "red"},
            {'range': [20,35], 'color': "yellow"},
            {'range': [35,50], 'color': "green"}
        ],
        'bar': {'color': "darkblue"}
    }
))

st.plotly_chart(fig_gauge, use_container_width=True)

st.divider()

# =============================
# SENSOR CORRELATION HEATMAP
# =============================
st.subheader("🔥 Sensor Correlation Heatmap")

fig2, ax2 = plt.subplots(figsize=(10,6))

corr = filtered_df.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    ax=ax2
)

st.pyplot(fig2)

st.divider()

# =============================
# ALERT SYSTEM
# =============================
st.subheader("🚨 Soil Moisture Alert System")

threshold = 20

fig3, ax3 = plt.subplots(figsize=(8,5))

sns.scatterplot(
    x="soil_moisture_%",
    y="yield_kg_per_hectare",
    hue=(filtered_df["soil_moisture_%"] < threshold),
    palette={True:"red", False:"green"},
    data=filtered_df,
    ax=ax3
)

ax3.axvline(threshold, linestyle="--")

st.pyplot(fig3)

st.divider()

# =============================
# FARM LOCATION MAP
# =============================
st.subheader("🗺 Farm Locations")

st.map(filtered_df[["latitude","longitude"]])