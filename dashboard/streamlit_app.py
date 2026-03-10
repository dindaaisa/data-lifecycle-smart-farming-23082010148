import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(
    page_title="Smart Farming Dashboard",
    layout="wide"
)

st.title("🌱 Smart Farming Sensor Dashboard")
st.markdown("Dashboard monitoring sensor IoT untuk analisis pertanian cerdas")

# ================================
# LOAD DATA
# ================================
df = pd.read_csv("../outputs/smart_farming_cleaned.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])

# ================================
# SIDEBAR FILTER
# ================================
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

# ================================
# DATA QUALITY MONITORING
# ================================
st.subheader("📊 Data Quality Monitoring")

col1, col2, col3 = st.columns(3)

accuracy = 1 - (filtered_df.isnull().sum().sum() / filtered_df.size)
completeness = filtered_df.notnull().sum().sum() / filtered_df.size

recent_data = filtered_df[
    filtered_df["timestamp"] >
    filtered_df["timestamp"].max() - pd.Timedelta(days=30)
]

timeliness = len(recent_data) / len(filtered_df)

col1.metric("Accuracy", round(accuracy, 2))
col2.metric("Completeness", round(completeness, 2))
col3.metric("Timeliness (30 days)", round(timeliness, 2))

st.divider()

# ================================
# DATA PREVIEW
# ================================
st.subheader("📄 Dataset Preview")
st.dataframe(filtered_df.head())

st.divider()

# ================================
# TIME SERIES SENSOR
# ================================
st.subheader("📈 Soil Moisture Trend (Time Series)")

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

# ================================
# GAUGE METER
# ================================
st.subheader("🌡 Current Soil Moisture Gauge")

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

# ================================
# HEATMAP KORELASI SENSOR
# ================================
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

# ================================
# ALERT SYSTEM
# ================================
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

# ================================
# MAP FARM LOCATION
# ================================
st.subheader("🗺 Farm Locations")

st.map(filtered_df[["latitude","longitude"]])