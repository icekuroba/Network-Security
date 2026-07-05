# Network Security

This repository contains hands-on network security projects focused on defensive security, service exposure validation, firewall hardening, log analysis, detection workflows, and security automation.

The purpose of this repository is to document practical cybersecurity labs that combine networking, Linux, Python, Docker, Nmap, firewall logs, and defensive analysis.

## Focus Areas

- Network security
- Blue team fundamentals
- Log analysis
- Firewall hardening
- Service exposure validation
- Attack surface reduction
- Detection engineering basics
- Security automation with Python
- Incident documentation

## Projects

### 1. Attack Defense Detection Lab

A controlled cybersecurity lab focused on service exposure, Nmap scanning, evidence collection, hardening, and post-mitigation validation.

The lab demonstrates the following workflow:

```text
Expose service -> Scan -> Collect evidence -> Harden -> Re-scan -> Generate report
```

Main topics:

- Docker service exposure
- Nmap scanning
- Network binding hardening
- Before-and-after security validation
- Attack surface reduction
- Markdown reporting

Project folder:

```text
Attack_Defense_Detection_Lab/
```

---

### 2. Security Log Analyzer

A Python-based log analysis tool that detects suspicious activity from sample security logs.

The analyzer reviews authentication logs, Nginx access logs, and UFW firewall logs to identify suspicious behavior.

Detected events include:

- SSH brute force attempts
- Suspicious web probing
- Multiple HTTP 404 errors
- Firewall-blocked traffic

Main topics:

- Python log parsing
- Detection logic
- Severity classification
- CSV report generation
- Markdown report generation
- Blue team investigation workflow

Project folder:

```text
Security_Log_Analyzer/
```

## Repository Structure

```text
Network-Security/
├── Attack_Defense_Detection_Lab/
├── Security_Log_Analyzer/
└── README.md
```

## Tools and Technologies

- Ubuntu Linux
- Python 3
- Docker
- Nginx
- Nmap
- UFW
- Git/GitHub
- Markdown
- CSV reporting

## Purpose

This repository is part of my cybersecurity and network security portfolio.

It is focused on practical labs, defensive analysis, log investigation, and security automation.

## Future Project Ideas

Possible future additions to this repository:

- Firewall Hardening Lab
- Web Application Vulnerability Defense Lab
- Incident Response Simulation Lab
- Network Traffic Analysis Lab
- Basic IDS Detection Rules Lab
- Secure GitHub Pipeline Lab

## Security Note

All projects in this repository are designed for educational and authorized lab environments only.

Do not scan, test, or analyze systems without permission.
