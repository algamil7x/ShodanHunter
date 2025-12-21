#!/usr/bin/env python3
"""
ShodanHunter - Multi-Technology Vulnerability Scanner
Hunt for vulnerabilities across multiple technologies using Shodan API
GitHub: https://github.com/algamil7x/ShodanHunter
"""

import shodan
import sys
import time
import os
import glob
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""{Fore.CYAN}
 _____ _               _             _   _             _            
/  ___| |             | |           | | | |           | |           
\ `--.| |__   ___   __| | __ _ _ __ | |_| |_   _ _ __ | |_ ___ _ __ 
 `--. \ '_ \ / _ \ / _` |/ _` | '_ \|  _  | | | | '_ \| __/ _ \ '__|
/\__/ / | | | (_) | (_| | (_| | | | | | | | |_| | | | | ||  __/ |   
\____/|_| |_|\___/ \__,_|\__,_|_| |_\_| |_/\__,_|_| |_|\__\___|_|   

{Fore.GREEN}[+] ShodanHunter v1.0 - Multi-Technology Scanner
{Fore.YELLOW}[*] Technologies: Citrix, Jenkins, GitLab, Jira, Confluence, WordPress, Apache, Grafana, Kibana
{Fore.CYAN}[*] GitHub: https://github.com/algamil7x/ShodanHunter
{Style.RESET_ALL}"""

USAGE = f"""{Fore.YELLOW}
Usage Examples:
  # List available technologies
  python3 shodanhunter.py -list
  
  # Scan single technology
  python3 shodanhunter.py -tech citrix -d target.com -o results.txt
  
  # Scan all technologies
  python3 shodanhunter.py -tech all -d target.com -o results.txt
  
  # Use custom query file
  python3 shodanhunter.py -qf queries/citrix.txt -d target.com -o results.txt
{Style.RESET_ALL}"""

AVAILABLE_TECH = {
    'citrix': 'queries/citrix.txt',
    'jenkins': 'queries/jenkins.txt',
    'gitlab': 'queries/gitlab.txt',
    'jira': 'queries/jira.txt',
    'confluence': 'queries/confluence.txt',
    'wordpress': 'queries/wordpress.txt',
    'apache': 'queries/apache.txt',
    'grafana': 'queries/grafana.txt',
    'kibana': 'queries/kibana.txt',
    'exposed': 'queries/exposed.txt',
}

class ShodanHunter:
    def __init__(self, api_key):
        self.api = shodan.Shodan(api_key)
        self.results = set()
        
    def search_query(self, query, domain):
        full_query = f"{query} hostname:*.{domain}"
        
        try:
            print(f"{Fore.YELLOW}[*] Searching: {query}{Style.RESET_ALL}")
            results = self.api.search(full_query, limit=100)
            
            total = results.get('total', 0)
            print(f"{Fore.CYAN}    Total available: {total}{Style.RESET_ALL}")
            
            count = 0
            for result in results['matches']:
                hostnames = result.get('hostnames', [])
                port = result.get('port', 443)
                
                for hostname in hostnames:
                    if domain in hostname:
                        url = f"https://{hostname}:{port}" if port != 443 else f"https://{hostname}"
                        
                        if url not in self.results:
                            self.results.add(url)
                            count += 1
                            print(f"{Fore.GREEN}    [+] Found: {url}{Style.RESET_ALL}")
            
            print(f"{Fore.GREEN}    ✓ Query complete: {count} unique URLs added{Style.RESET_ALL}\n")
            return count
            
        except shodan.APIError as e:
            print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")
            return 0
        except Exception as e:
            print(f"{Fore.RED}[-] Unexpected error: {e}{Style.RESET_ALL}")
            return 0
    
    def hunt(self, queries_file, domain, output_file):
        print(f"{Fore.CYAN}[*] Starting hunt on: *.{domain}")
        print(f"[*] Loading queries from: {queries_file}\n{Style.RESET_ALL}")
        
        try:
            with open(queries_file, 'r') as f:
                queries = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        except FileNotFoundError:
            print(f"{Fore.RED}[-] File not found: {queries_file}{Style.RESET_ALL}")
            return
        
        print(f"{Fore.CYAN}Loaded {len(queries)} queries from {queries_file}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Output will be saved to: {output_file}\n{Style.RESET_ALL}")
        
        query_num = 1
        for query in queries:
            print(f"{Fore.CYAN}[{query_num}/{len(queries)}] Domain: {domain} | Query: {query}{Style.RESET_ALL}")
            self.search_query(query, domain)
            query_num += 1
            time.sleep(1)
        
        print(f"{Fore.GREEN}✓ All queries complete: {len(self.results)} total unique URLs{Style.RESET_ALL}\n")
        self.save_results(output_file)
    
    def save_results(self, output_file):
        print(f"{Fore.GREEN}✓ Completed! Found {len(self.results)} unique URLs. Saved to {output_file}{Style.RESET_ALL}")
        
        with open(output_file, 'w') as f:
            for url in sorted(self.results):
                f.write(url + '\n')
        
        print(f"\n{Fore.YELLOW}=== RESULTS SUMMARY ==={Style.RESET_ALL}")
        print(f"{Fore.CYAN}Total URLs: {len(self.results)}{Style.RESET_ALL}\n")
        for url in sorted(self.results):
            print(url)

def list_technologies():
    print(f"\n{Fore.CYAN}=== Available Technologies ==={Style.RESET_ALL}\n")
    for tech, path in AVAILABLE_TECH.items():
        print(f"{Fore.GREEN}  {tech:<15} {Fore.YELLOW}→ {path}{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}Use: python3 shodanhunter.py -tech <technology> -d target.com -o output.txt{Style.RESET_ALL}\n")

def main():
    print(BANNER)
    
    if '-list' in sys.argv or '--list' in sys.argv:
        list_technologies()
        sys.exit(0)
    
    if len(sys.argv) < 5:
        print(USAGE)
        sys.exit(1)
    
    queries_file = None
    domain = None
    output_file = None
    tech = None
    
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-qf' and i + 1 < len(sys.argv):
            queries_file = sys.argv[i + 1]
        elif sys.argv[i] == '-tech' and i + 1 < len(sys.argv):
            tech = sys.argv[i + 1].lower()
        elif sys.argv[i] == '-d' and i + 1 < len(sys.argv):
            domain = sys.argv[i + 1]
        elif sys.argv[i] == '-o' and i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]
    
    if tech and tech in AVAILABLE_TECH:
        queries_file = AVAILABLE_TECH[tech]
    
    if not all([queries_file, domain, output_file]):
        print(f"{Fore.RED}[-] Missing required arguments{Style.RESET_ALL}")
        print(USAGE)
        sys.exit(1)
    
    api_key = os.environ.get('SHODAN_API_KEY')
    if not api_key:
        print(f"{Fore.RED}[-] SHODAN_API_KEY environment variable not set{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Set it with: export SHODAN_API_KEY='your_key_here'{Style.RESET_ALL}")
        sys.exit(1)
    
    hunter = ShodanHunter(api_key)
    hunter.hunt(queries_file, domain, output_file)

if __name__ == "__main__":
    main()
