from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def analyze_text(answer, job_desc):

    texts = [answer, job_desc]

    vectorizer = TfidfVectorizer()

    tfidf = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])

    score = round(similarity[0][0] * 100)

    return score