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

1. Observed findings:
   - State only facts directly supported by the analytical result.
   - Include the relevant numbers.

2. Interpretation:
   - Explain what the findings may indicate.
   - Clearly label interpretations as interpretations.
   - Do not present assumptions as facts.

3. Recommendations:
   - Give one or two practical actions or investigations.
   - Recommendations must be justified by the available evidence.
   - If the available data is insufficient for a strong recommendation, say what additional data should be investigated.

Do not invent facts, causes, trends, or operational conditions that are not present in the analytical result.
"""

    response = llm.invoke(prompt)

    return response.content