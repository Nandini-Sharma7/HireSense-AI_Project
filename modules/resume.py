from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_resume_text(pdf_file):

    text = ""

    reader = PdfReader(pdf_file)

    for page in reader.pages:
        text += page.extract_text()

    return text


def analyze_resume(pdf_file, job_description):

    resume_text = extract_resume_text(pdf_file)

    texts = [resume_text, job_description]

    vectorizer = TfidfVectorizer()

    tfidf = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(
        tfidf[0:1],
        tfidf[1:2]
    )

    score = round(similarity[0][0] * 100)

    return score