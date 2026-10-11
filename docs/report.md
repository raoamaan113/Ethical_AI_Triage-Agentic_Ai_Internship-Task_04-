# Ethical AI Decision-Making Framework for Healthcare Triage

**Author:** Rao Muhammad Amaan  
**Institution:** VisaBridge  
**Supervisor & Mentor:** Zeeshan Usmani  
**Program:** Agentic AI Internship (Task 4)  

---

## 1. Introduction & Executive Summary
In high-stakes emergency department (ED) environments managing high daily patient volumes (e.g., 50 patients/day), automated triage systems must balance operational efficiency with strict ethical guardrails. Traditional algorithmic triage often optimizes purely for speed or immediate clinical severity, risking systemic neglect of vulnerable demographics, elderly patients, or individuals facing prolonged wait times. 

This project establishes a transparent, equitable Ethical AI Triage Framework that combines clinical urgency (vital signs severity), wait-time compensation bonuses, and fairness audits to ensure fair, accountable patient prioritization.

---

## 2. Ethical Principles & Risk Analysis

### Core Ethical Pillars
1. **Non-Maleficence & Clinical Priority:** Life-threatening emergencies (e.g., cardiac arrest, acute stroke, major trauma) must invariably supersede non-urgent cases.
2. **Distributive Justice & Wait-Time Compensation:** Patients stuck in queues for extended durations (>30 and >60 minutes) receive progressive priority adjustments to prevent queue starvation.
3. **Fairness & Vulnerability Parity:** Mitigates historical disparities by flagging vulnerability and applying equitable review adjustments, preventing algorithmic bias against elderly or marginalized populations.
4. **Transparency & Explainability:** Every priority score is fully auditable, breaking down exact scoring weights for clinical vitals, wait times, and fairness safeguards.

### Identified Ethical Risks & Mitigation
- **Risk 1 (Age Bias):** Algorithms prioritizing speed might deprioritize elderly patients with atypical symptom presentations.  
  *Mitigation:* Integration of vulnerability weighting and vital-severity floors.
- **Risk 2 (Queue Starvation):** Patients with moderate scores continually pushed back by new high-acuity arrivals.  
  *Mitigation:* Wait-time bonus increments (+8 for >30 mins, +15 for >60 mins).

---

## 3. System Architecture & Decision Tree Logic

The framework is implemented via a modular Python backend (`src/triage_tree.py`) and visualized through an interactive Streamlit dashboard (`app.py`).