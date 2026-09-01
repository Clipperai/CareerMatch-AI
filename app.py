from flask import Flask, request
from calculate_score import calculate_match
from database import save_analysis
from ai_analysis import generate_recommendation



app = Flask(__name__)

@app.route("/")
def home():
    return "hello"

@app.route("/analyze", methods= ['POST'])
def analyze():

    data = request.json

    resume_skills = set(data["resume_skills"])
    job_skills = set(data["job_skills"])

    result = calculate_match(resume_skills, job_skills)
    matched, missing, percentage, points = result

    save_analysis(
    ", ".join(resume_skills),
    ", ".join(job_skills),
    ", ".join(matched),
    ", ".join(missing),
    points
)

    response = {

            "matched": list(matched),
            "missing": list(missing),
            "percentage": percentage,
            "points": points,
            "AI Recommendation": generate_recommendation(matched, missing)
            
        }

    return response

# RUN FLASK APP

if __name__ == "__main__":
    app.run(debug= True)