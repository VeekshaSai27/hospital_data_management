import streamlit as st
import sqlite3
import pandas as pd

def run():
    st.header("Billing System")

    conn = sqlite3.connect("data/hospital.db")
    c = conn.cursor()

    patients = c.execute("SELECT id, name FROM patients").fetchall()

    with st.form("Add Billing Record"):
        patient = st.selectbox("Select Patient", patients, format_func=lambda x: f"{x[1]} (ID: {x[0]})")
        service = st.text_input("Service Provided (e.g., Consultation, Surgery)")
        amount = st.number_input("Amount (₹)", min_value=0.0)
        paid = st.selectbox("Payment Status", ["Unpaid", "Paid"])

        if st.form_submit_button("Generate Bill"):
            c.execute('''
                INSERT INTO billing (patient_id, amount, service, paid)
                VALUES (?, ?, ?, ?)
            ''', (patient[0], amount, service, 1 if paid == "Paid" else 0))
            conn.commit()
            st.success("Bill Added!")

    # Display all bills
    st.subheader("All Billing Records")
    df = pd.read_sql_query('''
        SELECT b.id, p.name AS patient, b.service, b.amount, 
               CASE WHEN b.paid = 1 THEN 'Paid' ELSE 'Unpaid' END AS payment_status
        FROM billing b
        JOIN patients p ON b.patient_id = p.id
    ''', conn)
    st.dataframe(df)

    conn.close()
