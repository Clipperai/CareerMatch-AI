# NORMALIZE SKILL FUNCTION

def normalize_skill(skill):

    skill = " ".join(skill.split())
    skill = skill.lower()
    skill = skill.replace("apis", "api")
    
    return skill


# CALCULATE MATCH FUNCTION
def calculate_match(resume_skills, job_skills):


    skill_weights = {
        "python": 3,
        "dsa": 3,
        "restful api": 3,
        "hld": 2,
        "lld": 2,
        "llms": 2,
        "go": 1,
        "node.js": 1
    }

    points = 0


    resume_skills = {normalize_skill(skill) for skill in resume_skills}

    job_skills = {normalize_skill(skill) for skill in job_skills}

    matched = resume_skills & job_skills
    missing = job_skills - resume_skills

    for skill in matched:
            
            points += skill_weights.get(skill, 0) 

    match_percentage = (points / sum(skill_weights.values())) * 100

    return matched, missing, match_percentage, points