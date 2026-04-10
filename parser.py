import PyPDF2
import spacy
import docx

nlp = spacy.load("en_core_web_sm")

   

SKILLS_DB = [
    "python","java","c++","machine learning","deep learning","nlp",
    "data analysis","pandas","numpy","sql","html","css",
    "javascript","react","node","django","flask","tensorflow"
]

# Extract text from PDF
def extract_text(file):
    file_type = file.name.split(".")[-1].lower()

    text = ""

    # PDF
    if file_type == "pdf":
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()

    # DOCX
    elif file_type == "docx":
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    # DOC (basic support)
    elif file_type == "doc":
        text = "DOC format not fully supported. Please upload DOCX or PDF."

    return text

# Extract skills
def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))

# ATS Score
def calculate_ats_score(resume_text, job_desc):
    resume_text = resume_text.lower()
    job_desc = job_desc.lower()

    score = 0

    #  Keyword Matching (50%)
    job_keywords = job_desc.split()
    matched = sum(1 for word in job_keywords if word in resume_text)
    keyword_score = (matched / len(job_keywords)) * 50

    #  Skills Matching (20%)
    skills = extract_skills(resume_text)
    skill_score = min(len(skills) * 4, 20)  # max 20

    #  Experience Section (15%)
    experience_score = 15 if "experience" in resume_text or "internship" in resume_text else 5

    #  Education Section (5%)
    education_score = 5 if "education" in resume_text else 2

    #  Resume Length & Structure (10%)
    length_score = 10 if 800 < len(resume_text) < 3000 else 5

    score = keyword_score + skill_score + experience_score + education_score + length_score

    return round(score, 2)
