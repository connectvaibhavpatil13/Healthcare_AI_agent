from app.agents.llm import llm


def generate_recommendation(question: str, analysis: str) -> str:
    """
    Generate a decision-support recommendation using the LLM.
    """

    prompt = f"""
You are a healthcare business decision-support assistant.

User question:
{question}

Analytical result:
{analysis}

Based only on the analytical result, provide:
1. A short business insight.
2. One or two practical recommendations.

Do not invent facts that are not present in the analytical result.
Clearly distinguish the observed result from the recommendation.
"""

    response = llm.invoke(prompt)

    return response.content