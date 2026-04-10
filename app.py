import streamlit as st
import pandas as pd

from parser import extract_text, extract_skills, calculate_ats_score
from matcher import match_jobs

st.set_page_config(page_title="AI Resume Screener", layout="wide")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'> AI Resume Screening System</h1>", unsafe_allow_html=True)
st.markdown("---")

BASE_JOB_DESC = "python machine learning data analysis software development"

# ================= SINGLE RESUME =================
st.subheader("📄 Single Resume Analysis")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF or Word)",
    type=["pdf", "docx", "doc"]
)

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type not in ["pdf", "docx", "doc"]:
        st.error(" Only PDF and Word documents (.pdf, .doc, .docx) are allowed!")
        st.stop()
    text = extract_text(uploaded_file)
    skills = extract_skills(text)

    overall_ats = calculate_ats_score(text, BASE_JOB_DESC)
    results = match_jobs(text)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("###  Skills Identified")
        st.info(", ".join(skills))

        st.markdown("### Overall ATS Score")
        st.metric("ATS Score", f"{overall_ats} / 100")



    st.markdown("---")

    # JOB MATCH TABLE
    st.markdown("###  Top Job Matches")
    table_data = []
    for _, row in results.iterrows():
        table_data.append({
            "Job Role": row["title"],
            "Match Score (%)": round(row["score"] * 100, 2)
        })

    df = pd.DataFrame(table_data).sort_values(by="Match Score (%)", ascending=False)
    best_job = df.iloc[0]
    st.success(f"🏆 Best Match: {best_job['Job Role']} ({best_job['Match Score (%)']}%)")
    st.dataframe(df, use_container_width=True)

    # GRAPH
    #st.markdown("###  Job Role Comparison")
    #st.bar_chart(df.set_index("Job Role")["Match Score (%)"])


# ================= MULTIPLE RESUME =================
st.markdown("---")
st.subheader("📂 Multiple Resume Analysis")

multi_files = st.file_uploader(
    "Upload Multiple Resumes (Max 100) - PDF or Word",
    type=["pdf", "docx", "doc"],
    accept_multiple_files=True,
    key="multi"
)
if multi_files:
    valid_files = []
    invalid_files = []

    for file in multi_files:
        file_type = file.name.split(".")[-1].lower()

        if file_type in ["pdf", "docx", "doc"]:
            valid_files.append(file)
        else:
            invalid_files.append(file.name)

    # Show error for invalid files
    if invalid_files:
        st.error(f" These files are not supported: {', '.join(invalid_files)}")
    
    #  Keep only valid files
    multi_files = valid_files


#  LIMIT CHECK
    if len(multi_files) > 100:
        st.warning("⚠️ Only first 100 resumes will be processed.")
        multi_files = multi_files[:100]

    st.info(f"Total valid resumes: {len(multi_files)}")

    results_data = []
    #graph_data = []

    best_candidate = None
    best_score = 0
    best_role = ""

    #  PROCESS EACH RESUME
    for file in multi_files:
        text = extract_text(file)
        skills = extract_skills(text)
        ats_score = calculate_ats_score(text, BASE_JOB_DESC)

        # Best Job Match
        job_results = match_jobs(text)
        all_jobs = []
        for _, row in job_results.iterrows():
         all_jobs.append(f"{row['title']} ({round(row['score']*100,2)}%)")

    #  BEST JOB (for ranking)
        top_job = job_results.iloc[0]
        match_score = round(top_job["score"] * 100, 2)
        role = top_job["title"]
        results_data.append({
            "Candidate": file.name,
            "Skills": ", ".join(skills),
            "Skills Count": len(skills),
            "ATS Score": round(ats_score, 2),
            "Recommended Jobs": " | ".join(all_jobs),
            "Best Role": role,
            "Match Score": match_score
        })

        #graph_data.append({
         #   "Candidate": file.name,
          #  "Best Role": role,
          #  "Match Score": match_score
        #})

        # Track Best Candidate
        if match_score > best_score:
            best_score = match_score
            best_candidate = file.name
            best_role = role

    #  DISPLAY BEST CANDIDATE
    st.success(f" Best Candidate: {best_candidate} → {best_role} ({best_score}%)")

    #  SHOW ATS SCORES (CARDS)
    st.markdown("###  Overall ATS Scores")
    df_multi = pd.DataFrame(results_data)
    cols = st.columns(len(df_multi))
    for idx, row in df_multi.iterrows():
        with cols[idx]:
            st.metric(label=row["Candidate"], value=f"{row['ATS Score']} / 100")

    #  SKILLS TABLE
    st.markdown("###  Skills Identified")
    skills_df = df_multi[["Candidate", "Skills"]]
    st.dataframe(skills_df, use_container_width=True)

    #  BEST ROLE TABLE
    st.markdown("###  Job Recommendations (All Candidates)")

    jobs_df = df_multi[["Candidate", "Recommended Jobs"]]
    st.dataframe(jobs_df, use_container_width=True)
    #  GRAPH → Best Role Comparison
    #st.markdown("### Best Role Match Comparison")
    #graph_df = pd.DataFrame(graph_data).set_index("Candidate")["Match Score"]
    #st.bar_chart(graph_df)