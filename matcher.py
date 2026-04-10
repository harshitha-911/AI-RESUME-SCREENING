from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def match_jobs(resume_text):
    jobs = pd.read_csv("jobs.csv")

    descriptions = jobs["description"].tolist()
    descriptions.append(resume_text)

    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(descriptions)

    similarity = cosine_similarity(matrix)

    scores = similarity[-1][:-1]

    jobs["score"] = scores
    return jobs.sort_values(by="score", ascending=False).head(5)