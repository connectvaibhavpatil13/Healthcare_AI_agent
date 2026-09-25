from app.services.sql_service import execute_query


def get_department_patient_volume():
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