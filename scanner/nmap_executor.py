import subprocess
import os
from datetime import datetime

class NmapExecutor:
    def __init__(self, output_dir="data"):
        self.output_dir = output_dir

        # Ensure output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def run_scan(self, target):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(self.output_dir, f"scan_{timestamp}.xml")

        command = [
            "nmap",
            "-sS",        # SYN scan
            "-sV",        # Service/version detection
            "-oX", output_file,
            target
        ]

        print(f"\n[+] Running Nmap scan on {target}...\n")

        try:
            subprocess.run(command, check=True)
            print(f"[+] Scan completed successfully")
            print(f"[+] Output saved at: {output_file}")
            return output_file

        except FileNotFoundError:
            print("[-] Nmap is not installed or not found in PATH")
            return None

        except subprocess.CalledProcessError:
            print("[-] Nmap scan failed")
            return None