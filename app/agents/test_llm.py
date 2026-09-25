from app.agents.llm import llm

response = llm.invoke(
    "What are 5 important business analytics metrics "
    "a hospital manager should monitor?"
)

print(response.content)