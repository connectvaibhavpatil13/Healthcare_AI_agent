from app.agents.llm import llm
from app.agents.tools import get_department_patient_volume


tools = [get_department_patient_volume]
llm_with_tools = llm.bind_tools(tools)

user_question = "Which department has the highest patient volume?"

# Step 1: Ask the LLM what tool it needs
response = llm_with_tools.invoke(user_question)

print("First AI response:")
print(response)

# Step 2: Execute the tool requested by the LLM
tool_call = response.tool_calls[0]

tool_result = get_department_patient_volume.invoke(
    tool_call["args"]
)

print("\nTool result:")
print(tool_result)

# Step 3: Send the tool result back to the LLM
final_response = llm_with_tools.invoke([
    ("user", user_question),
    response,
    {
        "role": "tool",
        "content": str(tool_result),
        "tool_call_id": tool_call["id"],
    },
])

print("\nFinal AI response:")
print(final_response.content)