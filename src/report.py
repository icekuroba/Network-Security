import csv
from pathlib import Path


def generate_markdown_report(findings, severity_counts, output_path):
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Security Log Analyzer Report",
        "",
        "## Summary",
        "",
        f"- Total findings: {len(findings)}",
        f"- High severity: {severity_counts.get('HIGH', 0)}",
        f"- Medium severity: {severity_counts.get('MEDIUM', 0)}",
        f"- Low severity: {severity_counts.get('LOW', 0)}",
        f"- Informational: {severity_counts.get('INFO', 0)}",
        "",
        "## Findings",
        "",
    ]

    if not findings:
        lines.append("No suspicious events were detected.")
    else:
        for index, finding in enumerate(findings, start=1):
            lines.extend([
                f"### Finding {index}: {finding['event_type']}",
                "",
                f"- Severity: {finding['severity']}",
                f"- Source: {finding['source']}",
                f"- Message: {finding['message']}",
                f"- Recommendation: {finding['recommendation']}",
                "",
            ])

    lines.extend([
        "## Defensive Value",
        "",
        "This report helps identify suspicious authentication activity, web probing, and firewall-blocked traffic from sample security logs.",
        "",
        "## Security Note",
        "",
        "This project uses sample logs for educational and authorized lab environments only."
    ])

    output.write_text("\n".join(lines), encoding="utf-8")


def generate_csv_report(findings, output_path):
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = ["severity", "source", "event_type", "message", "recommendation"]

    with open(output, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(findings)
