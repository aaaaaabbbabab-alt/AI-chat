# Sentinel-AI: Network Scanner & AI Vulnerability Analyzer
# Developed by: Abdulaziz (https://github.com/YourUsername)

import socket
import g4f
import sys
import time

class SentinelAI:
    def __init__(self):
        self.version = "1.0.0"
        self.target = ""
        self.open_ports = []
        self.common_ports = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
            53: "DNS", 80: "HTTP", 443: "HTTPS", 3306: "MySQL",
            8080: "HTTP-Proxy"
        }

    def banner(self):
        print(f"""
        [!] Sentinel-AI v{self.version}
        [!] AI-Powered Security Scanner
        [!] Developed by Abdulaziz
        ---------------------------------
        """)

    def scan(self, target):
        self.target = target
        print(f"[*] Initializing scan on {target}...")
        for port, service in self.common_ports.items():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Found Open Port: {port} ({service})")
                self.open_ports.append(f"{port}/{service}")
            s.close()

    def analyze_with_ai(self):
        if not self.open_ports:
            return "No vulnerabilities detected (No open ports found)."
        
        print("[*] Sending data to AI for security analysis...")
        prompt = f"Analyze the following open ports for security risks: {self.open_ports}. Provide a brief report and fix recommendations."
        
        try:
            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_turbo,
                messages=[{"role": "user", "content": prompt}]
            )
            return response
        except Exception as e:
            return f"AI Analysis failed: {e}"

if __name__ == "__main__":
    tool = SentinelAI()
    tool.banner()
    target_ip = input("Enter Target IP/Domain: ")
    tool.scan(target_ip)
    print("\n[#] AI Security Insights:")
    print(tool.analyze_with_ai())
