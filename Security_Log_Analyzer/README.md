# Security Log Analyzer

Security Log Analyzer is a Python-based cybersecurity project that analyzes sample security logs and detects suspicious activity related to authentication, web probing, and firewall-blocked traffic.

The project demonstrates a basic blue team workflow:

```text
Collect logs -> Parse events -> Detect suspicious activity -> Classify severity -> Generate reports
```

## Objectives

- Analyze authentication logs for failed SSH login attempts.
- Detect possible SSH brute force activity.
- Analyze Nginx access logs for suspicious web probing.
- Detect repeated HTTP 404 errors from the same source.
- Analyze UFW firewall logs for blocked connection attempts.
- Generate Markdown and CSV reports with security findings.
- Practice log analysis, detection logic, and defensive documentation.

## Tools Used

- Ubuntu Linux
- Python 3
- Sample Linux authentication logs
- Sample Nginx access logs
- Sample UFW firewall logs
- Git/GitHub

## Project Structure

```text
Security_Log_Analyzer/
├── README.md
├── data/
│   ├── sample_auth.log
│   ├── sample_nginx_access.log
│   └── sample_ufw.log
├── src/
│   ├── analyzer.py
│   ├── report.py
│   └── main.py
├── reports/
│   ├── security-log-report.md
│   └── security-log-findings.csv
├── docs/
│   ├── detection-rules.md
│   └── sample-incidents.md
└── screenshots/
```

## Detection Logic

The analyzer currently detects:

| Detection Type | Log Source | Severity |
|---|---|---|
| SSH brute force attempt | auth.log | HIGH |
| Suspicious web probing | Nginx access.log | HIGH |
| Multiple HTTP 404 errors | Nginx access.log | MEDIUM |
| Firewall blocked traffic | UFW log | MEDIUM |

## Sample Findings

Example output:

```text
HIGH - SSH brute force attempt
5 failed SSH login attempts detected from 192.168.56.20.

HIGH - Suspicious web probing
Suspicious web paths requested by 192.168.56.44: /.env, /admin, /etc/passwd, /phpmyadmin, /wp-admin.

MEDIUM - Firewall blocked traffic
Blocked connection attempts detected against ports 22, 3389, and 3306.
```

## How to Run

From the project root:

```bash
python3 src/main.py
```

Expected output:

```text
Security Log Analyzer completed.
Findings detected: 5
High severity: 2
Medium severity: 3
Markdown report: reports/security-log-report.md
CSV report: reports/security-log-findings.csv
```

## Generated Reports

The project generates two reports:

```text
reports/security-log-report.md
reports/security-log-findings.csv
```

The Markdown report is useful for documentation.  
The CSV report is useful for filtering, analysis, or importing into other tools.

## Defensive Value

This project demonstrates how basic log analysis can help identify suspicious behavior such as:

- Repeated SSH login failures.
- Web directory probing.
- Attempts to access sensitive files.
- Repeated firewall-blocked connections.
- Suspicious source IP activity.

These detections are useful for blue team workflows, SOC analyst practice, and defensive security documentation.

## Future Improvements

- Add support for real `/var/log/auth.log` files.
- Add CLI arguments for custom log paths.
- Add JSON output.
- Add severity scoring.
- Add timestamp extraction.
- Add top source IP summary.
- Add Streamlit dashboard.
- Add MITRE ATT&CK mapping.
- Add support for Apache logs.
- Add support for Windows event logs.

## Security Note

This project uses sample logs for educational and authorized lab environments only.
