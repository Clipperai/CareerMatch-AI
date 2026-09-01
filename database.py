import sqlite3

# DATABASE CONNECTION

connection = sqlite3.connect("job_match.db")

cursor = connection.cursor()

# CREATE TABLE
cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis (
        id INTEGER PRIMARY KEY, 
        resume_skills TEXT, 
        job_skills TEXT, 
        matched_skills TEXT, 
        missing_skills TEXT, 
        score REAL
    )
""")

connection.commit()
connection.close()


# SAVE ANALYSIS
def save_analysis(resume, job, matched, missing, score):

    connection = sqlite3.connect("job_match.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO analysis
        (resume_skills, job_skills, matched_skills, missing_skills, score)
        VALUES (?, ?, ?, ?, ?)
    """, (resume, job, matched, missing, score))

    connection.commit()
    connection.close()


# GET HISTORY

def get_history():

    connection = sqlite3.connect("job_match.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM analysis ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    connection.close()
    return rows


# CALLING HISTORY FUNCTION AND PRINTING RESULT
result = get_history()
print(result)

