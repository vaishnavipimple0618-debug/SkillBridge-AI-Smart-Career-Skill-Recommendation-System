import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="SkillBridge AI", page_icon="🚀", layout="wide")

CAREERS = [
    {"role":"Data Scientist","category":"AI & Data","skills":["Python","SQL","Statistics","Machine Learning","Pandas","Data Visualization"],"description":"Analyze data, build predictive models, and communicate insights."},
    {"role":"Machine Learning Engineer","category":"AI & Data","skills":["Python","Machine Learning","Scikit-learn","TensorFlow","Statistics","Git"],"description":"Build, evaluate, and deploy machine-learning systems."},
    {"role":"Data Analyst","category":"AI & Data","skills":["SQL","Excel","Python","Data Visualization","Statistics","Power BI"],"description":"Turn business data into clear reports and actionable insights."},
    {"role":"Frontend Developer","category":"Software Development","skills":["HTML","CSS","JavaScript","React","Git","Responsive Design"],"description":"Create accessible, responsive user interfaces for the web."},
    {"role":"Backend Developer","category":"Software Development","skills":["Python","Java","SQL","APIs","Git","Data Structures"],"description":"Build application logic, databases, and reliable services."},
    {"role":"Full Stack Developer","category":"Software Development","skills":["HTML","CSS","JavaScript","React","Python","SQL","APIs","Git"],"description":"Develop both client-side and server-side web applications."},
    {"role":"Cybersecurity Analyst","category":"Security","skills":["Networking","Linux","Cybersecurity","Python","Risk Assessment","SIEM"],"description":"Monitor systems, investigate threats, and reduce security risk."},
    {"role":"Cloud Engineer","category":"Cloud & DevOps","skills":["Linux","Networking","AWS","Docker","CI/CD","Python","Git"],"description":"Build and maintain scalable cloud infrastructure."},
    {"role":"UI/UX Designer","category":"Design","skills":["Figma","Wireframing","Prototyping","User Research","Accessibility","Visual Design"],"description":"Design intuitive digital experiences based on user needs."},
    {"role":"Business Intelligence Analyst","category":"AI & Data","skills":["SQL","Power BI","Excel","Data Visualization","Statistics","Communication"],"description":"Create dashboards and insights that support business decisions."},
]

ALL_SKILLS = sorted({skill for c in CAREERS for skill in c["skills"]})
LEARNING = {
    "Python":"Practice functions, data structures, file handling, and small automation projects.",
    "SQL":"Learn SELECT, JOIN, GROUP BY, subqueries, and database design.",
    "Machine Learning":"Study train/test splits, model evaluation, regression, classification, and clustering.",
    "Scikit-learn":"Build pipelines and compare models using cross-validation.",
    "TensorFlow":"Start with neural-network fundamentals and a small image or text classifier.",
    "Statistics":"Revise probability, distributions, hypothesis testing, and descriptive statistics.",
    "Pandas":"Practice data cleaning, grouping, merging, and exploratory analysis.",
    "Data Visualization":"Build clear charts and dashboards with a consistent visual hierarchy.",
    "HTML":"Create semantic page structure and accessible forms.",
    "CSS":"Practice Flexbox, Grid, responsive layouts, and reusable design tokens.",
    "JavaScript":"Learn DOM events, async requests, and modular programming.",
    "React":"Build reusable components, forms, and state-driven interfaces.",
    "Git":"Practice commits, branches, pull requests, and conflict resolution.",
    "Responsive Design":"Use mobile-first layouts, flexible grids, and media queries.",
    "Java":"Revise OOP, collections, exceptions, and unit testing.",
    "APIs":"Learn REST, HTTP methods, JSON, status codes, and API testing.",
    "Data Structures":"Practice arrays, linked lists, stacks, queues, trees, and complexity.",
    "Excel":"Practice formulas, pivot tables, lookups, and data cleaning.",
    "Power BI":"Learn data modeling, Power Query, DAX basics, and dashboard design.",
    "Networking":"Study TCP/IP, DNS, routing, ports, and troubleshooting.",
    "Linux":"Practice shell commands, permissions, processes, and logs.",
    "Cybersecurity":"Learn threat modeling, common vulnerabilities, and defensive controls.",
    "Risk Assessment":"Identify assets, threats, likelihood, impact, and mitigations.",
    "SIEM":"Explore log analysis, alert triage, and incident workflows.",
    "AWS":"Learn IAM, compute, storage, networking, and cost basics.",
    "Docker":"Build images, run containers, and write Dockerfiles.",
    "CI/CD":"Automate tests and deployments with a basic pipeline.",
    "Figma":"Create components, design systems, and interactive prototypes.",
    "Wireframing":"Sketch user flows and low-fidelity screen layouts.",
    "Prototyping":"Test interaction flows before implementation.",
    "User Research":"Practice interviews, usability tests, and synthesizing findings.",
    "Accessibility":"Learn contrast, keyboard navigation, labels, and WCAG principles.",
    "Visual Design":"Practice typography, spacing, alignment, and color hierarchy.",
    "Communication":"Practice explaining technical ideas clearly and concisely."
}

def get_recommendations(selected):
    # TF-IDF represents each role's skill/description text; cosine similarity ranks roles
    docs = [" ".join(c["skills"]) + " " + c["description"] for c in CAREERS]
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(docs + [" ".join(selected)])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()
    results = []
    for career, score in zip(CAREERS, scores):
        matched = [s for s in career["skills"] if s.lower() in {x.lower() for x in selected}]
        missing = [s for s in career["skills"] if s.lower() not in {x.lower() for x in selected}]
        # Score combines text similarity with transparent skill coverage.
        coverage = len(matched) / max(1, len(career["skills"]))
        final_score = round((0.55 * float(score) + 0.45 * coverage) * 100)
        results.append({**career, "score": min(final_score, 99), "matched": matched, "missing": missing})
    return sorted(results, key=lambda x: x["score"], reverse=True)

st.markdown("""
<style>
.stApp {background:#f5f7fb;}
.block-container {padding-top:1.7rem; max-width:1200px;}
.hero {background:linear-gradient(115deg,#173b8f,#356df3 62%,#7554d9);padding:28px 32px;border-radius:20px;color:white;margin-bottom:20px;}
.hero h1 {color:white;font-size:2.25rem;margin:0 0 8px 0;}
.hero p {color:#e7edff;font-size:1.02rem;margin:0;}
.metric-card {background:white;border:1px solid #e5eaf4;border-radius:16px;padding:18px 20px;min-height:105px;}
.metric-label {color:#68758d;font-size:0.85rem;}
.metric-value {font-size:1.8rem;font-weight:750;color:#1c2b4a;margin-top:4px;}
.role-card {background:white;border:1px solid #e4e9f3;border-radius:16px;padding:18px 20px;margin:10px 0;}
.pill {display:inline-block;background:#edf3ff;color:#2458c5;padding:5px 10px;border-radius:20px;font-size:0.78rem;margin:3px 4px 3px 0;}
.small-muted {color:#68758d;font-size:0.88rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>🚀 SkillBridge AI</h1>
  <p>Your skills. Your next opportunity. Personalized career recommendations powered by machine learning.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://placehold.co/220x70/173b8f/ffffff?text=SkillBridge+AI", use_container_width=True)
    st.header("Build your profile")
    name = st.text_input("Your name", value="Student")
    education = st.selectbox("Current education", ["B.Tech / B.E.", "Diploma", "B.Sc. / BCA", "MCA / M.Tech", "Other"])
    interests = st.multiselect("Career interests", ["AI & Data", "Software Development", "Security", "Cloud & DevOps", "Design"], default=["AI & Data", "Software Development"])
    selected_skills = st.multiselect("Skills you already have", ALL_SKILLS, default=["Python", "SQL", "HTML", "CSS", "JavaScript", "Git"])
    st.caption("Tip: select only skills you can comfortably explain or demonstrate.")
    run = st.button("✨ Analyze my career fit", type="primary", use_container_width=True)

if not selected_skills:
    st.info("Choose at least one skill in the sidebar to generate personalized recommendations.")
    st.stop()

results = get_recommendations(selected_skills)
if interests:
    preferred = [r for r in results if r["category"] in interests]
    others = [r for r in results if r["category"] not in interests]
    results = preferred + others

top = results[0]
avg = round(sum(r["score"] for r in results[:3]) / min(3, len(results)))
missing_count = len(set(s for r in results[:3] for s in r["missing"]))
col1, col2, col3, col4 = st.columns(4)
for col, label, value in [
    (col1, "Skills selected", str(len(selected_skills))),
    (col2, "Top career match", f'{top["score"]}%'),
    (col3, "Career paths analyzed", str(len(CAREERS))),
    (col4, "Suggested skills to explore", str(missing_count))
]:
    with col:
        st.markdown(f'<div class="metric-card"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)

st.write("")
left, right = st.columns([1.35, 1])
with left:
    st.subheader(f"Hi {name or 'there'} — your career matches")
    st.caption("Match scores are estimates from the included sample role profiles, not hiring probabilities.")
    for i, item in enumerate(results[:5], 1):
        matched = item["matched"]
        missing = item["missing"]
        with st.container(border=True):
            a, b = st.columns([4, 1])
            with a:
                st.markdown(f"### {i}. {item['role']}")
                st.caption(f'{item["category"]} · {item["description"]}')
            with b:
                st.metric("Match", f'{item["score"]}%')
            st.progress(item["score"] / 100)
            st.markdown("**Skills you have**")
            st.markdown(" ".join([f'<span class="pill">{s}</span>' for s in matched]) if matched else '<span class="small-muted">No direct skill overlap yet — start with the skill gap below.</span>', unsafe_allow_html=True)
            st.markdown("**Skills to build next**")
            st.markdown(" ".join([f'<span class="pill">{s}</span>' for s in missing[:5]]) if missing else '<span class="small-muted">Great coverage of this sample profile!</span>', unsafe_allow_html=True)

with right:
    st.subheader("Your skill-gap roadmap")
    st.caption(f"Suggested next skills for {top['role']}")
    roadmap = top["missing"][:4]
    if not roadmap:
        st.success("You cover all listed skills for the top sample role. Strengthen them with projects.")
    for idx, skill in enumerate(roadmap, 1):
        st.markdown(f"**{idx}. {skill}**")
        st.write(LEARNING.get(skill, f"Practice {skill} with a small guided project."))
    st.divider()
    st.subheader("Profile snapshot")
    st.write(f"**Education:** {education}")
    st.write(f"**Interests:** {', '.join(interests) if interests else 'Not specified'}")
    st.write(f"**Selected skills:** {', '.join(selected_skills)}")
    st.download_button("⬇️ Download my career report (CSV)",
        data=pd.DataFrame([{"Career":r["role"],"Category":r["category"],"Match score (%)":r["score"],"Matched skills":", ".join(r["matched"]),"Skills to build":", ".join(r["missing"])} for r in results]).to_csv(index=False),
        file_name="skillbridge_career_report.csv", mime="text/csv", use_container_width=True)

st.divider()
st.subheader("How the AI recommendation works")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**01 · Represent**")
    st.write("TF-IDF converts career descriptions and skill lists into numerical text features.")
with c2:
    st.markdown("**02 · Compare**")
    st.write("Cosine similarity measures text similarity; skill coverage adds a transparent skills-overlap signal.")
with c3:
    st.markdown("**03 · Recommend**")
    st.write("Career paths are ranked and missing skills are paired with learning suggestions.")
st.caption("Educational prototype. Recommendations are based on a small built-in sample dataset and should support—not replace—career guidance.")
