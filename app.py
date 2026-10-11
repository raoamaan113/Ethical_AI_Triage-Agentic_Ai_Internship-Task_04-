import streamlit as st
import json
import os
import pandas as pd
import sys

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from triage_tree import EthicalTriageTree

# Page Configuration
st.set_page_config(
    page_title="Ethical AI Healthcare Triage Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Ethical AI Decision-Making Framework for Healthcare Triage")
st.markdown("### Agentic AI Internship - Task 4 | Balancing Clinical Efficiency & Fairness")
st.divider()

# Load Dataset
@st.cache_data
def load_data():
    data_path = os.path.join("data", "patient_dataset.json")
    with open(data_path, "r") as f:
        return json.load(f)

raw_patients = load_data()
tree = EthicalTriageTree()
evaluated_patients = tree.process_all_patients(raw_patients)
df = pd.DataFrame(evaluated_patients)

# Sidebar Controls
st.sidebar.header("🔍 Triage Filters & Controls")
selected_level = st.sidebar.selectbox(
    "Filter by Triage Level", 
    ["All Levels", "Level 1: Immediate Resuscitation", "Level 2: Emergent", "Level 3: Urgent", "Level 4-5: Non-Urgent / Semi-Urgent"]
)

if selected_level != "All Levels":
    filtered_df = df[df["triage_level"] == selected_level]
else:
    filtered_df = df

# Main Metrics Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Patients Processed", len(df))
col2.metric("Level 1 (Immediate)", len(df[df["triage_level"].str.contains("Level 1")]))
col3.metric("Fairness Safeguards Triggered", int(df["fairness_safeguard_applied"].sum()))
col4.metric("Avg Priority Score", round(df["priority_score"].mean(), 1))

st.divider()

# Layout: Tabs for Table View & Analytics
tab1, tab2, tab3 = st.tabs(["📋 Prioritized Patient Queue", "📊 Fairness & Bias Audit", "⚙️ Ethical Framework Architecture"])

with tab1:
    st.subheader("Live Emergency Room Patient Queue")
    st.caption("Sorted dynamically by clinical severity, wait time compensation, and ethical parity safeguards.")
    
    # Display styled dataframe
    st.dataframe(
        filtered_df[[
            "patient_id", "name", "age", "gender", "chief_complaint", 
            "vitals_severity", "wait_time_min", "priority_score", "triage_level", "fairness_safeguard_applied"
        ]],
        use_container_width=True,
        hide_index=True
    )

with tab2:
    st.subheader("Ethical Fairness & Demographic Distribution Audit")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("##### Age vs. Priority Score Distribution")
        st.scatter_chart(df, x="age", y="priority_score", color="vitals_severity")
        st.caption("Ensures elderly patients with high vulnerability are not systematically deprioritized.")

    with col_b:
        st.markdown("##### Triage Level Breakdown")
        level_counts = df["triage_level"].value_counts()
        st.bar_chart(level_counts)
        st.caption("Volume distribution across emergency severity tiers.")

with tab3:
    st.subheader("Core Ethical Principles Implemented in Task 4")
    st.markdown("""
    1. **Non-Maleficence & Clinical Urgency:** Prioritizes immediate life threats (cardiac arrest, stroke, trauma) above all else based on vitals severity.
    2. **Wait Time Compensation:** Prevents neglect of patients stuck waiting in queues by introducing a progressive priority bonus over 30 and 60 minutes.
    3. **Fairness & Vulnerability Safeguards:** Audits historical disparity risks and applies equitable score adjustments to prevent bias against elderly or vulnerable demographics.
    4. **Transparency & Explainability:** Every prioritization score is fully traceable back to its clinical and ethical rule parameters.
    """)

st.divider()
# Footer Section with Author Name
st.markdown("""
    <div class="footer-box">
        <p style="margin: 0; font-size: 1.1rem; font-weight: 600; color: #1F2937;">
            Developed for Agentic AI Internship | Institution: VisaBridge | Supervisor: Zeeshan Usmani
        </p>
        <p style="margin: 5px 0 0 0; font-size: 1.2rem; font-weight: 700; color: #2563EB;">
            Created by: Rao Muhammad Amaan
        </p>
    </div>
""", unsafe_allow_html=True)