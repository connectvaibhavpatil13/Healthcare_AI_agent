from app.agents.agent import agent


questions = [
    "How many appointments were there each month?"
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