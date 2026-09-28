from langchain_core.tools import tool

from app.services.sql_service import execute_query

@tool
def get_department_patient_volume():
    """
    Get patient visit volume for each hospital department.
    Use this when the user asks about department-wise patient volume.
    """

    query = """
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
    """

    return execute_query(query)

@tool
def get_total_patient_count():
    """
    Get the total number of patients registered in the hospital.
    Use this when the user asks how many patients there are.
    """

    query = """
        SELECT COUNT(*) AS total_patients
        FROM patients
    """

    return execute_query(query)