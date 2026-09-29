from app.agents.agent import agent



questions = [
    "Which department has the highest patient volume, how does its waiting time compare with other departments, and what should management investigate before making a recommendation?"
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

