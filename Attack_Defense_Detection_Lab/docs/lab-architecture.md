# Lab Architecture

This lab runs on an Ubuntu virtual machine.

Architecture:

Ubuntu VM
├── Docker
│   └── Nginx test service
├── Nmap scans
├── Python report generator
└── Markdown documentation

The exposed version binds Nginx to 0.0.0.0:8080.

The hardened version binds Nginx to 127.0.0.1:8080.
