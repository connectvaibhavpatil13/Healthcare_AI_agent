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