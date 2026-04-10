# 🚀 AI-Powered Resume Screening & Job Recommendation System

## 📌 Overview

This project is an **AI-based Resume Screening System** that analyzes resumes and recommends the most suitable job roles based on skills and content.

It supports both **Single Resume Analysis** and **Multiple Resume Comparison**, helping recruiters and candidates make better decisions.

---

## ✨ Key Features

### 📄 Single Resume Analysis

* Extracts text from **PDF and Word (DOCX)** resumes
* Identifies **technical skills**
* Calculates **Overall ATS Score (out of 100)**
* Provides **resume improvement feedback**
* Displays **Top Job Matches in tabular format**
* Visualizes job-role comparison using graphs

---

### 📂 Multiple Resume Analysis (Up to 100 Resumes)

* Upload and analyze **multiple resumes at once**
* Displays **ATS Score for each candidate**
* Shows **skills identified for all candidates**
* Provides **multiple job recommendations per candidate**
* Highlights **Best Candidate based on job match score**
* Clean **comparison tables for all candidates**
* Graphical comparison of candidate performance

---

## 🧠 Technologies Used

* **Python**
* **Streamlit** – UI & Dashboard
* **Pandas & NumPy** – Data processing
* **PyPDF2** – PDF parsing
* **python-docx** – Word document processing
* **Scikit-learn** – Job matching (similarity scoring)
* **NLTK / SpaCy** – Skill extraction

---

## 🗂 Project Structure

```
AI-Resume-Screener/
│
├── app.py              # Main Streamlit application
├── parser.py           # Resume parsing & ATS logic
├── matcher.py          # Job matching logic
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
├── resumes/            # Sample resumes (optional)
└── jobs/               # Job descriptions (optional)
```

---

## ⚙️ How It Works

1. **Upload Resume(s)**

   * Supports PDF and Word files

2. **Text Extraction**

   * Extracts content using parsing libraries

3. **Skill Identification**

   * Detects relevant technical skills

4. **ATS Scoring**

   * Calculates overall resume score

5. **Job Matching**

   * Matches resume with job roles using similarity

6. **Visualization**

   * Displays tables and graphs for insights

---

## ▶️ How to Run the Project


Follow these steps to set up and run the project from scratch:

---

### 🔹 Step 1: Install Prerequisites

Make sure you have the following installed:

* Python (version 3.8 or above)
* Git

Check installation:

```bash
python --version
git --version
```

---

### 🔹 Step 2: Clone the Repository

Download the project to your local machine:

```bash
git clone https://github.com/your-username/AI-Resume-Screener.git
cd AI-Resume-Screener
```

---

### 🔹 Step 3: Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

* **Windows:**

```bash
venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 🔹 Step 4: Install Dependencies

Install all required libraries:

```bash
pip install -r requirements.txt
```

---

### 🔹 Step 5: Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

---

### 🔹 Step 6: Open in Browser

After running, you will see a local URL like:

```text
http://localhost:8501
```

Open this link in your browser.

---

### 🔹 Step 7: Use the Application

* Upload a **single resume** (PDF/DOCX)
* Or upload **multiple resumes (up to 100)**
* View ATS score, skills, job matches, and graphs

---

## ⚠️ Important Notes

* Supported formats: **PDF, DOCX**
* `.doc` files have limited support
* Ensure internet connection for first-time library downloads

---


## 📊 Output Features

* 🎯 ATS Score (Overall)
* 🧠 Skills Identified
* 📢 Resume Feedback
* 📋 Job Match Tables
* 📊 Graphical Comparisons
* 🏆 Best Candidate Selection (Multiple Resumes)

---

## 🚧 Limitations

* Basic support for `.doc` files (recommended: use `.docx`)
* ATS scoring is rule-based (can be improved with AI models)

---

## 🔮 Future Enhancements

* 🤖 Integration with **BERT / LLM models**
* 📄 Downloadable **PDF Reports**
* 🌐 Deploy on **Streamlit Cloud / AWS**
* 🎨 Advanced UI improvements
* 📊 Skill-wise analytics

---




