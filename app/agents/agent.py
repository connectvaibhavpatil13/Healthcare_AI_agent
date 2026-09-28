from langchain.agents import create_agent

from app.agents.llm import llm
from app.agents.tools import get_department_patient_volume


tools = [
    get_department_patient_volume
]

agent = create_agent(
    model=llm,
    tools=tools
)