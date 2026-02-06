import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Analyseur de Précipitations IA",
    layout="wide",
)

# ---------------- DATA ----------------
sample_data = pd.DataFrame([
    {"date": "2021-01-01", "observed": 45.2, "predicted": 42.8, "temperature": 28.5},
    {"date": "2021-01-02", "observed": 52.3, "predicted": 48.9, "temperature": 29.1},
    {"date": "2021-01-03", "observed": 38.7, "predicted": 41.2, "temperature": 27.8},
    {"date": "2021-01-04", "observed": 61.5, "predicted": 58.3, "temperature": 30.2},
    {"date": "2021-01-05", "observed": 55.8, "predicted": 54.1, "temperature": 29.5},
    {"date": "2021-01-06", "observed": 48.2, "predicted": 46.7, "temperature": 28.9},
    {"date": "2021-01-07", "observed": 72.4, "predicted": 70.5, "temperature": 31.2},
])

future_data = pd.DataFrame([
    {"date": "2021-01-08", "predicted": 65.3, "temperature": 30.8},
    {"date": "2021-01-09", "predicted": 58.7, "temperature": 29.4},
    {"date": "2021-01-10", "predicted": 71.2, "temperature": 31.5},
])

# ---------------- HEADER ----------------
st.title("🌧 Analyseur de Précipitations IA")
st.subheader("Prévision basée sur le modèle PrecipFormer")

# ---------------- METRICS ----------------
c1, c2, c3, c4 = st.columns(4)

c1.metric("MSE", "0.0234")
c2.metric("RMSE", "0.153 mm")
c3.metric("MAE", "0.128 mm")
c4.metric("R² Score", "0.892")

st.divider()

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(["📊 Vue d'ensemble", "🔮 Prévisions", "📈 Analyse"])

# ---------------- TAB 1 ----------------
with tab1:
    st.subheader("Observé vs Prédit")

    fig1 = px.line(
        sample_data,
        x="date",
        y=["observed", "predicted"],
        markers=True,
        labels={"value": "mm/jour", "date": "Date"},
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Précipitations moyennes")

    fig2 = px.bar(
        sample_data,
        x="date",
        y="observed",
        labels={"observed": "mm/jour"},
    )
    st.plotly_chart(fig2, use_container_width=True)

# ---------------- TAB 2 ----------------
with tab2:
    st.subheader("Prévisions à venir")

    fig3 = px.line(
        future_data,
        x="date",
        y="predicted",
        markers=True,
        labels={"predicted": "mm/jour"},
    )
    st.plotly_chart(fig3, use_container_width=True)

    cols = st.columns(3)

    for i, row in future_data.iterrows():
        with cols[i]:
            st.info(f"""
            📅 **{row.date}**  
            🌧 **{row.predicted} mm**  
            🌡 **{row.temperature} °C**
            """)

# ---------------- TAB 3 ----------------
with tab3:
    st.subheader("Modèle PrecipFormer")

    st.markdown("""
    ### Architecture
    - Embedding spatial (CNN)
    - Attention temporelle
    - Reconstruction spatiale

    ### Données
    - TCRW  
    - CAPE  
    - Vent  
    - Température  
    - Humidité  

    ### Performance
    Entraîné sur IMERG (2010–2020) avec séparation 80/20.
    """)

# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2026 Analyseur de Précipitations IA")
