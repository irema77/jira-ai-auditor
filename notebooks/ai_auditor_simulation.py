import pandas as pd
import json

def run_ai_auditor_simulation():
    print("--- IT Governance AI Auditor Initialized ---\\n")
    
    # 1. Load the mock CMDB data
    print("[1] Loading CMDB data from Jira Assets...")
    df = pd.read_csv('../data/mock_jira_assets.csv')
    print(f"    Loaded {len(df)} asset records successfully.\\n")

    # 2. Load the AI System Prompt
    print("[2] Loading AI System Prompt and Constraints...")
    with open('../prompts/system_prompt_v1.txt', 'r') as file:
        system_prompt = file.read()
    print("    System Prompt loaded successfully.\\n")

    # 3. Simulate LLM API Call (Mocking the AI processing)
    print("[3] Sending data and prompt to LLM for analysis...\\n")
    
    # This dictionary simulates the exact JSON response an LLM would generate 
    # based on the strict rules defined in our system_prompt_v1.txt
    mock_llm_response = {
        "critical_anomalies": [
            {"asset_id": "AST-1004", "issue": "Status is 'Retired' but shows recent network activity on 2026-10-07. Security Risk."},
            {"asset_id": "AST-1009", "issue": "Status is 'Missing' but network activity detected on 2026-06-10. Investigate immediately."}
        ],
        "data_gaps": [
            {"asset_id": "AST-1002", "issue": "Missing MAC_ADDRESS for active Server."},
            {"asset_id": "AST-1003", "issue": "Missing ASSIGNED_USER for active Laptop."},
            {"asset_id": "AST-1010", "issue": "Missing ASSIGNED_USER for active Tablet."}
        ],
        "formatting_errors": [
            {"asset_id": "AST-1003", "issue": "Invalid MAC address format (00-1A-2B-3C-XX)."},
            {"asset_id": "AST-1007", "issue": "Inconsistent date format in WARRANTY_EXPIRY (05.08.2024)."},
            {"asset_id": "AST-1010", "issue": "Inconsistent date format in WARRANTY_EXPIRY (02/28/2026)."}
        ],
        "audit_summary": {
            "total_assets_scanned": 10,
            "critical_risks_found": 2,
            "data_gaps_found": 3,
            "compliance_score": "50%"
        }
    }
    
    # 4. Output the Results
    print("--- AI AUDITOR JSON OUTPUT ---\\n")
    print(json.dumps(mock_llm_response, indent=4))

if __name__ == "__main__":
    run_ai_auditor_simulation()
