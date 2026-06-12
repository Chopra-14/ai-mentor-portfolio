import streamlit as st
from google import genai
import json

st.set_page_config(page_title="Resume Fit Scorer", layout="wide", page_icon="📄")

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background: #f9f9f8; }
    [data-testid="stHeader"] { background: transparent; }
    .block-container { padding: 2rem 3rem; max-width: 1100px; }

    h1 { font-size: 1.3rem !important; font-weight: 500 !important; }

    div[data-testid="metric-container"] {
        background: #ffffff;
        border: 0.5px solid #e5e5e5;
        border-radius: 12px;
        padding: 1rem 1.2rem;
    }
    div[data-testid="metric-container"] label {
        font-size: 12px !important;
        color: #888 !important;
    }
    div[data-testid="metric-container"] [data-testid="metric-value"] {
        font-size: 1.6rem !important;
        font-weight: 500 !important;
    }

    .stTextArea textarea {
        background: #f4f4f2 !important;
        border: 0.5px solid #ddd !important;
        border-radius: 10px !important;
        font-size: 13px !important;
        padding: 12px !important;
    }
    .stTextArea textarea:focus {
        border-color: #7F77DD !important;
        background: #fff !important;
    }

    .stTextInput input {
        background: #f4f4f2 !important;
        border: 0.5px solid #ddd !important;
        border-radius: 10px !important;
        font-size: 13px !important;
    }

    .stButton > button {
        background: #534AB7 !important;
        color: #fff !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        padding: 0.5rem 1.8rem !important;
        transition: background 0.15s;
    }
    .stButton > button:hover { background: #3C3489 !important; }

    .info-card {
        background: #ffffff;
        border: 0.5px solid #e5e5e5;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
    }
    .score-hero {
        background: #f4f4f2;
        border-radius: 12px;
        padding: 1.5rem;
        display: flex;
        align-items: center;
        gap: 2rem;
        margin-bottom: 1rem;
    }
    .score-num {
        font-size: 3rem;
        font-weight: 500;
        line-height: 1;
    }
    .tier-badge {
        display: inline-block;
        font-size: 12px;
        font-weight: 500;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 6px;
    }
    .chip {
        display: inline-block;
        font-size: 12px;
        padding: 4px 12px;
        border-radius: 20px;
        margin: 3px;
    }
    .chip-red { background: #FCEBEB; color: #791F1F; }
    .chip-green { background: #EAF3DE; color: #27500A; }
    .rationale-box {
        background: #f4f4f2;
        border-radius: 10px;
        padding: 14px;
        font-size: 13px;
        color: #555;
        line-height: 1.7;
    }
    .section-label {
        font-size: 13px;
        font-weight: 500;
        color: #333;
        margin-bottom: 8px;
    }
    hr { border: none; border-top: 0.5px solid #e5e5e5; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)


# ── Header ──────────────────────────────────────────────
col_logo, col_badge = st.columns([5, 1])
with col_logo:
    st.markdown("## 📄 Resume fit scorer")
    st.caption("AI-powered compatibility analysis")
with col_badge:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<span style="background:#EEEDFE;color:#3C3489;font-size:12px;font-weight:500;'
        'padding:5px 14px;border-radius:20px;">✨ Gemini 2.0 Flash</span>',
        unsafe_allow_html=True
    )

st.markdown("<hr>", unsafe_allow_html=True)

# ── Inputs ───────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="section-label">🪪 Resume</div>', unsafe_allow_html=True)
    resume = st.text_area("Resume", height=260, label_visibility="collapsed",
                          placeholder="Paste your resume here — experience, skills, education, projects…")
with col2:
    st.markdown('<div class="section-label">💼 Job description</div>', unsafe_allow_html=True)
    jd = st.text_area("Job Description", height=260, label_visibility="collapsed",
                      placeholder="Paste the job description — requirements, responsibilities, qualifications…")

# ── API Key + Button ─────────────────────────────────────
c1, c2 = st.columns([5, 1])
with c1:
    st.markdown('<div class="section-label">🔑 Gemini API key</div>', unsafe_allow_html=True)
    api_key = st.text_input("API Key", type="password", label_visibility="collapsed",
                             placeholder="Paste your Gemini API key here…")
with c2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    run = st.button("✨ Analyse fit", use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ── Score ────────────────────────────────────────────────
if run:
    if not resume or not jd or not api_key:
        field = "resume" if not resume else "job description" if not jd else "API key"
        st.warning(f"Please fill in your {field} before scoring.", icon="⚠️")
    else:
        with st.spinner("Analysing your fit…"):
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"""You are a placement coach. Compare the Resume and Job Description carefully.
Return ONLY valid JSON:
{{"score":0,"technical_skills_match":0,"soft_skills_match":0,"experience_relevance":0,"project_fit":0,"rationale":"","missing_skills":[],"suggestions":[]}}
All numeric fields are integers 0-100. missing_skills and suggestions are concise string arrays, max 6 each.
Resume:\n{resume}\n\nJob Description:\n{jd}"""

                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt,
                    config={"response_mime_type": "application/json"}
                )
                r = json.loads(response.text)

                score = int(r.get("score", 0))
                tech  = int(r.get("technical_skills_match", 0))
                soft  = int(r.get("soft_skills_match", 0))
                exp   = int(r.get("experience_relevance", 0))
                proj  = int(r.get("project_fit", 0))

                if score >= 85:
                    tier, tbg, tcolor = "Strong match", "#E1F5EE", "#0F6E56"
                elif score >= 70:
                    tier, tbg, tcolor = "Good fit", "#EEEDFE", "#534AB7"
                elif score >= 50:
                    tier, tbg, tcolor = "Moderate fit", "#FAEEDA", "#854F0B"
                else:
                    tier, tbg, tcolor = "Weak fit", "#FCEBEB", "#A32D2D"

                # Score hero
                st.markdown(f"""
                <div class="info-card">
                  <span class="tier-badge" style="background:{tbg};color:{tcolor}">{tier}</span>
                  <div style="display:flex;align-items:baseline;gap:8px;margin-bottom:6px">
                    <span class="score-num" style="color:var(--text-color)">{score}</span>
                    <span style="font-size:14px;color:#888">/100 overall fit</span>
                  </div>
                  <p style="font-size:13px;color:#666;line-height:1.6;margin:0">{r.get("rationale","")[:200]}</p>
                </div>
                """, unsafe_allow_html=True)

                # Metrics
                m1, m2, m3, m4 = st.columns(4)
                m1.metric("⚙️ Technical skills", f"{tech}/100")
                m2.metric("🤝 Soft skills",       f"{soft}/100")
                m3.metric("🏢 Experience",         f"{exp}/100")
                m4.metric("🚀 Project fit",        f"{proj}/100")

                # Progress bars
                st.markdown("<br>", unsafe_allow_html=True)
                bar_cols = st.columns(4)
                for col, (label, val) in zip(bar_cols, [
                    ("Technical", tech), ("Soft skills", soft),
                    ("Experience", exp), ("Projects", proj)
                ]):
                    with col:
                        st.caption(label)
                        st.progress(val / 100)

                st.markdown("<hr>", unsafe_allow_html=True)

                # Rationale
                st.markdown('<div class="section-label">💬 Rationale</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="rationale-box">{r.get("rationale","No rationale provided.")}</div>',
                            unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                # Missing + Suggestions
                left, right = st.columns(2)
                with left:
                    st.markdown('<div class="section-label">⚠️ Missing skills</div>', unsafe_allow_html=True)
                    chips = " ".join(f'<span class="chip chip-red">{s}</span>'
                                     for s in r.get("missing_skills", []))
                    st.markdown(chips or "<span style='color:#aaa;font-size:13px'>None identified</span>",
                                unsafe_allow_html=True)
                with right:
                    st.markdown('<div class="section-label">💡 Suggestions</div>', unsafe_allow_html=True)
                    chips = " ".join(f'<span class="chip chip-green">{s}</span>'
                                     for s in r.get("suggestions", []))
                    st.markdown(chips or "<span style='color:#aaa;font-size:13px'>None at this time</span>",
                                unsafe_allow_html=True)

            except Exception as e:
                st.error("Gemini returned an error. Please retry in 30 seconds.", icon="🚨")
                with st.expander("Error details"):
                    st.code(str(e))
