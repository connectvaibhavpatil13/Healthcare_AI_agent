from langchain.agents import create_agent

from app.agents.llm import llm
from app.agents.tools import (
    get_department_patient_volume,
    get_total_patient_count
)


tools = [
    get_department_patient_volume,
    get_total_patient_count
]

agent = create_agent(
    model=llm,
    tools=tools
)