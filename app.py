import streamlit as st
import plotly.graph_objects as go

from modules.speech import analyze_speech
from modules.face import analyze_face
from modules.nlp import analyze_text
from modules.scoring import final_score
from modules.resume import analyze_resume
from modules.suggestions import generate_suggestions
from modules.report import generate_pdf


st.set_page_config(
    page_title="HireSense AI",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("📌 Navigation")

st.sidebar.info(
    """
    HireSense AI Dashboard

    Features:
    - Resume Analysis
    - Interview Scoring
    - Emotion Detection
    - PDF Report Generation
    """
)

# ---------------- HEADER ---------------- #

st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
        🎯 HireSense AI
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='text-align: center;'>
        Advanced AI-Based Interview Intelligence & Behavioral Analysis System
    </h4>
    """,
    unsafe_allow_html=True
)

st.info(
    """
    HireSense AI analyzes interview performance using:

    ✅ Speech Analysis  
    ✅ Emotion Detection  
    ✅ NLP Relevance Scoring  
    ✅ Resume Matching  
    ✅ AI Suggestions
    """
)

st.markdown("---")

# ---------------- INPUT SECTION ---------------- #

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

# ---------------- ANALYSIS ---------------- #

if st.button("Analyze Candidate"):

    if video is None:
        st.warning("Please upload a video")

    elif resume is None:
        st.warning("Please upload resume PDF")

    else:

        with st.spinner("AI Analysis Running..."):

            # Speech Analysis
            speech_data = analyze_speech()

            speech_score = speech_data["confidence"]

            # Face Analysis
            face_data = analyze_face()

            face_score = face_data["confidence"]

            emotion = face_data["emotion"]

            # NLP Analysis
            nlp_score = analyze_text(
                candidate_answer,
                job_description
            )

            # Resume Analysis
            resume_score = analyze_resume(
                resume,
                job_description
            )

            # Final Score
            final = final_score(
                speech_score,
                face_score,
                nlp_score
            )

            # AI Suggestions
            suggestions = generate_suggestions(
                speech_score,
                face_score,
                nlp_score,
                resume_score
            )

            # PDF Report
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

        # ---------------- GRAPH ---------------- #

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