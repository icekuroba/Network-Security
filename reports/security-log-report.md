# Security Log Analyzer Report

## Summary

- Total findings: 5
- High severity: 2
- Medium severity: 3
- Low severity: 0
- Informational: 0

## Findings

### Finding 1: SSH brute force attempt

- Severity: HIGH
- Source: 192.168.56.20
- Message: 5 failed SSH login attempts detected from 192.168.56.20.
- Recommendation: Restrict SSH access, use key-based authentication, and consider fail2ban or firewall rules.

### Finding 2: Suspicious web probing

- Severity: HIGH
- Source: 192.168.56.44
- Message: Suspicious web paths requested by 192.168.56.44: /.env, /admin, /etc/passwd, /phpmyadmin, /wp-admin.
- Recommendation: Review web logs, block abusive IPs, and ensure sensitive files are not publicly exposed.

### Finding 3: Multiple 404 errors

- Severity: MEDIUM
- Source: 192.168.56.44
- Message: 5 HTTP 404 responses detected from 192.168.56.44.
- Recommendation: Investigate possible directory brute forcing or automated scanning.

### Finding 4: Firewall blocked traffic

- Severity: MEDIUM
- Source: 192.168.56.60
- Message: 2 blocked connection attempt(s) from 192.168.56.60. Target port(s): 22, 3389.
- Recommendation: Review firewall logs and consider blocking repeated suspicious sources.

### Finding 5: Firewall blocked traffic

- Severity: MEDIUM
- Source: 192.168.56.61
- Message: 1 blocked connection attempt(s) from 192.168.56.61. Target port(s): 3306.
- Recommendation: Review firewall logs and consider blocking repeated suspicious sources.

## Defensive Value

This report helps identify suspicious authentication activity, web probing, and firewall-blocked traffic from sample security logs.

## Security Note

This project uses sample logs for educational and authorized lab environments only.