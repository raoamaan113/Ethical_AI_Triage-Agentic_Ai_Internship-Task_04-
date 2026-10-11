class EthicalTriageTree:
    """
    Ethical Triage Decision Tree for Healthcare AI
    Prioritizes patients based on:
    1. Vitals Severity (Clinical Urgency)
    2. Wait Time Compensation (Preventing neglect of long-waiting patients)
    3. Ethical Safeguards (Fairness adjustment to mitigate historical disparity risks)
    """
    def __init__(self):
        pass

    def evaluate_patient(self, patient: dict) -> dict:
        severity = patient.get("vitals_severity", 1)
        wait_time = patient.get("wait_time_min", 0)
        disparity_risk = patient.get("historical_disparity_risk", False)
        
        # Base priority score derived from clinical severity (Scale 1-10)
        priority_score = severity * 10
        
        # Wait time weighting: Add urgency bonus if wait time is excessive (>45 mins)
        wait_bonus = 0
        if wait_time > 60:
            wait_bonus = 15
        elif wait_time > 30:
            wait_bonus = 8
            
        priority_score += wait_bonus
        
        # Ethical Safeguard: Boost review priority slightly for historical disparity/vulnerability flags
        # to ensure equitable review and prevent systemic oversight.
        fairness_adjustment = 0
        if disparity_risk and severity >= 5:
            fairness_adjustment = 5
            priority_score += fairness_adjustment

        # Determine Triage Level & Action Category
        if priority_score >= 80 or severity >= 9:
            triage_level = "Level 1: Immediate Resuscitation"
            action = "Direct to Trauma Bay / Emergency Doctor"
        elif priority_score >= 60 or severity >= 7:
            triage_level = "Level 2: Emergent"
            action = "Priority Physician Evaluation within 15 mins"
        elif priority_score >= 40 or severity >= 4:
            triage_level = "Level 3: Urgent"
            action = "Standard Examination within 30-45 mins"
        else:
            triage_level = "Level 4-5: Non-Urgent / Semi-Urgent"
            action = "Queue for Standard Waiting Room"

        return {
            "patient_id": patient["patient_id"],
            "name": patient["name"],
            "age": patient["age"],
            "gender": patient["gender"],
            "chief_complaint": patient["chief_complaint"],
            "vitals_severity": severity,
            "wait_time_min": wait_time,
            "priority_score": priority_score,
            "triage_level": triage_level,
            "recommended_action": action,
            "fairness_safeguard_applied": fairness_adjustment > 0
        }

    def process_all_patients(self, patients: list) -> list:
        results = [self.evaluate_patient(p) for p in patients]
        # Sort by priority score in descending order (highest priority first)
        results.sort(key=lambda x: x["priority_score"], reverse=True)
        return results