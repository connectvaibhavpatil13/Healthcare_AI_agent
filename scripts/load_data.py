import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

print("Connected to MySQL successfully!")

tables = {
    "departments": "departments.csv",
    "doctors": "doctors.csv",
    "patients": "patients.csv",
    "appointments": "appointments.csv",
    "admissions": "admissions.csv",
    "treatments": "treatments.csv",
    "billing": "billing.csv",
    "patient_feedback": "patient_feedback.csv"
}

for table_name, filename in tables.items():
    file_path = f"data/raw/{filename}"

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        con=engine,
        if_exists="append",
        index=False
    )

    print(f"{table_name}: {len(df)} records loaded")
