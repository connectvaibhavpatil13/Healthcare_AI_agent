from fastapi import APIRouter
from sqlalchemy import text
from app.services.sql_service import execute_query
from app.database.connection import engine

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/patient-count")
def patient_count():
    query = text("SELECT COUNT(*) AS total_patients FROM patients")

    with engine.connect() as connection:
        result = connection.execute(query).mappings().first()

    return {
        "metric": "Total Patients",
        "value": result["total_patients"]
    }

@router.get("/department-patient-volume")
def department_patient_volume():

    query = text("""
        SELECT
            d.Department_Name,
            COUNT(a.Appointment_ID) AS patient_visits
        FROM appointments a
        JOIN doctors doc
            ON a.Doctor_ID = doc.Doctor_ID
        JOIN departments d
            ON doc.Department_ID = d.Department_ID
        GROUP BY d.Department_ID, d.Department_Name
        ORDER BY patient_visits DESC
    """)

    with engine.connect() as connection:
        results = connection.execute(query).mappings().all()

    return {
        "data": results
    }

@router.get("/monthly-appointments")
def monthly_appointments():

    query = text("""
        SELECT
            DATE_FORMAT(Appointment_Date, '%Y-%m') AS month,
            COUNT(*) AS total_appointments
        FROM appointments
        GROUP BY DATE_FORMAT(Appointment_Date, '%Y-%m')
        ORDER BY month
    """)

    with engine.connect() as connection:
        results = connection.execute(query).mappings().all()

    return {
        "data": results
    }

@router.get("/appointment-status")
def appointment_status():

    query = text("""
        SELECT
            Appointment_Status,
            COUNT(*) AS total
        FROM appointments
        GROUP BY Appointment_Status
        ORDER BY total DESC
    """)

    with engine.connect() as connection:
        results = connection.execute(query).mappings().all()

    return {
        "data": results
    }

@router.get("/revenue")
def revenue():

    query = text("""
        SELECT
            SUM(Final_Amount) AS total_revenue,
            AVG(Final_Amount) AS average_bill,
            COUNT(Bill_ID) AS total_bills
        FROM billing
    """)

    with engine.connect() as connection:
        result = connection.execute(query).mappings().first()

    return {
        "total_revenue": float(result["total_revenue"] or 0),
        "average_bill": round(float(result["average_bill"] or 0), 2),
        "total_bills": result["total_bills"]
    }

@router.get("/test-query")
def test_query():

    query = """
        SELECT
            COUNT(*) AS total_patients
        FROM patients
    """

    result = execute_query(query)

    return {
        "data": result
    }
