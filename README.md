# 🚀 HireSense AI  
## 🤖 AI-Based Interview Intelligence & Behavioral Analysis System  

### 🌐 Live Demo  
🔗 https://hiresense-aiproject-b8sve2juwiv5uvv7kkjpjx.streamlit.app/

---

# 📌 Overview  

HireSense AI is an advanced AI-powered recruitment intelligence platform designed to automate and enhance interview evaluation using Machine Learning, Natural Language Processing (NLP), and behavioral analysis techniques.

The system analyzes candidate performance through multiple AI modules including speech confidence analysis, emotion detection, resume classification, NLP-based interview assessment, and intelligent feedback generation.

The project integrates a trained Machine Learning model for resume classification using TF-IDF Vectorization and Naive Bayes Classification, making it a complete AI + Data Science based recruitment solution.

---

# ✨ Key Features  

## 🎤 Speech Confidence Analysis  
Analyze communication fluency, speaking confidence, filler words, and speech duration.

## 😊 Emotion Detection  
Detect candidate emotions and behavioral expressions during interviews using AI-based facial analysis.

## 📄 Resume Analysis & Scoring  
Evaluate resumes based on job description relevance, skills, and candidate profile matching.

## 🧠 NLP-Based Interview Analysis  
Analyze candidate answers using Natural Language Processing techniques for relevance and quality assessment.

## 🤖 Machine Learning Resume Classification  
Predict candidate job category using a trained Machine Learning model and resume dataset.

## 📈 ML Model Evaluation  
Visualize model performance using Accuracy Metrics and Confusion Matrix analysis.

## 💡 AI Suggestions Engine  
Generate intelligent feedback and improvement suggestions for candidates.

## 📊 Interactive Dashboard  
Display candidate performance analytics using dynamic charts and visualizations.

## 📝 PDF Report Generation  
Generate downloadable interview evaluation reports in PDF format.

---

# 🧠 Machine Learning Integration  

The project includes a supervised Machine Learning model trained on a Resume Classification Dataset.

### 🔹 ML Techniques Used  

- TF-IDF Vectorization  
- Naive Bayes Classification  
- NLP Text Preprocessing  
- Resume Category Prediction  
- Accuracy Evaluation  
- Confusion Matrix Visualization  

### 📌 Model Workflow  

Resume Upload  
→ Text Extraction  
→ NLP Preprocessing  
→ TF-IDF Vectorization  
→ Naive Bayes Classification  
→ Predicted Job Role  

---

# 🛠️ Technologies Used  

| Technology | Purpose |
|---|---|
| 🐍 Python | Core Backend Development |
| 🎨 Streamlit | Interactive Web Application |
| 🤖 Scikit-learn | Machine Learning Models |
| 📊 Plotly | Dashboard Visualizations |
| 🧠 NLP | Text Analysis & Classification |
| 📄 PyPDF2 | Resume Text Extraction |
| 🖼️ Pillow | Image Processing |
| 📈 Matplotlib | Confusion Matrix Visualization |
| 💾 Joblib | ML Model Serialization |

---

# 📂 Project Structure  

```bash
HireSense-AI
│
├── assets
│   └── confusion_matrix.png
│
├── ml_model
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── model.pkl
│
├── modules
│   ├── face.py
│   ├── nlp.py
│   ├── predict.py
│   ├── report.py
│   ├── resume.py
│   ├── scoring.py
│   ├── speech.py
│   └── suggestions.py
│
├── app.py
├── README.md
└── requirements.txt
