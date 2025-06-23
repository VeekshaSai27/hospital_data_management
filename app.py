import streamlit as st
from database import init_db
import patient, doctor, appointment, billing, reports

st.set_page_config(page_title="Hospital Management", layout="wide")

def main():
    init_db()
    st.sidebar.title("Hospital Management System")
    choice = st.sidebar.radio("Go to", ["Patients", "Doctors", "Appointments", "Billing", "Reports"])

    if choice == "Patients":
        patient.run()
    elif choice == "Doctors":
        doctor.run()
    elif choice == "Appointments":
        appointment.run()
    elif choice == "Billing":
        billing.run()
    elif choice == "Reports":
        reports.run()


if __name__ == "__main__":
    main()
