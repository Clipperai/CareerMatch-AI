import os
from groq import Groq
from dotenv import load_dotenv

# GRABBING API KEY FROM .env FILE

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# GROQ FUNCTIONALITY

client = Groq(api_key=GROQ_API_KEY)

MODEL = "openai/gpt-oss-safeguard-20b"



# RECOMMMENDATION FUNCTION

def generate_recommendation(matched, missing):
    prompt = f""" 
    You are an expert ATS and career coach who designs practical, progressive learning paths.

Matched skills:
{matched}

Missing skills:
{missing}

User's current project:
Job Match Analyzer built with Python, Streamlit, Flask, SQLite, and AI API integration.

Your task:
Analyze the skill gap and recommend the best next project/task for the user.

Rules:

* Focus ONLY on the missing skills.
* First recommend a project/task that matches the user's CURRENT skill level.
* Prefer improving or extending the user's existing Job Match Analyzer when possible.
* Then briefly explain how the same project can gradually increase in difficulty.
* Progression must follow:
  Level 1 → Beginner/current level
  Level 2 → Intermediate upgrade
  Level 3 → More advanced upgrade
* Do NOT jump directly to advanced technologies.
* Use the 80/20 principle to prioritize the highest-value fundamentals.
* Use SMART goals for the immediate Level 1 task.
* Keep each level practical and project-based.
* Maximum 5 short bullet points.
* Do NOT create a huge roadmap.
* Do NOT recommend technologies that are unrelated to the missing skills.

Response format:
🎯 Priority Skill: [one missing skill]

🚀 Level 1 — Current Level:
[One practical project/task the user can realistically build now]

📈 Level 2 — Upgrade:
[One meaningful upgrade to the same project]

🔥 Level 3 — Advanced Upgrade:
[One more challenging upgrade]

SMART Goal:
[One measurable short-term goal for Level 1]


"""

    response = client.chat.completions.create(
        model = MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt

            }
        ]

    )

    output= response.choices[0].message.content

    return output

    