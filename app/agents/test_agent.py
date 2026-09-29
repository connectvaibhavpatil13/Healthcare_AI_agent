from app.agents.agent import agent


questions = [
    "Which department has the highest patient volume, and what should the hospital do about it?"
]

for question in questions:
    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })

    print("\nQuestion:", question)
    print("Answer:", result["messages"][-1].content)