from analyzer import analyze_all_logs, count_by_severity
from report import generate_markdown_report, generate_csv_report


AUTH_LOG = "data/sample_auth.log"
NGINX_LOG = "data/sample_nginx_access.log"
UFW_LOG = "data/sample_ufw.log"

MARKDOWN_REPORT = "reports/security-log-report.md"
CSV_REPORT = "reports/security-log-findings.csv"


def main():
    findings = analyze_all_logs(AUTH_LOG, NGINX_LOG, UFW_LOG)
    severity_counts = count_by_severity(findings)

    generate_markdown_report(findings, severity_counts, MARKDOWN_REPORT)
    generate_csv_report(findings, CSV_REPORT)

    print("Security Log Analyzer completed.")
    print(f"Findings detected: {len(findings)}")
    print(f"High severity: {severity_counts['HIGH']}")
    print(f"Medium severity: {severity_counts['MEDIUM']}")
    print(f"Markdown report: {MARKDOWN_REPORT}")
    print(f"CSV report: {CSV_REPORT}")


if __name__ == "__main__":
    main()
