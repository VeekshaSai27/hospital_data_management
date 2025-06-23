import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

def run():
    st.header("Appointment Scheduling")

    conn = sqlite3.connect("data/hospital.db")
    c = conn.cursor()

    # Fetch patient and doctor data
    patients = c.execute("SELECT id, name FROM patients").fetchall()
    doctors = c.execute("SELECT id, name FROM doctors").fetchall()

    with st.form("Schedule Appointment"):
        patient = st.selectbox("Select Patient", patients, format_func=lambda x: f"{x[1]} (ID: {x[0]})")
        doctor = st.selectbox("Select Doctor", doctors, format_func=lambda x: f"{x[1]} (ID: {x[0]})")
        app_date = st.date_input("Appointment Date", date.today())
        status = st.selectbox("Status", ["Scheduled", "Completed", "Cancelled"])

        if st.form_submit_button("Add to record"):
            c.execute('''INSERT INTO appointments (patient_id, doctor_id, date, status)
                         VALUES (?, ?, ?, ?)''',
                      (patient[0], doctor[0], str(app_date), status))
            conn.commit()
            st.success("Appointment Scheduled!")

    # View all appointments
    st.subheader("All Appointments")
    df = pd.read_sql_query('''
        SELECT a.id, p.name AS patient, d.name AS doctor, a.date, a.status
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
    ''', conn)
    st.dataframe(df)

    conn.close()
