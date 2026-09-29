from langchain.agents import create_agent

from app.agents.llm import llm
from app.agents.tools import (
    get_department_patient_volume,
    get_total_patient_count,
    get_appointment_status,
    get_monthly_appointments,
    get_decision_recommendation,
    get_average_waiting_time,
    get_department_average_waiting_time
)


tools = [
    get_department_patient_volume,
    get_total_patient_count,
    get_appointment_status,
    get_monthly_appointments,
    get_decision_recommendation,
    get_average_waiting_time,
    get_department_average_waiting_time
]

agent = create_agent(
    model=llm,
    tools=tools
)