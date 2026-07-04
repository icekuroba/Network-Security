import re
from collections import Counter, defaultdict
from pathlib import Path


SUSPICIOUS_PATHS = [
    "/admin",
    "/wp-admin",
    "/.env",
    "/etc/passwd",
    "/phpmyadmin",
    "/login.php",
    "/config.php",
]

SSH_FAILED_THRESHOLD = 5
WEB_404_THRESHOLD = 5


def add_finding(findings, severity, source, event_type, message, recommendation):
    findings.append({
        "severity": severity,
        "source": source,
        "event_type": event_type,
        "message": message,
        "recommendation": recommendation
    })


def analyze_auth_log(path):
    findings = []

    if not Path(path).exists():
        return findings

    failed_ssh_ips = Counter()

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if "Failed password" in line:
                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    failed_ssh_ips[match.group(1)] += 1

    for ip, count in failed_ssh_ips.items():
        if count >= SSH_FAILED_THRESHOLD:
            add_finding(
                findings,
                "HIGH",
                ip,
                "SSH brute force attempt",
                f"{count} failed SSH login attempts detected from {ip}.",
                "Restrict SSH access, use key-based authentication, and consider fail2ban or firewall rules."
            )
        else:
            add_finding(
                findings,
                "MEDIUM",
                ip,
                "Failed SSH login",
                f"{count} failed SSH login attempt(s) detected from {ip}.",
                "Monitor repeated failures and restrict SSH to trusted IPs."
            )

    return findings


def analyze_nginx_log(path):
    findings = []

    if not Path(path).exists():
        return findings

    suspicious_hits = defaultdict(list)
    error_404_count = Counter()

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            ip_match = re.match(r"(\d+\.\d+\.\d+\.\d+)", line)
            request_match = re.search(r'"[A-Z]+ ([^ ]+) HTTP', line)
            status_match = re.search(r'" (\d{3}) ', line)

            if not ip_match or not request_match:
                continue

            ip = ip_match.group(1)
            requested_path = request_match.group(1)

            if status_match and status_match.group(1) == "404":
                error_404_count[ip] += 1

            for suspicious_path in SUSPICIOUS_PATHS:
                if requested_path.startswith(suspicious_path):
                    suspicious_hits[ip].append(requested_path)

    for ip, paths in suspicious_hits.items():
        add_finding(
            findings,
            "HIGH",
            ip,
            "Suspicious web probing",
            f"Suspicious web paths requested by {ip}: {', '.join(sorted(set(paths)))}.",
            "Review web logs, block abusive IPs, and ensure sensitive files are not publicly exposed."
        )

    for ip, count in error_404_count.items():
        if count >= WEB_404_THRESHOLD:
            add_finding(
                findings,
                "MEDIUM",
                ip,
                "Multiple 404 errors",
                f"{count} HTTP 404 responses detected from {ip}.",
                "Investigate possible directory brute forcing or automated scanning."
            )

    return findings


def analyze_ufw_log(path):
    findings = []

    if not Path(path).exists():
        return findings

    blocked_by_ip = Counter()
    blocked_ports = defaultdict(list)

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if "[UFW BLOCK]" in line:
                src_match = re.search(r"SRC=(\d+\.\d+\.\d+\.\d+)", line)
                dpt_match = re.search(r"DPT=(\d+)", line)

                if src_match:
                    ip = src_match.group(1)
                    blocked_by_ip[ip] += 1

                    if dpt_match:
                        blocked_ports[ip].append(dpt_match.group(1))

    for ip, count in blocked_by_ip.items():
        ports = ", ".join(sorted(set(blocked_ports[ip])))

        add_finding(
            findings,
            "MEDIUM",
            ip,
            "Firewall blocked traffic",
            f"{count} blocked connection attempt(s) from {ip}. Target port(s): {ports}.",
            "Review firewall logs and consider blocking repeated suspicious sources."
        )

    return findings


def analyze_all_logs(auth_log, nginx_log, ufw_log):
    findings = []
    findings.extend(analyze_auth_log(auth_log))
    findings.extend(analyze_nginx_log(nginx_log))
    findings.extend(analyze_ufw_log(ufw_log))
    return findings


def count_by_severity(findings):
    counts = Counter(finding["severity"] for finding in findings)

    return {
        "HIGH": counts.get("HIGH", 0),
        "MEDIUM": counts.get("MEDIUM", 0),
        "LOW": counts.get("LOW", 0),
        "INFO": counts.get("INFO", 0),
    }
