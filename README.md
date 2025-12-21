# 🔍 ShodanHunter

**Multi-Technology Vulnerability Scanner for Bug Bounty Hunting**

Hunt for vulnerabilities across multiple technologies using Shodan API. Perfect for bug bounty hunters and security researchers.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Shodan](https://img.shields.io/badge/Powered%20by-Shodan-red.svg)](https://shodan.io)

---

## ✨ Features

- 🎯 **10+ Technologies**: Citrix, Jenkins, GitLab, Jira, Confluence, WordPress, Apache Tomcat, Grafana, Kibana, Exposed Files
- 🚀 **Fast Scanning**: Concurrent searching with intelligent rate limiting
- 📊 **Organized Queries**: Technology-specific query files for precision
- 💾 **Clean Output**: Deduplicated results ready for Nuclei scanning
- 🎨 **Beautiful UI**: Colored terminal output for better readability
- 🔧 **Extensible**: Easy to add new technologies

---

## 🛠️ Installation

### Quick Start
```bash
# Clone repository
git clone https://github.com/algamil7x/ShodanHunter.git
cd ShodanHunter

# Install dependencies
pip3 install -r requirements.txt

# Set Shodan API Key
export SHODAN_API_KEY="your_api_key_here"

# Make executable
chmod +x shodanhunter.py

# Verify installation
python3 shodanhunter.py -list
```

### Getting Shodan API Key

1. Register at [Shodan](https://account.shodan.io/register)
2. Get your API key from [account page](https://account.shodan.io)
3. Free tier: 100 queries/month
4. Paid tier: Unlimited queries ($49/month)

---

## 📖 Usage

### List Available Technologies
```bash
python3 shodanhunter.py -list
```

### Scan Single Technology
```bash
python3 shodanhunter.py -tech citrix -d target.com -o results.txt
```

### Scan All Technologies
```bash
python3 shodanhunter.py -tech all -d target.com -o results.txt
```

### Use Custom Query File
```bash
python3 shodanhunter.py -qf queries/citrix.txt -d target.com -o results.txt
```

---

## 🎯 Supported Technologies

| Technology | Query File | Known CVEs | Bug Bounty Popular |
|-----------|-----------|-----------|-------------------|
| Citrix Gateway | citrix.txt | 50+ | ⭐⭐⭐ |
| Jenkins | jenkins.txt | 100+ | ⭐⭐⭐ |
| GitLab | gitlab.txt | 80+ | ⭐⭐⭐ |
| Atlassian Jira | jira.txt | 60+ | ⭐⭐ |
| Confluence | confluence.txt | 70+ | ⭐⭐ |
| Apache Tomcat | apache.txt | 90+ | ⭐⭐ |
| WordPress | wordpress.txt | 200+ | ⭐⭐⭐ |
| Grafana | grafana.txt | 40+ | ⭐⭐ |
| Kibana | kibana.txt | 30+ | ⭐ |
| Exposed Files | exposed.txt | N/A | ⭐⭐⭐ |

---

## 🔗 Integration with Nuclei

Perfect workflow for bug bounty:
```bash
# Step 1: Hunt with ShodanHunter
python3 shodanhunter.py -tech citrix -d target.com -o targets.txt

# Step 2: Scan with Nuclei
cat targets.txt | nuclei -tags citrix,xss -severity high,critical -o vulns.txt

# Step 3: Review vulnerabilities
cat vulns.txt
```

---

## 📁 Project Structure
```
ShodanHunter/
├── shodanhunter.py          # Main tool
├── requirements.txt         # Python dependencies
├── README.md                # This file
├── queries/                 # Query files directory
│   ├── citrix.txt          # Citrix/NetScaler queries
│   ├── jenkins.txt         # Jenkins queries
│   ├── gitlab.txt          # GitLab queries
│   ├── jira.txt            # Jira queries
│   ├── confluence.txt      # Confluence queries
│   ├── wordpress.txt       # WordPress queries
│   ├── apache.txt          # Apache Tomcat queries
│   ├── grafana.txt         # Grafana queries
│   ├── kibana.txt          # Kibana queries
│   └── exposed.txt         # Exposed files queries
├── examples/               # Example outputs
│   └── demo_output.txt
└── docs/                   # Documentation
    ├── INSTALLATION.md
    └── CONTRIBUTING.md
```

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details.

### Quick Contribution Guide

1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewTech`)
3. Add queries to `queries/newtech.txt`
4. Update `AVAILABLE_TECH` in `shodanhunter.py`
5. Commit changes (`git commit -m 'Add NewTech support'`)
6. Push to branch (`git push origin feature/NewTech`)
7. Open Pull Request

---

## ⚠️ Disclaimer

**For educational and authorized security testing only.**

- ✅ Use only on bug bounty programs with permission
- ✅ Read and follow program scope carefully
- ❌ Do NOT use on unauthorized targets
- ❌ Do NOT abuse Shodan API

The authors are not responsible for misuse of this tool.

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

---

## 🙏 Acknowledgments

- Inspired by real-world bug bounty hunting workflows
- Built for the security community
- Powered by [Shodan](https://shodan.io)
- Thanks to all contributors

---

## 📞 Contact
- **Twitter/X**: [@algamil7x](https://x.com/algamil7x)
- **GitHub**: [@algamil7x](https://github.com/algamil7x)
- **Issues**: [Report bugs](https://github.com/algamil7x/ShodanHunter/issues)
- **Pull Requests**: [Contribute](https://github.com/algamil7x/ShodanHunter/pulls)

---

**Happy Hunting! 🎯🔥**

Made with ❤️ by Bug Bounty Hunters, for Bug Bounty Hunters
