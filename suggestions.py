from openai import OpenAI
from config import API_KEY, MODEL

client = OpenAI(api_key=API_KEY)

def get_suggestions(resume_text, job_desc):
    prompt = f"""
    Analyze this resume and give:
    - Strengths
    - Weaknesses
    - Missing skills
    - Improvement tips

    Resume:
    {resume_text}

    Job Description:
    {job_desc}
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content