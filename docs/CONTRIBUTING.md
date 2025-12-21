# 🤝 Contributing to ShodanHunter

Thank you for your interest in contributing to ShodanHunter! This guide will help you get started.

---

## 🎯 Ways to Contribute

- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Add new technology queries
- 🎨 Improve UI/UX
- 🧪 Write tests
- 🌐 Add translations

---

## 🚀 Quick Start

### 1. Fork the Repository

Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/ShodanHunter.git
cd ShodanHunter
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 4. Make Your Changes

Edit the files you want to change.

### 5. Test Your Changes
```bash
# Test the tool
python3 shodanhunter.py -list

# Test with a target
python3 shodanhunter.py -tech citrix -d test.com -o test_results.txt
```

### 6. Commit Your Changes
```bash
git add .
git commit -m "Add support for NewTechnology"
```

### 7. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 8. Create Pull Request

Go to your fork on GitHub and click "New Pull Request".

---

## 🔧 Adding New Technologies

The most common contribution is adding support for new technologies. Here's how:

### Step 1: Create Query File

Create a new file in `queries/` directory:
```bash
nano queries/newtech.txt
```

Add Shodan queries for your technology:
```text
# NewTech Detection Queries
http.title:"NewTech"
product:"NewTech"
http.component:"NewTech"
ssl.cert.subject.cn:"newtech"
http.html:"newtech"
port:8080 http.title:"NewTech"
```

### Step 2: Update shodanhunter.py

Add your technology to the `AVAILABLE_TECH` dictionary:
```python
AVAILABLE_TECH = {
    'citrix': 'queries/citrix.txt',
    'jenkins': 'queries/jenkins.txt',
    # ... existing entries ...
    'newtech': 'queries/newtech.txt',  # Add this line
}
```

### Step 3: Test Your Addition
```bash
# List technologies (should show newtech)
python3 shodanhunter.py -list

# Test the new technology
python3 shodanhunter.py -tech newtech -d test.com -o test.txt
```

### Step 4: Update README

Add your technology to the table in README.md:
```markdown
| NewTech | newtech.txt | 20+ | ⭐⭐ |
```

### Step 5: Submit Pull Request

Include in your PR description:
- Technology name
- Why it's useful for bug bounty
- Number of queries added
- Example output (if possible)

---

## 📋 Query Writing Guidelines

### Good Queries

✅ **Specific and accurate:**
```text
http.title:"Jenkins Dashboard"
product:"Jenkins"
```

✅ **Multiple detection methods:**
```text
http.html:"jenkins"
http.favicon.hash:81586312
ssl.cert.subject.cn:"jenkins"
```

✅ **Include version detection:**
```text
http.html:"Jenkins 2.0"
```

### Bad Queries

❌ **Too generic:**
```text
http.html:"admin"  # Too many false positives
```

❌ **Single detection method:**
```text
http.title:"Login"  # Not specific enough
```

---

## 🐛 Reporting Bugs

### Before Reporting

- Check if the bug already exists in [Issues](https://github.com/algamil7x/ShodanHunter/issues)
- Try the latest version from `main` branch
- Collect relevant information

### Bug Report Template
```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Run command: `python3 shodanhunter.py ...`
2. See error

**Expected behavior**
What you expected to happen.

**Actual behavior**
What actually happened.

**Environment:**
- OS: [e.g., Ubuntu 22.04, Windows 11, macOS]
- Python version: [e.g., 3.10.2]
- ShodanHunter version: [e.g., v1.0]

**Error message (if any):**
```
Paste error here
```

**Additional context**
Any other relevant information.
```

---

## 💡 Feature Requests

Use this template for feature requests:
```markdown
**Feature description**
Clear description of the feature.

**Use case**
Why this feature would be useful.

**Proposed solution**
How you think it should work.

**Alternatives considered**
Other ways to achieve the same goal.

**Additional context**
Screenshots, examples, etc.
```

---

## 📝 Code Style Guidelines

### Python Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions small and focused
- Add comments for complex logic

### Example:
```python
def search_technology(tech_name, domain):
    """
    Search for a specific technology in a domain.
    
    Args:
        tech_name (str): Name of technology to search
        domain (str): Target domain
        
    Returns:
        list: List of URLs found
    """
    # Implementation here
    pass
```

---

## ✅ Pull Request Guidelines

### Before Submitting

- [ ] Test your changes thoroughly
- [ ] Update documentation if needed
- [ ] Follow code style guidelines
- [ ] Write clear commit messages
- [ ] Add your name to CONTRIBUTORS.md (if exists)

### PR Description Template
```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Changes Made
- Added support for NewTech
- Fixed bug in X
- Improved performance of Y

## Testing
Describe how you tested your changes.

## Screenshots (if applicable)
Add screenshots here.

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Changes tested
```

---

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md (if we create it)
- Mentioned in release notes
- Credited in commit history

---

## 📜 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Spam or advertising
- Any form of abuse

---

## 📞 Questions?

- Open an [Issue](https://github.com/algamil7x/ShodanHunter/issues)
- Twitter: [@algamil7x](https://twitter.com/algamil7x)
- Email: (if you want to add it)

---

## 🎉 Thank You!

Every contribution, no matter how small, helps make ShodanHunter better for everyone!

**Happy Contributing! 🚀**
