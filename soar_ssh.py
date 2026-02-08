import csv
import requests

API_KEY = "913fb8b25a492a4fdfdf944d65cb9559cc8afe2b9bdf29c50bc61f0f4aeaae6a3515677d9afab710"
INPUT_FILE = "soar_lite.csv"

print("\n[+] SOAR Lite Automation Started\n")

with open(INPUT_FILE, newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        ip = row['attacker_ip']
        failures = int(row['failures'])

        print(f"[+] Enriching IP: {ip}")

        url = "https://api.abuseipdb.com/api/v2/check"
        headers = {
            "Key": API_KEY,
            "Accept": "application/json"
        }
        params = {
            "ipAddress": ip,
            "maxAgeInDays": 90
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()["data"]

        abuse_score = data["abuseConfidenceScore"]
        total_reports = data["totalReports"]

        if abuse_score > 50:
            severity = "HIGH"
        elif abuse_score > 20:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        print(f"    Abuse Score   : {abuse_score}")
        print(f"    Total Reports : {total_reports}")
        print(f"    Severity      : {severity}\n")
import csv

INPUT_FILE = "soar_lite.csv"
THRESHOLD = 5

print("\n[+] SOAR Lite Automation Started\n")

with open(INPUT_FILE, newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        attacker_ip = row["attacker_ip"]
        failures = int(row["failures"])

        if failures > THRESHOLD:
            severity = "HIGH"
            action = "Investigate immediately"
        else:
            severity = "LOW"
            action = "Monitor"

        print(f"IP: {attacker_ip} | Failures: {failures} | Severity: {severity} | Action: {action}")

print("\n[+] Automation Completed\n")
