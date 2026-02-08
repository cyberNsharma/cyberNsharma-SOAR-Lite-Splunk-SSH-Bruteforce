# SOAR-Lite Splunk SSH Brute Force Detection

## Overview
This project demonstrates a **blue team SOC workflow** for detecting, triaging, and automating response decisions for **SSH brute force attacks** using Splunk and Python-based SOAR-lite automation.

The focus is not just detection, but **analyst-style decision making**, noise reduction, and automation efficiency.

---

## Attack Scenario
- SSH brute force attack simulated from Kali Linux
- Target system: Ubuntu Linux (SSH service)
- Attack activity generates failed authentication logs
- Logs ingested and analyzed in Splunk

---

## Log Source & Ingestion
- Log source: `/var/log/auth.log`
- Events collected by Splunk Universal Forwarder
- Failed SSH authentication attempts indexed in Splunk

This mirrors real-world Linux authentication monitoring in SOC environments.

---

## Detection Logic (Splunk)
Splunk search used to identify brute force behavior:

- Multiple failed SSH login attempts
- Repeated attempts from the same source IP
- Short time window correlation

Detection output includes:
- Attacker IP address
- Number of failed attempts

---

## Alert Triage & SOAR-Lite Automation
Detection results are exported from Splunk as a CSV file and processed using a **Python automation script**.

### Automation Capabilities
- Parses Splunk-exported CSV
- Evaluates failed login count per IP
- Assigns severity:
  - Low
  - Medium
  - High
- Generates analyst-style findings

This simulates **SOAR-lite alert triage**, reducing manual analyst effort.

---

## Noise vs Risk Decision Making
Not all failed logins are incidents.

The automation applies logic to distinguish:
- Benign authentication failures (noise)
- Suspicious repeated attempts
- Clear brute force activity requiring escalation

This reflects how SOC analysts prioritize alerts in production environments.

---

## Threat Intelligence Enrichment
Detected attacker IPs are enriched using **AbuseIPDB** to:
- Validate malicious reputation
- Reduce false positives
- Add external context to alerts

This step improves confidence before escalation.

---

## Analyst Actions & Response
Based on severity and enrichment:
- Alerts are documented
- Risk is assessed
- Escalation recommendations are generated

This reflects SOC analyst communication and response workflow.

---

## Repository Contents
- `README.md` – Project documentation
- `soar_ssh.py` – Python SOAR-lite automation script
- `SOAR-Lite-SSH-Bruteforce-Report.pdf` – SOC-style investigation report
- `screenshots/` – Evidence of detection, automation, and enrichment
- `.csv file` - file that is taken from Splunk

---

## Key Skills Demonstrated
- SOC monitoring & log analysis
- Splunk detection engineering
- SSH authentication security
- Python automation for SOC
- SOAR-lite triage logic
- Threat intelligence enrichment
- Incident decision making

---




