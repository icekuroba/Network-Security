from pathlib import Path

BEFORE_SCAN = Path("scans/before-hardening.txt")
AFTER_SCAN = Path("scans/after-hardening.txt")
REPORT = Path("reports/hardening-report.md")


def extract_open_ports(scan_file):
    open_ports = []

    if not scan_file.exists():
        return open_ports

    with open(scan_file, "r", encoding="utf-8") as file:
        for line in file:
            if "/tcp" in line and "open" in line:
                open_ports.append(line.strip())

    return open_ports


def main():
    before_ports = extract_open_ports(BEFORE_SCAN)
    after_ports = extract_open_ports(AFTER_SCAN)

    reduced_ports = [port for port in before_ports if port not in after_ports]

    report_lines = [
        "# Attack Defense Detection Lab - Hardening Report",
        "",
        "## Objective",
        "",
        "Compare exposed services before and after applying basic hardening.",
        "",
        "## Before Hardening",
        "",
    ]

    if before_ports:
        for port in before_ports:
            report_lines.append(f"- {port}")
    else:
        report_lines.append("- No open ports detected.")

    report_lines.extend([
        "",
        "## After Hardening",
        "",
    ])

    if after_ports:
        for port in after_ports:
            report_lines.append(f"- {port}")
    else:
        report_lines.append("- No open ports detected.")

    report_lines.extend([
        "",
        "## Reduced Exposure",
        "",
    ])

    if reduced_ports:
        for port in reduced_ports:
            report_lines.append(f"- {port}")
    else:
        report_lines.append("- No reduced exposure detected or scans are identical.")

    report_lines.extend([
        "",
        "## Conclusion",
        "",
        "The lab demonstrates how reducing service exposure helps decrease the attack surface of a host."
    ])

    REPORT.parent.mkdir(parents=True, exist_ok=True)

    with open(REPORT, "w", encoding="utf-8") as file:
        file.write("\n".join(report_lines))

    print("Hardening report generated.")
    print(f"Before open ports: {len(before_ports)}")
    print(f"After open ports: {len(after_ports)}")
    print(f"Report: {REPORT}")


if __name__ == "__main__":
    main()
