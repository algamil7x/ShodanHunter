#!/usr/bin/env python3
"""
ShodanHunter - Multi-Technology Shodan Hunting Tool
Author: algamil7x
"""

import shodan
import sys
import time
import os
import logging
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# =====================
# Banner
# =====================
BANNER = rf"""{Fore.CYAN}
 _____ _               _             _   _             _
/  ___| |             | |           | | | |           | |
\ `--.| |__   ___   __| | __ _ _ __ | |_| |_   _ _ __ | |_ ___ _ __
 `--. \ '_ \ / _ \ / _` |/ _` | '_ \|  _  | | | | '_ \| __/ _ \ '__|
/\__/ / | | | (_) | (_| | (_| | | | | | | | |_| | | | | ||  __/ |
\____/|_| |_|\___/ \__,_|\__,_|_| |_|\_| |_/\__,_|_| |_|\__\___|_|

{Fore.GREEN}[+] ShodanHunter by algamil7x
{Fore.YELLOW}[*] Advanced Shodan Hunting Tool (PRO / Academic Required)
{Fore.CYAN}[*] https://github.com/algamil7x/ShodanHunter
{Style.RESET_ALL}"""

# =====================
# Available Technologies
# =====================
AVAILABLE_TECH = {
    "citrix": "queries/citrix.txt",
    "jenkins": "queries/jenkins.txt",
    "gitlab": "queries/gitlab.txt",
    "jira": "queries/jira.txt",
    "confluence": "queries/confluence.txt",
    "wordpress": "queries/wordpress.txt",
    "apache": "queries/apache.txt",
    "grafana": "queries/grafana.txt",
    "kibana": "queries/kibana.txt",
    "exposed": "queries/exposed.txt",
}

# =====================
# Logging Setup
# =====================
def setup_logging(output_dir):
    log_file = os.path.join(output_dir, "shodanhunter.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )

    return logging.getLogger("ShodanHunter")


# =====================
# Core Class
# =====================
class ShodanHunter:
    def __init__(self, api_key, logger):
        self.api = shodan.Shodan(api_key)
        self.logger = logger

    def search_query(self, query, domain, results_set):
        full_query = f"{query} hostname:*.{domain}"
        self.logger.info(f"Searching: {query}")

        try:
            results = self.api.search(full_query, limit=100)
            total = results.get("total", 0)
            self.logger.info(f"Total available results: {total}")

            for result in results.get("matches", []):
                port = result.get("port", 443)
                for hostname in result.get("hostnames", []):
                    if domain in hostname:
                        url = f"https://{hostname}:{port}" if port != 443 else f"https://{hostname}"
                        results_set.add(url)

        except shodan.APIError as e:
            self.logger.error(f"Shodan API error: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")

    def hunt(self, tech_name, queries_file, domain, output_dir):
        self.logger.info(f"Starting hunt for tech: {tech_name}")
        self.logger.info(f"Using queries file: {queries_file}")

        try:
            with open(queries_file, "r") as f:
                queries = [q.strip() for q in f if q.strip() and not q.startswith("#")]
        except FileNotFoundError:
            self.logger.error(f"Query file not found: {queries_file}")
            return

        results = set()

        for idx, query in enumerate(queries, 1):
            self.logger.info(f"[{idx}/{len(queries)}] {query}")
            self.search_query(query, domain, results)
            time.sleep(1)

        output_file = os.path.join(output_dir, f"{tech_name}.txt")
        with open(output_file, "w") as f:
            for url in sorted(results):
                f.write(url + "\n")

        self.logger.info(f"Saved {len(results)} results to {output_file}")


# =====================
# Helpers
# =====================
def list_technologies():
    print(f"\n{Fore.CYAN}Available Technologies:{Style.RESET_ALL}\n")
    for tech in AVAILABLE_TECH:
        print(f"  - {tech}")
    print()


# =====================
# Main
# =====================
def main():
    print(BANNER)

    if "-list" in sys.argv or "--list" in sys.argv:
        list_technologies()
        sys.exit(0)

    domain = None
    tech = None
    query_file = None

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-d" and i + 1 < len(sys.argv):
            domain = sys.argv[i + 1]
        elif sys.argv[i] == "-tech" and i + 1 < len(sys.argv):
            tech = sys.argv[i + 1].lower()
        elif sys.argv[i] == "-qf" and i + 1 < len(sys.argv):
            query_file = sys.argv[i + 1]

    if not domain or (not tech and not query_file):
        print(f"{Fore.RED}[-] Missing required arguments{Style.RESET_ALL}")
        print("Usage:")
        print("  python3 shodanhunter.py -tech citrix -d target.com")
        print("  python3 shodanhunter.py -tech all -d target.com")
        print("  python3 shodanhunter.py -qf queries/exposed.txt -d target.com")
        sys.exit(1)

    api_key = os.environ.get("SHODAN_API_KEY")
    if not api_key:
        print(f"{Fore.RED}[-] SHODAN_API_KEY not set{Style.RESET_ALL}")
        sys.exit(1)

    # Create output directory per run
    output_dir = os.path.join("output", domain)
    os.makedirs(output_dir, exist_ok=True)

    logger = setup_logging(output_dir)
    hunter = ShodanHunter(api_key, logger)

    if query_file:
        hunter.hunt("custom", query_file, domain, output_dir)
    else:
        if tech == "all":
            for tech_name, qf in AVAILABLE_TECH.items():
                hunter.hunt(tech_name, qf, domain, output_dir)
        elif tech in AVAILABLE_TECH:
            hunter.hunt(tech, AVAILABLE_TECH[tech], domain, output_dir)
        else:
            logger.error(f"Unknown technology: {tech}")
            sys.exit(1)

    logger.info("Hunting completed successfully")


if __name__ == "__main__":
    main()

