import streamlit as st
from google import genai
import json

st.set_page_config(
    page_title="Resume Scorer",
    layout="wide"
)

st.title("Resume vs JD Fit Scorer")
st.caption("Day 5 Lab 5A")

col1, col2 = st.columns(2)

with col1:
    resume = st.text_area(
        "Paste Resume",
        height=400
    )

with col2:
    jd = st.text_area(
        "Paste Job Description",
        height=400
    )

api_key = st.text_input(
    "Gemini API Key",
    type="password"
)

if st.button("Score"):

    if not resume or not jd or not api_key:
        st.warning("Please fill all fields")

    else:

        try:

            with st.spinner("Scoring..."):

                client = genai.Client(
                    api_key=api_key
                )

                prompt = f"""
You are a placement coach.

Compare Resume and Job Description.

Return ONLY JSON.

{{
"score": 0,
"technical_skills_match": 0,
"soft_skills_match": 0,
"experience_relevance": 0,
"project_fit": 0,
"rationale": "",
"missing_skills": [],
"suggestions": []
}}

Resume:
{resume}

Job Description:
{jd}
"""

                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt,
                    config={
                        "response_mime_type": "application/json"
                    }
                )

            result = json.loads(
                response.text
            )

            st.metric(
                "Fit Score",
                f"{result.get('score',0)}/100"
            )

            st.subheader(
                "Score Breakdown"
            )

            chart = {
                "Technical":
                result.get(
                    "technical_skills_match",
                    0
                ),

                "Soft":
                result.get(
                    "soft_skills_match",
                    0
                ),

                "Experience":
                result.get(
                    "experience_relevance",
                    0
                ),

                "Projects":
                result.get(
                    "project_fit",
                    0
                )
            }

            st.bar_chart(chart)

            st.subheader("Rationale")
            st.write(
                result.get(
                    "rationale",
                    ""
                )
            )

            st.subheader(
                "Missing Skills"
            )

            for skill in result.get(
                "missing_skills",
                []
            ):
                st.write(
                    f"• {skill}"
                )

            st.subheader(
                "Suggestions"
            )

            for suggestion in result.get(
                "suggestions",
                []
            ):
                st.write(
                    f"• {suggestion}"
                )

        except Exception as e:

            st.error(
                "Gemini busy. Retry after 30 seconds."
            )

            st.code(str(e))