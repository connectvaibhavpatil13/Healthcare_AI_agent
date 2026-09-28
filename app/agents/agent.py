from langchain.agents import create_agent

from app.agents.llm import llm
from app.agents.tools import (
    get_department_patient_volume,
    get_total_patient_count,
    get_appointment_status,
    get_monthly_appointments
)


tools = [
    get_department_patient_volume,
    get_total_patient_count,
    get_appointment_status,
    get_monthly_appointments
]

agent = create_agent(
    model=llm,
    tools=tools
)