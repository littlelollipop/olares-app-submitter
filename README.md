# Olares App Submitter Skill

A comprehensive skill that helps developers submit applications to the Olares App Store. This skill provides complete workflow guidance for creating OAC (Olares Application Chart) packages, submitting PRs, and passing GitBot validation.

## 🌟 Features

- ✅ **Complete OAC Package Creation Guide** - Step-by-step instructions for creating compliant OAC packages
- ✅ **PR Submission Workflow** - Proper PR naming conventions and submission steps
- ✅ **GitBot Error Solutions** - 20+ real-world GitBot validation errors with solutions (discovered through actual testing)
- ✅ **Local Validation Script** - Python script to validate OAC packages before submission
- ✅ **Comprehensive Documentation** - Detailed references for OAC specification and submission guide

## 📦 Installation

### Option 1: Clone via Git

```bash
# Clone this repository to your local machine
git clone https://github.com/LittleLollipop/olares-app-submitter.git
```

### Option 2: Download ZIP

1. Visit https://github.com/LittleLollipop/olares-app-submitter
2. Click "Code" → "Download ZIP"
3. Extract to your desired location

## 🚀 Usage

### Basic Usage

When you need to submit an app to Olares App Store, provide the skill files to your AI assistant:

```
Please read the SKILL.md and references/ files to help me submit my app to Olares App Store.
```

The AI assistant will guide you through the process.

### Workflow Steps

1. **Create OAC Package**
   - Use the provided templates: `Chart.yaml` and `OlaresManifest.yaml`
   - Create `owners` file with your GitHub username
   - Ensure all required fields are present

2. **Validate Locally (Optional)**
   ```bash
   python3 /path/to/olares-app-submitter/scripts/validate_oac.py /path/to/your-app
   ```

3. **Submit PR**
   - Fork `https://github.com/beclab/apps`
   - Add your OAC directory to the forked repo
   - Create a Draft PR with proper naming: `[NEW][your-app][1.0.0] Title`
   - Click "Ready for review" to trigger GitBot validation

4. **Fix GitBot Errors**
   - Check PR comments for GitBot validation results
   - Refer to `references/gitbot-errors.md` for common errors and solutions
   - Fix issues and push new commits to trigger re-validation

## 📁 File Structure

```
olares-app-submitter/
├── SKILL.md                          # Skill definition and workflow guide
├── README.md                         # English README (this file)
├── README_zh.md                      # Chinese README
├── references/                       # Reference documentation
│   ├── oac-specification.md         # OAC package specification
│   ├── olares-submit-guide.md      # Detailed submission guide
│   └── gitbot-errors.md           # 20+ GitBot error solutions
└── scripts/                          # Utility scripts
    └── validate_oac.py             # Local OAC package validator
```

## 📖 Documentation

### Required Fields in OlaresManifest.yaml

**`metadata.icon` field** - Required by GitBot validation:
```yaml
metadata:
  name: your-app
  icon: https://app.cdn.olares.com/appstore/your-app/icon.png
```

**`entrances` field** - Define app entrance points:
```yaml
entrances:
- name: yourapp
  port: 80
  host: yourapp
  title: Your App Title
  icon: https://app.cdn.olares.com/appstore/your-app/icon.png
  openMethod: window
```

### Template Restrictions

- **Image field must be hardcoded** - Cannot use Helm template placeholders like `{{ .Values.image.tag }}` in `templates/deployment.yaml`
- **All container resources must be set** - Must define both `requests` and `limits` for memory and CPU

### Directory Naming Rules

- Only allowed characters: `a-z`, `A-Z`, `0-9`, space, `. , ! ? ; : ' " -`
- Maximum length: 30 characters
- **Hyphens (`-`) are NOT allowed** - Use underscores (`_`) instead

### PR Submission Rules

- **One PR = One directory** - Cannot modify multiple app directories in a single PR
- PR title must exactly match the directory name

## 🔍 Using This Skill with Different AI Assistants

This is a **universal skill** that can be used by any AI assistant.

### For Claude Users (via Claude API or Claude.ai)

Simply provide the skill files to Claude:
```
Please read the SKILL.md and references/ files to help me submit my app to Olares App Store.
```

Or upload the skill directory as context.

### For GPT Users (via GPTs or Assistants API)

1. Upload `SKILL.md` and `references/*.md` as knowledge files
2. Instruct the GPT: "Follow the workflow in SKILL.md to help submit an app to Olares"

### For Other AI Assistants

Any AI that can read Markdown can use this skill:
1. Read `SKILL.md` for workflow overview
2. Reference `references/gitbot-errors.md` when encountering errors
3. Use `scripts/validate_oac.py` for local validation (Python required)

## 📚 References

- [Olares Official Documentation](https://docs.olares.cn/zh/developer/develop/submit/)
- [Official Apps Repository](https://github.com/beclab/apps)
- [OAC Packaging Guide](https://docs.olares.cn/zh/developer/develop/package/chart.html)

## 🤝 Contributing

Found a new GitBot error? Please help improve this skill by:

1. Fork this repository
2. Add the new error and solution to `references/gitbot-errors.md`
3. Submit a Pull Request

## 📝 License

MIT License - feel free to use and modify this skill.

---

## 📊 Actual Test Results

**PR Submitted**: [#2185](https://github.com/beclab/apps/pull/2185) (Merged ✅)

**Errors Discovered**: 10 errors found during testing, all documented in `references/gitbot-errors.md`

**Value**: This skill provides real-world solutions to GitBot validation errors, helping developers save hours of trial-and-error.
