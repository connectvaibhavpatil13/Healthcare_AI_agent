from langchain_core.tools import tool
from app.services.sql_service import execute_query
from app.services.decision_service import generate_recommendation


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

@tool
def get_appointment_status():
    """
    Get the number of appointments for each appointment status.
    Use this when the user asks about appointment status,
    such as completed, cancelled, pending, or scheduled appointments.
    """

    query = """
        SELECT
            Appointment_Status,
            COUNT(*) AS total
        FROM appointments
        GROUP BY Appointment_Status
        ORDER BY total DESC
    """

    return execute_query(query)
@tool
def get_monthly_appointments():
    """
    Get the total number of appointments for each month.
    Use this when the user asks about monthly appointment trends.
    """

    query = """
        SELECT
            DATE_FORMAT(Appointment_Date, '%Y-%m') AS month,
            COUNT(*) AS total_appointments
        FROM appointments
        GROUP BY DATE_FORMAT(Appointment_Date, '%Y-%m')
        ORDER BY month
    """

    return execute_query(query)

@tool
def get_decision_recommendation(question: str, analysis: str):
    """
    Generate a business insight and recommendation based on an analytical result.
    Use this when the user asks for recommendations or decision support.
    """

    return generate_recommendation(question, analysis)

@tool
def get_average_waiting_time():
    """
    Get the average appointment waiting time.
    Use this when evaluating operational pressure or patient waiting experience.
    """

    query = """
        SELECT
            AVG(Waiting_Time_Min) AS average_waiting_time_minutes
        FROM appointments
        WHERE Waiting_Time_Min IS NOT NULL
    """

    return execute_query(query)

@tool
def get_department_average_waiting_time():
    """
    Get the average appointment waiting time for each hospital department.
    Use this when comparing department-level patient volume with waiting time.
    """
    query = """
        SELECT
            d.Department_Name,
            AVG(a.Waiting_Time_Min) AS average_waiting_time_minutes
        FROM appointments a
        JOIN doctors doc
            ON a.Doctor_ID = doc.Doctor_ID
        JOIN departments d
            ON doc.Department_ID = d.Department_ID
        WHERE a.Waiting_Time_Min IS NOT NULL
        GROUP BY d.Department_ID, d.Department_Name
        ORDER BY average_waiting_time_minutes DESC
    """
    return execute_query(query)