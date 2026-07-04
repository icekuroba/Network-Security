# Attack Defense Detection Lab

## Overview

Attack Defense Detection Lab is a controlled cybersecurity lab focused on service exposure, network scanning, evidence collection, hardening, and post-mitigation validation.

The goal is to demonstrate a complete security workflow:

Expose service -> Scan -> Collect evidence -> Harden -> Re-scan -> Generate report

## Objectives

- Deploy an exposed Nginx service using Docker.
- Identify exposed ports using Nmap.
- Apply basic hardening by limiting service exposure.
- Compare scan results before and after hardening.
- Generate a Markdown report with Python.
- Document the defensive process clearly.

## Tools Used

- Ubuntu Linux
- Docker
- Nginx
- Nmap
- Python
- Git/GitHub

## Lab Phases

### 1. Offensive Phase

A controlled Nmap scan is used to identify exposed services.

### 2. Defensive Phase

The exposed service is hardened by changing its network binding.

### 3. Detection and Reporting

Scan results are compared and a hardening report is generated automatically.

## Project Structure

Attack_Defense_Detection_Lab/
├── docker/
│   └── nginx-lab/
├── scans/
├── logs/
├── scripts/
├── reports/
├── docs/
└── screenshots/

## Security Note

This project is for educational and authorized lab environments only.
