from app.agents.agent import agent


result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Which department has the highest patient volume?"
        }
    ]
})


print(result["messages"][-1].content)