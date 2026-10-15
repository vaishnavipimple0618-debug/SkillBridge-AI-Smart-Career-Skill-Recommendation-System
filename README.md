# SkillBridge AI — Smart Career & Skill Recommendation System

## Overview
SkillBridge AI is a student-facing AI/ML web app that ranks career paths based on a user's selected skills. It combines TF-IDF text representation, cosine similarity, and a transparent skill-coverage score. It also highlights missing skills and provides starter learning actions.

## Features
- Responsive Streamlit dashboard
- Profile inputs: name, education, interests, and current skills
- Top-five career recommendations with match scores
- Matched-skill and skill-gap breakdown
- Learning roadmap for the highest-ranked career
- Downloadable CSV report
- Local execution; no API key or paid service required

## Tech stack
Python, Streamlit, pandas, scikit-learn, TF-IDF, cosine similarity.

## Run locally (Windows / VS Code)
1. Install Python 3.10 or newer from https://www.python.org/downloads/
2. Extract the project ZIP and open the `skillbridge_ai_project` folder in VS Code.
3. Open Terminal → New Terminal.
4. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
5. Activate it on Windows PowerShell:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, use Command Prompt:
   ```bat
   .venv\Scripts\activate.bat
   ```
6. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
7. Start the app:
   ```bash
   streamlit run app.py
   ```
8. Streamlit will show a local URL, usually http://localhost:8501. Open it in your browser.

## How to use
1. Enter your name and education in the sidebar.
2. Select career interests and the skills you already have.
3. Review career matches and skill gaps.
4. Download the CSV report if needed.

## Method
Each career profile is represented as text containing its skills and description. TF-IDF transforms these documents into weighted vectors. Cosine similarity compares the selected skills with each profile. A second signal measures the fraction of required sample skills already selected. The final score is:
`match_score = 0.55 × cosine_similarity + 0.45 × skill_coverage`, expressed as a percentage and capped at 99.

## Important limitations
- The role catalog is a small illustrative sample, not a live labor-market database.
- Scores are relative fit indicators, not a probability of employment or guaranteed hiring result.
- Skills are selected by the user; the app does not verify proficiency.
- Recommendations should be reviewed with mentors and updated as role requirements change.

## Suggested future improvements
- Add resume parsing with explicit user consent
- Expand and regularly validate the role/skill dataset
- Add explainable evaluation using a labeled benchmark dataset
- Add user accounts and privacy-conscious profile storage
- Add multilingual support and accessibility testing

## Submission checklist
- [ ] Run the app successfully on your own laptop
- [ ] Replace sample profile defaults with your own demo
- [ ] Capture your own live UI screenshots
- [ ] Add your name, institute, and internship details to the report/PPT
- [ ] Verify your IBM BOB Masterclass 1 instructions and submission form requirements
