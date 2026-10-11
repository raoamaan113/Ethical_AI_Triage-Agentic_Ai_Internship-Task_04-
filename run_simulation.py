import json
import os
import sys

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from triage_tree import EthicalTriageTree

def main():
    # Load patient dataset
    data_path = os.path.join("data", "patient_dataset.json")
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}")
        return

    with open(data_path, "r") as f:
        patients = json.load(f)

    tree = EthicalTriageTree()
    evaluated_patients = tree.process_all_patients(patients)

    print("=" * 90)
    print("ETHICAL AI HEALTHCARE TRIAGE - TOP 10 PRIORITIZED PATIENTS SIMULATION")
    print("=" * 90)
    print(f"{'ID':<6} | {'Name':<10} | {'Age/Sex':<8} | {'Complaint':<28} | {'Score':<6} | {'Triage Level'}")
    print("-" * 90)

    for p in evaluated_patients[:10]:
        print(f"{p['patient_id']:<6} | {p['name']:<10} | {p['age']}/{p['gender'][0]:<5} | {p['chief_complaint']:<28} | {p['priority_score']:<6} | {p['triage_level']}")

    print("=" * 90)
    print(f"Successfully processed and audited all {len(patients)} emergency room patients!")

if __name__ == "__main__":
    main()