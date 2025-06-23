import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

def run():
    st.header("Hospital Reports")
    conn = sqlite3.connect("data/hospital.db")

    df = pd.read_sql_query("SELECT * FROM appointments", conn)
    st.subheader("Appointments Overview")
    st.dataframe(df)

    # Plot trends
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
        daily_count = df.groupby('date').size().reset_index(name='appointments')
        fig = px.line(daily_count, x='date', y='appointments', title='Daily Appointments')
        st.plotly_chart(fig)

    conn.close()
