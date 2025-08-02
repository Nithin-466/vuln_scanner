import nmap  # Import the nmap library

# Ask the user to enter the target IP address
target = input("Enter the target IP address to scan (e.g. 192.168.1.10): ")

# Create the Nmap scanner object
scanner = nmap.PortScanner()

# Run a basic port scan with service detection
print(f"\n[+] Scanning {target} for open ports and service versions...\n")
scanner.scan(target, '1-1024', '-sV')

# Vulnerability database (dictionary of known bad versions)
vuln_db = {
    "ftp 2.3.4": "CVE-2011-2523 - vsftpd backdoor",
    "http 2.4.49": "CVE-2021-41773 - Apache Path Traversal",
    "http 2.4.50": "CVE-2021-42013 - Apache RCE",
    "http 2.2.8": "CVE-2009-1891 - mod_proxy reverse proxy DoS",
    "ssh 7.2p2": "CVE-2016-0777 - OpenSSH Info Leak",
    "ssh 5.3": "CVE-2010-4478 - OpenSSH privilege escalation",
    "mysql 5.5.20": "CVE-2012-2122 - MySQL authentication bypass",
    "mysql 5.1.73": "CVE-2013-1860 - DoS via COM_TABLE_DUMP",
    "postgresql 8.3": "CVE-2007-3278 - SQL Injection",
    "telnet 1.2": "CVE-2005-0469 - Telnet Remote Buffer Overflow",
    "samba 3.6.3": "CVE-2012-1182 - Remote Code Execution",
    "samba 4.7.5": "CVE-2018-1050 - DoS vulnerability",
    "dnsmasq 2.78": "CVE-2017-14491 - Heap buffer overflow",
    "rpcbind 0.2.3": "CVE-2017-8779 - Remote DoS",
    "apache 2.2.22": "CVE-2012-0053 - mod_log_config buffer overflow",
    "apache 2.4.7": "CVE-2014-0098 - mod_status DoS",
    "nginx 1.3.9": "CVE-2013-2070 - Stack-based Buffer Overflow",
    "http 2.4.63": "DEMO-VULN - Apache version used for testing alert"

}

# Loop through the results of the scan
for host in scanner.all_hosts():
    print(f"\nHost: {host}")
    print(f"State: {scanner[host].state()}")

    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()

        for port in sorted(ports):
            service = scanner[host][proto][port]['name']
            version = scanner[host][proto][port].get('version', 'unknown')
            product = scanner[host][proto][port].get('product', 'unknown')

            print(f"Port {port} | Service: {product} {version}")

            # Check if this version is in the known vulnerability list
            key = f"{service} {version}"
            if key in vuln_db:
                print(f"⚠️  [VULNERABILITY FOUND] {vuln_db[key]}")
