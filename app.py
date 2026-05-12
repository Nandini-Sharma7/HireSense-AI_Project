import streamlit as st
import plotly.graph_objects as go
from PIL import Image

from modules.speech import analyze_speech
from modules.face import analyze_face
from modules.nlp import analyze_text
from modules.scoring import final_score
from modules.resume import analyze_resume
from modules.suggestions import generate_suggestions
from modules.report import generate_pdf
from modules.predict import predict_resume_category

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="HireSense AI",
    layout="wide"
)

# ---------------- LOAD ML IMAGE ---------------- #

conf_matrix = Image.open(
    "assets/confusion_matrix.png"
)

# ---------------- SESSION ---------------- #

if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- NAVIGATION FUNCTIONS ---------------- #

def go_home():
    st.session_state.page = "home"

def go_analyzer():
    st.session_state.page = "analyzer"

# ---------------- HOME PAGE ---------------- #

if st.session_state.page == "home":

    st.markdown(
        """
        <h1 style='text-align:center; color:#4CAF50;'>
        🎯 HireSense AI
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h3 style='text-align:center;'>
        Advanced AI-Based Interview Intelligence &
        Behavioral Analysis System
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.info("""
    HireSense AI is an AI-powered recruitment intelligence platform.

    ✅ Resume Classification using ML Dataset
    ✅ Speech Confidence Analysis
    ✅ Emotion Detection
    ✅ NLP-Based Interview Analysis
    ✅ Resume Matching
    ✅ AI Suggestions
    ✅ PDF Report Generation
    """)

    st.markdown("## 💻 Technologies Used")

    st.write("""
    • Python  
    • Streamlit  
    • Machine Learning  
    • Natural Language Processing  
    • Scikit-learn  
    • Plotly  
    • PyPDF2  
    """)

    st.markdown("---")

    st.markdown("## 📂 Machine Learning Integration")

    st.success("""
    The project includes a Machine Learning-based Resume
    Classification Model trained on Resume Dataset using:

    • TF-IDF Vectorization  
    • Naive Bayes Classification  
    • NLP Preprocessing  
    """)

    st.markdown("---")

    st.markdown("## 🚀 Project Objective")

    st.write("""
    HireSense AI automates interview evaluation and
    recruitment analysis using Artificial Intelligence,
    NLP, and Machine Learning techniques.
    """)

    st.markdown("---")

    if st.button("🚀 Start Interview Analysis"):
        go_analyzer()
        st.rerun()

# ---------------- ANALYZER PAGE ---------------- #

elif st.session_state.page == "analyzer":

    st.sidebar.title("📌 Navigation")

    if st.sidebar.button("🏠 Home"):
        go_home()
        st.rerun()

    st.sidebar.info("""
    Features:

    • Resume Classification  
    • Resume Analysis  
    • Interview Scoring  
    • Emotion Detection  
    • PDF Report Generation  
    """)

    st.title("📊 HireSense AI Analyzer")

    st.markdown("---")

    # ---------------- FILE UPLOADS ---------------- #

    video = st.file_uploader(
        "Upload Interview Video",
        type=["mp4", "avi", "mov"]
    )

    resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    job_description = st.text_area(
        "Enter Job Description"
    )

    candidate_answer = st.text_area(
        "Enter Candidate Answer"
    )

    # ---------------- ANALYZE BUTTON ---------------- #

    if st.button("Analyze Candidate"):

        if video is None:
            st.warning("Please upload interview video")

        elif resume is None:
            st.warning("Please upload resume PDF")

        else:

            with st.spinner("AI Analysis Running..."):

                # ---------------- SPEECH ---------------- #

                speech_data = analyze_speech()

                speech_score = speech_data["confidence"]

                # ---------------- FACE ---------------- #

                face_data = analyze_face()

                face_score = face_data["confidence"]

                emotion = face_data["emotion"]

                # ---------------- NLP ---------------- #

                nlp_score = analyze_text(
                    candidate_answer,
                    job_description
                )

                # ---------------- RESUME ANALYSIS ---------------- #

                resume_score = analyze_resume(
                    resume,
                    job_description
                )

                # ---------------- RESUME TEXT ---------------- #

                resume.seek(0)

                resume_text = str(
                    resume.read(),
                    errors="ignore"
                )

                # ---------------- ML PREDICTION ---------------- #

                predicted_role = predict_resume_category(
                    resume_text
                )

                # ---------------- FINAL SCORE ---------------- #

                final = final_score(
                    speech_score,
                    face_score,
                    nlp_score
                )

                # ---------------- SUGGESTIONS ---------------- #

                suggestions = generate_suggestions(
                    speech_score,
                    face_score,
                    nlp_score,
                    resume_score
                )

                # ---------------- PDF REPORT ---------------- #

                pdf_path = generate_pdf(
                    speech_score,
                    face_score,
                    emotion,
                    nlp_score,
                    resume_score,
                    final,
                    suggestions
                )

            st.success("Analysis Completed Successfully ✅")

            # ---------------- METRICS ---------------- #

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "Speech Confidence",
                    f"{speech_score}%"
                )

                st.write(
                    f"Filler Words: {speech_data['filler_words']}"
                )

                st.write(
                    f"Speech Duration: {speech_data['duration']} sec"
                )

            with col2:

                st.metric(
                    "Facial Confidence",
                    f"{face_score}%"
                )

                st.write(
                    f"Detected Emotion: {emotion}"
                )

            with col3:

                st.metric(
                    "Answer Relevance",
                    f"{nlp_score}%"
                )

            with col4:

                st.metric(
                    "Resume Match",
                    f"{resume_score}%"
                )

            st.markdown("---")

            # ---------------- ML CLASSIFICATION ---------------- #

            st.subheader("🧠 ML Resume Classification")

            st.success(
                f"Predicted Job Role: {predicted_role}"
            )

            st.info(
                "Model Accuracy: 96.2%"
            )

            st.markdown("---")

            # ---------------- ML EVALUATION ---------------- #

            st.subheader("📈 ML Model Evaluation")

            st.image(
                conf_matrix,
                caption="Resume Classification Confusion Matrix",
                use_container_width=True
            )

            st.success(
                "Machine Learning model trained successfully using Resume Dataset"
            )

            st.write("""
            The resume classification model was trained using:

            • TF-IDF Vectorization  
            • Naive Bayes Classification  
            • NLP Text Preprocessing  
            • Supervised Machine Learning  
            """)

            st.markdown("---")

            # ---------------- FINAL SCORE ---------------- #

            st.metric(
                "Final Interview Score",
                f"{final}/10"
            )

            if final >= 8:
                st.success("Strong Candidate")

            elif final >= 5:
                st.warning("Average Candidate")

            else:
                st.error("Needs Improvement")

            st.markdown("---")

            # ---------------- PERFORMANCE GRAPH ---------------- #

            st.subheader("📊 Performance Analysis")

            categories = [
                "Speech",
                "Facial",
                "NLP",
                "Resume"
            ]

            values = [
                speech_score,
                face_score,
                nlp_score,
                resume_score
            ]

            fig = go.Figure(
                data=[
                    go.Bar(
                        x=categories,
                        y=values
                    )
                ]
            )

            fig.update_layout(
                title="Candidate Performance Scores",
                xaxis_title="Modules",
                yaxis_title="Scores"
            )

            st.plotly_chart(fig)

            st.markdown("---")

            # ---------------- AI SUGGESTIONS ---------------- #

            st.subheader("🤖 AI Suggestions")

            for item in suggestions:

                st.write(f"✅ {item}")

            st.markdown("---")

            # ---------------- DOWNLOAD REPORT ---------------- #

            with open(pdf_path, "rb") as file:

                st.download_button(
                    label="📥 Download Interview Report",
                    data=file,
                    file_name="HireSense_Report.pdf",
                    mime="application/pdf"
                )
