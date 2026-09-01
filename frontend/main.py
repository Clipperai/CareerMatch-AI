import streamlit as st
import requests

# STREAMLIT UI

st.set_page_config(
    page_title= "Job Match Analyzer", 
    page_icon= "📜")

st.title("Job Match Analyzer")


resume_skills = st.text_input("Enter Resume Skills here:")
job_skills = st.text_input("Enter Job skills here:")


resume_skills = set(resume_skills.split(","))
job_skills = set(job_skills.split(","))

if resume_skills and job_skills:    
    analyze = st.button("Analyze")

    if analyze:

        response = requests.post(
            "http://127.0.0.1:5000/analyze",
            json = {
                "resume_skills": list(resume_skills),
                "job_skills": list(job_skills)
            }
        )

        result = response.json()

        st.divider()

        st.metric("Percentage" , result["percentage"])

        st.write("✅ Matched Skills")
        for skill in result["matched"]:
            st.success(skill)

        st.write("❌ Missing Skills")
        for skill in result["missing"]:
            st.error(skill)


        st.write("🎯 Points:", result["points"])
        st.divider()

        st.header("🤖 AI Recommendation:")

        st.write(result["AI Recommendation"])

        st.balloons()

        st.divider()

