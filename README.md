# 🔍 Vulnerability Scanner (Python + Nmap)

This is a beginner-friendly vulnerability scanner written in Python. It scans a target IP address using Nmap, detects open ports and services, and alerts you if any known vulnerable versions (CVE) are found.

---

## 🚀 How It Works

- Scans ports 1–1024 using `nmap -sV`
- Parses results using the `python-nmap` library
- Matches service version info with a simple vulnerability database (dictionary)
- Alerts if a version is known to be vulnerable

---

## 🧰 Requirements

- Python 3
- Kali Linux or any Linux OS
- Nmap installed:
  ```bash
  sudo apt install nmap
