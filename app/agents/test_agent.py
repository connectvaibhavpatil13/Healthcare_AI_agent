from app.agents.agent import agent


questions = [
    "How many patients are registered in the hospital?",
    "Which department has the highest patient volume?"
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