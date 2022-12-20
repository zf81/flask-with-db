import sqlite3
import pandas as pd

def get_db_connection():
    conn = sqlite3.connect('/Users/fizzahzaidi/Documents/development/python_projects/flask-with-db/patients.db')
    conn.row_factory = sqlite3.Row
    return conn

db = get_db_connection()
patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
patientListSql

df = pd.DataFrame(patientListSql)
df

# rename the columns
df.columns = ['mrn', 'firstname', 'lastname', 'dob', 'ssn', 'streetadress', 'zipcode', 'city']
df

