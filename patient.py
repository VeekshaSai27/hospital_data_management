import streamlit as st
import sqlite3

def run():
    conn = sqlite3.connect("data/hospital.db")
    c = conn.cursor()

    st.header("Patient Management")

    with st.form("Add Patient"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        contact = st.text_input("Contact Number")
        emergency = st.text_input("Emergency Contact")
        status = st.selectbox("Status", ["Inpatient", "Outpatient"])
        history = st.text_area("Medical History")

        if st.form_submit_button("Register"):
            c.execute('''INSERT INTO patients (name, age, gender, contact, emergency_contact, history, status)
                         VALUES (?, ?, ?, ?, ?, ?, ?)''', (name, age, gender, contact, emergency, history, status))
            conn.commit()
            st.success("Patient Registered!")

    # View patients
    st.subheader("Registered Patients")
    patients = c.execute("SELECT * FROM patients").fetchall()
    st.dataframe(patients)

    conn.close()
