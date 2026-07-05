# Attack Defense Detection Lab

Attack Defense Detection Lab is a controlled cybersecurity lab focused on service exposure, network scanning, evidence collection, hardening, and post-mitigation validation.

The project demonstrates a complete security workflow:

```text
Expose service -> Scan -> Collect evidence -> Harden -> Re-scan -> Generate report
```

This lab uses a Docker-based Nginx service to simulate an exposed network service. Nmap is used to validate exposure before and after applying a basic hardening change.

## Objectives

- Deploy an exposed Nginx service using Docker.
- Identify exposed ports using Nmap.
- Collect scan evidence before and after hardening.
- Reduce service exposure by changing the network binding.
- Compare scan results using a Python script.
- Generate a Markdown hardening report.
- Document the offensive and defensive workflow.

## Tools Used

- Ubuntu Linux
- Docker
- Docker Compose
- Nginx
- Nmap
- Python 3
- Git/GitHub

## Lab Architecture

```text
Ubuntu VM
├── Docker
│   └── Nginx test service
├── Nmap
│   ├── before-hardening scan
│   └── after-hardening scan
├── Python
│   └── scan comparison script
└── Markdown reports
```

## Security Scenario

The lab starts with an Nginx container exposed on all network interfaces:

```text
0.0.0.0:8080 -> 80/tcp
```

This means the service is reachable from the host network interface.

After hardening, the service is bound only to localhost:

```text
127.0.0.1:8080 -> 80/tcp
```

This reduces the exposed attack surface because the service is no longer reachable from the external network interface.

## Project Structure

```text
Attack_Defense_Detection_Lab/
├── docker/
│   └── nginx-lab/
│       ├── docker-compose-exposed.yml
│       ├── docker-compose-hardened.yml
│       └── index.html
├── scans/
│   ├── before-hardening.txt
│   └── after-hardening.txt
├── logs/
├── scripts/
│   └── scan_compare.py
├── reports/
│   └── hardening-report.md
├── docs/
│   ├── lab-architecture.md
│   ├── offensive-phase.md
│   └── defensive-phase.md
└── screenshots/
```

## Lab Phases

### 1. Offensive Phase

A controlled Nmap scan is used to identify exposed services in the lab environment.

The initial scan validates that the Nginx service is reachable through the host network interface.

### 2. Defensive Phase

The exposed service is hardened by changing its Docker network binding.

Instead of exposing the service on all interfaces, the service is restricted to localhost.

### 3. Detection and Reporting

Scan results are compared before and after hardening.

A Python script analyzes the Nmap output files and generates a Markdown report showing the reduced exposure.

## How to Run the Lab

### 1. Start the exposed service

From the project root:

```bash
cd docker/nginx-lab
docker compose -f docker-compose-exposed.yml up -d
```

Verify that the container is running:

```bash
docker ps
```

Expected exposure:

```text
0.0.0.0:8080->80/tcp
```

Test the service locally:

```bash
curl http://localhost:8080
```

### 2. Identify the host IP

```bash
hostname -I
```

Example:

```text
10.0.2.15
```

### 3. Run the before-hardening scan

From the project root:

```bash
cd ~/labs/Network-Security/Attack_Defense_Detection_Lab
nmap -sV -p 22,80,8080 10.0.2.15 -oN scans/before-hardening.txt
```

Expected result:

```text
8080/tcp open http nginx
```

### 4. Apply hardening

Stop the exposed container:

```bash
cd docker/nginx-lab
docker compose -f docker-compose-exposed.yml down
```

Start the hardened container:

```bash
docker compose -f docker-compose-hardened.yml up -d
```

Verify the new binding:

```bash
docker ps
```

Expected exposure:

```text
127.0.0.1:8080->80/tcp
```

The service should still work locally:

```bash
curl http://localhost:8080
```

### 5. Run the after-hardening scan

From the project root:

```bash
cd ~/labs/Network-Security/Attack_Defense_Detection_Lab
nmap -sV -p 22,80,8080 10.0.2.15 -oN scans/after-hardening.txt
```

Expected result:

```text
8080/tcp closed
```

### 6. Generate the hardening report

```bash
python3 scripts/scan_compare.py
```

View the generated report:

```bash
cat reports/hardening-report.md
```

## Results

### Before Hardening

```text
22/tcp   closed ssh
80/tcp   closed http
8080/tcp open   http nginx
```

The Nginx service was exposed through the host network interface.

### After Hardening

```text
22/tcp   closed ssh
80/tcp   closed http
8080/tcp closed http-proxy
```

The service remained available locally through `localhost`, but it was no longer exposed through the host network IP.

## Key Finding

The service was initially exposed on all interfaces using:

```text
0.0.0.0:8080
```

After hardening, it was restricted to localhost:

```text
127.0.0.1:8080
```

This reduced the attack surface by preventing network-level access to the service from the host IP.

## Defensive Value

This lab demonstrates a basic but important defensive concept:

> Services should only be exposed on the network interfaces where they are actually needed.

Limiting service exposure helps reduce unnecessary attack surface and supports secure network design.

## Generated Evidence

This project generates and stores the following evidence:

- `scans/before-hardening.txt`
- `scans/after-hardening.txt`
- `reports/hardening-report.md`

## What I Learned

- How Docker port bindings affect service exposure.
- How to validate exposed services with Nmap.
- How to compare before-and-after hardening results.
- How to document security findings with evidence.
- How small configuration changes can reduce attack surface.

## Future Improvements

- Add UFW firewall hardening.
- Add tcpdump packet capture evidence.
- Add Nginx access log analysis.
- Add failed request detection.
- Add a Python-based log analyzer.
- Add screenshots of scan results.
- Add MITRE ATT&CK or NIST CSF mapping.
- Add a small dashboard for scan comparison.

## Security Note

This project is for educational and authorized lab environments only.

Do not scan public IP addresses or systems without permission.
