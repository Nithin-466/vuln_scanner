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
  
 -python-nmap library:
 
    sudo apt install python3-nmap
    
  -How to Run

    python3 vuln_scanner.py
  #Then enter the target IP address (like 127.0.0.1)
 
 -Sample Output

    [+] Scanning 127.0.0.1 for open ports and service versions...

    Host: 127.0.0.1
    State: up
    Port 80 | Service: Apache httpd 2.4.63
    ⚠ [VULNERABILITY FOUND] DEMO-VULN - Apache version used for testing alert 

##  Author

**Nithin-466**  
Cybersecurity student learning ethical hacking and Python automation.
