from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats(resume, job_desc):
    texts = [resume, job_desc]
    cv = CountVectorizer().fit_transform(texts)
    similarity = cosine_similarity(cv)[0][1]
    
    # Example weights (you can refine later)
    keyword_match = similarity         # keywords match
    skills_match = similarity          # skills similarity (for demo, same as keyword)
    experience = 0.8                   # dummy value: 0-1 scale (improve later)
    format = 1.0                       # dummy value: 0-1 scale (resume format)

    score = (
        keyword_match * 0.4 +
        skills_match * 0.3 +
        experience * 0.2 +
        format * 0.1
    ) * 100  # convert to 0-100 scale

    return round(score, 2)