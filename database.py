import sqlite3

def init_db():
    conn = sqlite3.connect("data/hospital.db")
    cursor = conn.cursor()

    # Patient Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, age INTEGER, gender TEXT,
            contact TEXT, emergency_contact TEXT,
            history TEXT, status TEXT
        )
    ''')

    # Doctor Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, specialty TEXT,
            availability TEXT, performance_score INTEGER
        )
    ''')

    # Appointments Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor_id INTEGER,
            date TEXT,
            status TEXT
        )
    ''')

    # Billing Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS billing (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            amount REAL,
            service TEXT,
            paid INTEGER
        )
    ''')

    conn.commit()
    conn.close()
