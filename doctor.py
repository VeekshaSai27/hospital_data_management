import streamlit as st
import sqlite3

def run():
    st.header("Doctor Management")

    conn = sqlite3.connect("data/hospital.db")
    c = conn.cursor()

    # Form to add a new doctor
    with st.form("Add Doctor"):
        name = st.text_input("Doctor Name")
        specialty = st.text_input("Specialty")
        availability = st.text_input("Availability (e.g., Mon-Fri 10am-5pm)")
        performance = st.slider("Performance Score", 1, 10)

        if st.form_submit_button("Add Doctor"):
            c.execute('''INSERT INTO doctors (name, specialty, availability, performance_score)
                         VALUES (?, ?, ?, ?)''',
                      (name, specialty, availability, performance))
            conn.commit()
            st.success("Doctor added successfully!")

    # View doctors
    st.subheader("Registered Doctors")
    doctors = c.execute("SELECT * FROM doctors").fetchall()
    st.dataframe(doctors)

    conn.close()
