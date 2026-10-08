# IT Governance AI Auditor (Agentic Workflow)

## Project Overview
In modern enterprise environments, maintaining accurate Configuration Management Database (CMDB) records is a massive challenge. Discrepancies between asset management tools (like Jira Assets) and actual network activity (e.g., SolarWinds logs) lead to security vulnerabilities, budget leaks, and compliance issues. 

This project demonstrates an **Agentic AI Workflow** designed to act as an automated IT Governance Auditor. Using advanced **Prompt Engineering**, the AI agent analyzes synthetic IT asset data to identify critical anomalies, data fill-rate gaps, and formatting inconsistencies, ultimately outputting a structured, machine-readable JSON report.

## Agent Architecture & Workflow
1. **Data Ingestion:** Reads raw asset data containing Jira statuses, network last-seen dates, MAC addresses, and warranty expirations.
2. **AI Reasoning (System Prompt):** Applies strict IT governance constraints via a highly structured Persona-driven prompt to evaluate each record.
3. **Automated Auditing Execution:** 
   - Cross-references "Retired/Missing" statuses with recent network pings (Critical Security Risks).
   - Validates missing "Assigned User" or "MAC Address" fields (CMDB Fill-rate).
   - Detects inconsistent date and hardware formats.
4. **Structured Output:** Generates a deterministic JSON output ready to be consumed by IT service management (ITSM) dashboards or automated ticketing systems.

## Repository Structure
* `/data` : Contains the `mock_jira_assets.csv` dataset, carefully engineered with intentional governance anomalies.
* `/prompts` : Holds the core `system_prompt_v1.txt` showcasing the system instructions, output formatting rules, and validation constraints.
* `/notebooks` : Includes `ai_auditor_simulation.py`, a Python script simulating the data extraction with Pandas and the expected LLM API interaction.

## Business Impact & ROI
* **Risk Mitigation:** Instantly highlights "ghost" devices (e.g., retired laptops still active on the network), preventing unauthorized access.
* **Operational Efficiency:** Transforms hours of manual Excel/VLOOKUP cross-referencing into a seconds-long automated AI pipeline.
* **Data Quality:** Proactively ensures CMDB fill-rate compliance for critical fields, establishing a reliable source of truth for the IT Operations team.

---
*Developed as a professional portfolio project to showcase IT Business Analysis, Prompt Engineering, and AI-driven process automation capabilities.*
