# 🛠️ Installation Guide

Complete installation guide for ShodanHunter on different operating systems.

---

## 📋 Prerequisites

- Python 3.6 or higher
- pip3 (Python package manager)
- Shodan API Key (get one at https://account.shodan.io)
- Git (for cloning repository)

---

## 🚀 Quick Installation

### Linux / macOS / WSL
```bash
# Clone the repository
git clone https://github.com/algamil7x/ShodanHunter.git
cd ShodanHunter

# Install dependencies
pip3 install -r requirements.txt

# Set your Shodan API Key
export SHODAN_API_KEY="your_api_key_here"

# Make the script executable
chmod +x shodanhunter.py

# Verify installation
python3 shodanhunter.py -list
```

### Windows
```cmd
# Clone the repository
git clone https://github.com/algamil7x/ShodanHunter.git
cd ShodanHunter

# Install dependencies
pip install -r requirements.txt

# Set your Shodan API Key
set SHODAN_API_KEY=your_api_key_here

# Run the tool
python shodanhunter.py -list
```

---

## 🔑 Getting Shodan API Key

### Step 1: Create Account
1. Visit https://account.shodan.io/register
2. Sign up with your email
3. Verify your email address

### Step 2: Get API Key
1. Login to https://account.shodan.io
2. Copy your API key from the dashboard
3. The key looks like: `xxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Step 3: Set API Key

**Linux/macOS/WSL:**
```bash
export SHODAN_API_KEY="your_api_key_here"

# To make it permanent, add to ~/.bashrc or ~/.zshrc:
echo 'export SHODAN_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

**Windows CMD:**
```cmd
set SHODAN_API_KEY=your_api_key_here

# To make it permanent:
setx SHODAN_API_KEY "your_api_key_here"
```

**Windows PowerShell:**
```powershell
$env:SHODAN_API_KEY="your_api_key_here"

# To make it permanent:
[Environment]::SetEnvironmentVariable("SHODAN_API_KEY", "your_api_key_here", "User")
```

---

## 📊 Shodan API Plans

### Free Plan
- ✅ 100 query credits per month
- ✅ Basic search results
- ✅ Good for learning and testing
- ⚠️ Limited results per query

### Membership Plan ($49/month)
- ✅ Unlimited query credits
- ✅ Full access to all data
- ✅ Advanced filtering options
- ✅ API access with no limits
- ✅ Recommended for serious bug bounty hunting

### Academic Plan (Free for students)
- ✅ Same as Membership plan
- ✅ Requires .edu email address
- ✅ Perfect for security students

---

## ✅ Verify Installation

Run these commands to ensure everything is working:
```bash
# Check Python version
python3 --version
# Should show: Python 3.6 or higher

# Check if dependencies are installed
pip3 list | grep -E "shodan|colorama|requests"
# Should show all three packages

# Check API key
echo $SHODAN_API_KEY
# Should show your API key

# Test the tool
python3 shodanhunter.py -list
# Should display available technologies
```

---

## 🐛 Troubleshooting

### Issue: "SHODAN_API_KEY not set"

**Solution:**
```bash
export SHODAN_API_KEY="your_actual_key_here"
```

### Issue: "Module not found: shodan"

**Solution:**
```bash
pip3 install -r requirements.txt
# or
pip3 install shodan colorama requests
```

### Issue: "Permission denied"

**Solution:**
```bash
chmod +x shodanhunter.py
```

### Issue: "API Error: Invalid API key"

**Solution:**
- Verify your API key at https://account.shodan.io
- Make sure there are no extra spaces
- Re-export the key: `export SHODAN_API_KEY="correct_key"`

### Issue: "API Error: Upgrade your plan"

**Solution:**
- You've exceeded the free tier limits
- Wait until next month for reset
- Or upgrade to paid plan

---

## 🔧 Advanced Setup

### Virtual Environment (Recommended)
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the tool
python shodanhunter.py -list
```

### Installing Nuclei (for vulnerability scanning)
```bash
# Linux/macOS
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# Or using apt (Kali Linux)
sudo apt install nuclei

# Update templates
nuclei -update-templates

# Verify installation
nuclei -version
```

---

## 🎯 Next Steps

After successful installation:

1. Read the [README](../README.md) for usage examples
2. Check [CONTRIBUTING](CONTRIBUTING.md) to add new technologies
3. Start hunting! Try: `python3 shodanhunter.py -tech citrix -d target.com -o results.txt`

---

## 📞 Need Help?

- Open an issue: https://github.com/algamil7x/ShodanHunter/issues
- Twitter: [@algamil7x](https://twitter.com/algamil7x)

---

**Happy Hunting! 🎯🔥**
